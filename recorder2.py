import os
import sounddevice as sd
import soundfile as sf
import whisper
import time

# Set the duration per clip
duration = 3  # Recording duration in seconds

# Set sampling freq for mic to record
sampling_frequency = 44100  # Sample rate (Hz)

# Create the "recordings" folder if it doesn't exist
folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recordings")
os.makedirs(folder_path, exist_ok=True)

# Set the device ID of the mic that you want to use
device_id = 0  # Change this value to use a different mic

# Get the name of the mic that we're using
device_name = sd.query_devices(device_id, "input")["name"]

# Set the filename of the recording
filename = f"{int(time.time())}_{device_name}.wav"

# Set the full path of the recording
file_path = os.path.join(folder_path, filename)

# Program Flow
# - create recordings folder
# - inp() allows for user to input in secs how long to rec.
# - record() opens mic; records in clips of 3 seconds or as set above
# - transcribe() transcribes finished clips and writes transcribed text in transcript.txt 

# Function to get user input
def inp():
    global duration
    duration = input("Enter duration of recording in seconds: ")
    duration = int(duration)
    print("Recording duration set to " + str(duration) + " seconds")
    print("")

# Function to record audio

def record():
    # Open the mic
    with sd.InputStream(samplerate=sampling_frequency, device=device_id, channels=2) as stream:
        # Create a soundfile object. This object will write the audio data
        # to the file we specify
        with sf.SoundFile(file_path, mode="x", samplerate=sampling_frequency, channels=2) as file:
            # Record the audio in chunks of 3 seconds
            for _ in range(int(duration * sampling_frequency / 1024)):
                # Read 3 seconds of audio data from the mic
                data = stream.read(1024)
                # Write the audio data to file
                file.write(data)
                print("Recording...")
                
# Function to transcribe audio
def transcribe():
    # Open the audio file
    with open(file_path, "rb") as audio_file:
        # Read the audio data
        audio_data = audio_file.read()
        # Transcribe the audio data
        text = whisper.transcribe(audio_data)
        # Write the transcribed text to file
        with open("transcript.txt", "a") as transcript_file:
            transcript_file.write(text)
            transcript_file.write("\n")
            print("Transcription complete")
            print("Transcription saved to transcript.txt")
            print("")


# Main function
def main():
    # Get user input
    inp()
    # Record audio
    record()
    # Transcribe audio
    transcribe()
    pass

if __name__ == "__main__":
    # run the program
    main()
#RECORDER
# note: all references to transcription should be moved first. w8 sht that means theres a lot of stuff 2 code
# fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk

# IMPORTS
import pyaudio  # Handles portaudio interface for Python. Allows access to microphone i think
import wave  # Allows writing of .wav files
import keyboard  # Read keyboard inputs in dev console. Only used for testing
import os  # Allows access to files and filepaths
import Transcriber  # move this shit later. smth smth recursive import
# see later for function interrupt - https://stackoverflow.com/a/47684708


# DEFAULTS (AUDIO RECORDING)
chunk = 1024  # i dont really understand this one - i think it determines how the mic input is split in the wav file?
sampleFormat = pyaudio.paInt16  # Recording format for audio
channels = 1  # Audio channels. 1 is mono, 2 is stereo. 1 is easier/more compatible w/ Whisper i think
sampleRate = 16000  # Audio sample rate. x bits per sec (i think)
seconds = 3  # How many seconds per audio clip
filename = "output"  # Will save audio into "filename" + n + ".wav"
folder = "recordings"
filedir = os.path.join(os.getcwd(), folder)  # Will save audio into local subdirectory
clipNo = 0  # Counts how many clips have been recorded so far
delAmt = 4  # Delete every x files, if savePrevFiles = False


def setup():
    # Creating recordings folder if unavailable
    if not os.path.isdir(filedir):
        os.mkdir(filedir)

    # Deleting previous recordings, if any. Deletes .wav files only
    if len(os.listdir(filedir)) > 0:
        print("Deleting previous recordings...")
        for file in os.listdir(filedir):
            x = 0
            if len(file) > 4:
                x = len(file) - 4
            
            if file[x:len(file)] == ".wav":
                os.remove(os.path.join(filedir, file))


def record(savePrevFiles = False):
    p = pyaudio.PyAudio()  # Open portaudio interface
    global clipNo

    print("Activating audio input stream... (Press space to deactivate in console/testing mode)")
    stream = p.open(rate=sampleRate, channels=channels, format=sampleFormat, input=True)

    # Recording proper
    print("Starting recording...")
    while True:  # Allows infinite recording until interrupted
        for i in range (sampleRate // chunk * seconds):  # Records until x seconds pass
            if i == 0:  # Creating a new wave file. Only runs at beginning of recording every x seconds
                wf = wave.open(os.path.join(filedir, filename+str(clipNo)+".wav"), 'wb')
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(sampleFormat))  # Setting amt. of bits for audio file (resolution)
                wf.setframerate(sampleRate)
                clipNo += 1
            wf.writeframes(stream.read(chunk))  # Saving of audio input into wav file

            if keyboard.is_pressed("space"):
                break
        
        # Transcriber.start_transcribe(os.path.join(filedir, filename+str(clipNo-1)+".wav"))  # move this crap later

        yield os.path.join(filedir, filename+str(clipNo-1)+".wav")

        # Deleting prev files; leaves one file just to be safe (errors may happen here btw; look into it later)
        if clipNo > 1 and (clipNo-1) % delAmt == 0 and not savePrevFiles:  
            todel = []
            for i in range(2, delAmt+2):
                todel.append(filename+str(clipNo-i)+".wav")
            for rec in os.listdir(filedir):
                if rec in todel:
                    os.remove(os.path.join(filedir, rec))
        
        if keyboard.is_pressed("space"):
            break
    
    print("Stream closed.")
    stream.close()
    p.terminate()

    return


if __name__ == "__main__":
    Transcriber.load_model() 

    setup()
    record()


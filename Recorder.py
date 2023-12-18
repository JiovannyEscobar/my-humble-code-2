# RECORDER - Made for the Whisper Transcription Desktop Research
# Written by geebees

# IMPORTS
import pyaudio  # Handles portaudio interface for Python. Allows access to microphone
import wave  # Allows writing of .wav files
import keyboard  # Read keyboard inputs in dev console. Only used in console mode
import os  # Allows access to files and filepaths
from threading import *  # Event & multithread handler
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
clipNo = 0  # Counts how many clips have been recorded so far. Always starts at one less than the next file to be recorded
delAmt = 4  # Delete every x files, if savePrevFiles = False
nextrecpath = ""  # Contains recording path for finished audio file
keepRecording = Event()
nextRecIsDone = Event()


def setup(deletePreviousAudio=True):
    global clipNo
    # Creating recordings folder if unavailable
    if not os.path.isdir(filedir):
        os.mkdir(filedir)

    # Deleting previous recordings, if any. Deletes .wav files only
    if len(os.listdir(filedir)) > 0:
        wavFiles = [file for file in os.listdir(filedir) if len(file)>3 and file[len(file)-4:len(file)]==".wav"]
        if deletePreviousAudio:
            print("Deleting previous recordings...")
            for file in wavFiles:
                os.remove(os.path.join(filedir, file))
        else:
            clipNo = len(wavFiles)


def StartRecord(verbose=False):
    t = Thread(target=record, args=(verbose, ))
    print("Starting record thread...")
    keepRecording.set()
    t.start()


"""def record(savePrevFiles = False, verbose=False):
    p = pyaudio.PyAudio()  # Open portaudio interface
    global clipNo

    print("Activating audio input stream... (Press space to deactivate in console/testing mode)")
    stream = p.open(rate=sampleRate, channels=channels, format=sampleFormat, input=True)

    # Recording proper
    print("Starting recording...")
    isRecording.set()
    while isRecording.is_set():  # Allows infinite recording until interrupted
        for i in range (sampleRate // chunk * seconds):  # Records until x seconds pass
            if i == 0:  # Creating a new wave file. Only runs at beginning of recording every x seconds
                wf = wave.open(os.path.join(filedir, filename+str(clipNo)+".wav"), 'wb')
                wf.setnchannels(channels)
                wf.setsampwidth(p.get_sample_size(sampleFormat))  # Setting amt. of bits for audio file (resolution)
                wf.setframerate(sampleRate)
                clipNo += 1
            wf.writeframes(stream.read(chunk))  # Saving of audio input into wav file

            # Should only be used in console mode
            if keyboard.is_pressed("space"):
                break
        
        # Transcriber.start_transcribe(os.path.join(filedir, filename+str(clipNo-1)+".wav"))  # move this crap later

        global nextrecpath
        nextrecpath = os.path.join(filedir, filename+str(clipNo-1)+".wav")
        nextRecIsDone.set()
        if verbose:
            print("Recorded", nextrecpath)

        # Deleting prev files; leaves one file just to be safe (errors may happen here btw; look into it later)
        if clipNo > 1 and (clipNo-1) % delAmt == 0 and not savePrevFiles:  
            todel = []
            for i in range(2, delAmt+2):
                todel.append(filename+str(clipNo-i)+".wav")
            for rec in os.listdir(filedir):
                if rec in todel:
                    os.remove(os.path.join(filedir, rec))
        
        # Should only be used in console mode
        if keyboard.is_pressed("space"):
            break
    
    print("Stream closed.")
    stream.close()
    p.terminate()

    return

"""
def record(verbose=False):
    # Records audio files, then appends finished filepaths into global list. NOTE: To use, make sure to implement event handling

    p = pyaudio.PyAudio()  # Open portaudio interface
    global clipNo

    print("Activating audio input stream... (Press space to deactivate in console/testing mode)")
    stream = p.open(rate=sampleRate, channels=channels, format=sampleFormat, input=True)

    # Recording
    print("Starting recording...") if verbose else None
    while keepRecording.is_set():  # Allows infinite recording until interrupted
        for i in range (sampleRate // chunk * seconds):  # Records until 'seconds' amt. of seconds pass
            if keepRecording.is_set():
                if i == 0:  # Creating a new wave file. Only runs at beginning of recording every file
                    wf = wave.open(os.path.join(filedir, filename+str(clipNo)+".wav"), 'wb')
                    wf.setnchannels(channels)
                    wf.setsampwidth(p.get_sample_size(sampleFormat))  # Setting amt. of bits for audio file (resolution)
                    wf.setframerate(sampleRate)
                    clipNo += 1
                wf.writeframes(stream.read(chunk))  # Saving of audio input into wav file
            else:
                break
        
        global nextrecpath
        nextrecpath = os.path.join(filedir, filename+str(clipNo-1)+".wav")
        nextRecIsDone.set()
    
    print("Stream closed.") if verbose else None
    stream.close()
    p.terminate()

    return


if __name__ == "__main__":
    # Transcriber.load_model() 

    setup()
    StartRecord(verbose=True)

    while keepRecording.is_set():
        if nextRecIsDone.is_set():
            print("Recorded", nextrecpath)
            nextRecIsDone.clear()
        if keyboard.is_pressed("space"):
            keepRecording.clear()


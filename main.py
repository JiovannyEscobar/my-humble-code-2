# Whisper Transcription Desktop Research
# Run this file to run the app in console mode

import Recorder
import Transcriber
from threading import *
import os
import keyboard

running = Event()
loadingFinished = Event()
wavFiles = []

def LiveTranscription(modelsize, modellang):
    running.set()
    loadingFinished.clear()
    Transcriber.load_model(size=modelsize, lang=modellang)
    Recorder.setup()
    Recorder.StartRecord()
    loadingFinished.set()
    
    while Recorder.keepRecording.is_set():
        recs = [x for x in os.listdir(Recorder.filedir) if ".wav" in x]
        if Transcriber.doneTranscribing.is_set() and len(recs) > 1:
            t = Thread(target=CallTranscribe, args=(recs,))
            t.start()

    running.clear()


def CallTranscribe(recs):
    i = float('inf')
    for rec in recs:
        recnum = int("".join([str(y) for y in rec if y.isnumeric()]))
        i = recnum if recnum < i else i
    
    file = "output"+str(i)+".wav"
    Transcriber.start_transcribe(os.path.join(Recorder.filedir, file), waitEachFile=True)
    recs = []

if __name__ == "__main__":
    Transcriber.load_model()
    Recorder.setup()
    Recorder.StartRecord()
    
    while Recorder.keepRecording.is_set():
        recs = [x for x in os.listdir(Recorder.filedir) if ".wav" in x]

        if keyboard.is_pressed("space"):
            Recorder.keepRecording.clear()
            break

        if Transcriber.doneTranscribing.is_set() and len(recs) > 1:
            i = float('inf')
            for rec in recs:
                recnum = int("".join([str(y) for y in rec if y.isnumeric()]))
                i = recnum if recnum < i else i
            
            file = "output"+str(i)+".wav"
            Transcriber.start_transcribe(os.path.join(Recorder.filedir, file), waitEachFile=True)
            recs = []


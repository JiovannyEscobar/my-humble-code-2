# Whisper Transcription Desktop Research
# Run this file to run the app in console mode

import Recorder
import Transcriber
from threading import *
import os
import keyboard

running = Event()
    
if __name__ == "__main__":
    # don't run this yet
    Transcriber.load_model(size="small", amt=1)
    Recorder.setup()
    Recorder.StartRecord()
    recpath = os.path.join(os.getcwd(), "recordings")

    while Recorder.keepRecording.is_set():
        """if Recorder.nextRecIsDone.is_set():
            try:
                Transcriber.start_transcribe(Recorder.nextrecpath, waitEachFile=True, deleteFinishedFiles=False, verbose=True)
                Recorder.nextRecIsDone.clear()
            except:
                break
        if keyboard.is_pressed("space"):
            Recorder.keepRecording.clear()
            if Recorder.nextRecIsDone.is_set():
                try:
                    Transcriber.start_transcribe(Recorder.nextrecpath, waitEachFile=True, deleteFinishedFiles=False, verbose=True)
                    Recorder.nextRecIsDone.clear()
                except:
                    break"""
        recs = [x for x in os.listdir(recpath) if ".wav" in x]
        if keyboard.is_pressed("space"):
            Recorder.keepRecording.clear()

            while recs != []:
                if Transcriber.doneTranscribing.is_set():
                    i = float('inf')
                    for x in recs:
                        recnum = int("".join([str(y) for y in x if y.isnumeric()]))
                        if recnum < i:
                            i = recnum
                    
                    print("transcribe", i)
                    file = "output"+str(i)+".wav"
                    try:
                        Transcriber.start_transcribe(os.path.join(os.getcwd(), "recordings", file), verbose=True, waitEachFile=True, deleteFinishedFiles=True)
                        recs.pop(recs.index(file))
                    except:
                        break
        if Transcriber.doneTranscribing.is_set() and len(recs) > 1:
            i = float('inf')
            for x in recs:
                recnum = int("".join([str(y) for y in x if y.isnumeric()]))
                if recnum < i:
                    i = recnum
            
            print("transcribe", i)
            try:
                Transcriber.start_transcribe(os.path.join(os.getcwd(), "recordings", "output"+str(i)+".wav"), verbose=True, waitEachFile=True, deleteFinishedFiles=True)
            except:
                break


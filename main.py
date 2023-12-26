# Whisper Transcription Desktop Research
# Run this file to run the app in console mode

import Recorder
import Transcriber
from threading import *
import os
import keyboard

running = Event()
loadingFinished = Event()
done = Event()
wavFiles = []
stopCalled = Event()


def LiveTranscription(modelsize, modellang, consoleMode=False):
    done.clear()
    stopCalled.clear()
    running.set()
    loadingFinished.clear()
    
    Transcriber.load_model(size=modelsize, lang=modellang)
    Recorder.setup()
    Recorder.StartRecord()
    loadingFinished.set()

    while Recorder.keepRecording.is_set():
        recs = [x for x in os.listdir(Recorder.filedir) if ".wav" in x]

        if (consoleMode and keyboard.is_pressed("space")) or stopCalled.is_set():
            Recorder.keepRecording.clear()
            break

        if Transcriber.doneTranscribing.is_set() and len(recs) > 1:
            recs = []
            recs = [x for x in os.listdir(Recorder.filedir) if ".wav" in x]
            # Selecting earliest clip
            """t = Thread(target=SelectEarliestClip, args=(recs,))
            t.start()"""
            SelectEarliestClip(recs)
        recs = []

    # Live transcription is stopped
    t = Thread(target=Final)
    t.start()


def SelectEarliestClip(recs):
    recnum = float('inf')
    for rec in recs:
        i = int("".join([str(x) for x in rec if x.isnumeric()]))
        recnum = i if i < recnum else recnum

    file = Recorder.filename + str(recnum) + ".wav"
    """t = Thread(target=Transcriber.start_transcribe, args=(os.path.join(Recorder.filedir, file), True, True, False))
    t.start()"""
    Transcriber.start_transcribe(os.path.join(Recorder.filedir, file), waitEachFile=True)


def Final():
    recs = [rec for rec in os.listdir(os.path.join(os.getcwd(), Recorder.filedir)) if ".wav" in rec]

    print("Recording stopped. Files pending transcription:", recs)
    while not recs == []:
        recs = []
        recs = [rec for rec in os.listdir(os.path.join(os.getcwd(), Recorder.filedir)) if ".wav" in rec]
        if Transcriber.doneTranscribing.is_set() and len(recs) > 0:
            recnum = float('inf')
            for rec in recs:
                i = int("".join([str(x) for x in rec if x.isnumeric()]))
                recnum = i if i < recnum else recnum

            if recnum == float('inf'):
                break
            file = Recorder.filename + str(recnum) + ".wav"
            try:
                Transcriber.start_transcribe(os.path.join(Recorder.filedir, file), waitEachFile=True)
            except:
                continue

    running.clear()
    done.set()


if __name__ == "__main__":
    t = Thread(target=LiveTranscription, args=("small", "en", True))
    t.start()


# TRANSCRIBER - Made for the Whisper Transcription Desktop Research
# Written by geebees

# IMPORTS
import whisper
from threading import Thread, Event
import torch
import os
import time
import datetime


# TRANSCRIPTION DEFAULTS
global models
models = []
_device = "cpu"
global transcriptPath
transcriptPath = "transcriptions/"+str(datetime.date.today())+"-"+str(int(time.time()))+".txt"
global transcriptStartTime
transcriptStartTime = None
transcriptIsDone = Event()


def load_model(amt=4, size="small", lang="en"):  # me <3 small.en
    """HOW TO FIX BATCH MISMATCH ERROR THING? theoretically, load multiple models at once, alternate between"""
    if torch.cuda.is_available():  # Pytorch w/ cuda support is available; uses gpu
        print("Loading Transcribe using GPU...")
        _device = "cuda"
    else:
        print("Loading Transcribe using CPU...")

    if lang != "":
        lang = "." + lang
    modelname = size+lang

    print("Loading", amt, "model/s of Whisper AI ("+modelname+")")
    for i in range(amt):
        models.append([whisper.load_model(modelname, device=_device), False])
        print("loaded", modelname, "model #", i)


def transcribe(filepath, m, verbose=True):
    model = models[m][0]

    if verbose:
        print("Transcribing", filepath, "with model #", m, "to file", transcriptPath)
    try:
        transcription = model.transcribe(filepath)
        print(filepath, transcription["text"])

        # Write to file
        with open(transcriptPath, mode="a", encoding="utf-8") as txt:
            txt.write(transcription["text"]+"\n")
    except:
        # print("Error in transcribing", filepath, "; this may be caused by simultaneous transcription, and idk how"
        #       " to fix that issue yet")
        raise RuntimeError
    models[m][1] = False
    # transcriptIsDone.set()
    return


def start_transcribe(filepath, waitEachFile = False):  # allows multithreading. note: just realized if waitEachFile = True, this function is worthless
    """Used for multithreading & simultaneous transcription of multiple wav files. Note that Whisper processing multiple
    files is unstable and regularly returns errors. NOTE: waitEachFile = True is highly unstable & should only be used
    for testing"""
    for model in models:
        if not model[1]:
            m = models.index(model)
            model[1] = True
            break
        if models.index(model) == len(models)-1:
            # currently just warns you and doesn't do anything else
            print("Models all busy! Transcription cannot be done. Shutting down program...")
            m = 0

    t = Thread(target=transcribe, args=(filepath, m, ))

    t.start()
    if waitEachFile:
        t.join()


if __name__ == "__main__":
    load_model("small")

    for rec in os.listdir("recordings"):
        tstart = time.time()
        start_transcribe(os.path.join(os.getcwd(), rec), True)
        tstop = time.time()
        print("Time taken to transcribe", rec, ":", str(tstop-tstart))


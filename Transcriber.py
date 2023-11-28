# TRANSCRIBER

# IMPORTS
import whisper
from threading import Thread
import torch
import os
import time  # For testing only


# TRANSCRIPTION DEFAULTS
global models
models = []
_device = "cpu"


if torch.cuda.is_available():  # Pytorch w/ cuda support is available; uses gpu
    print("Loading Transcribe using GPU...")
    _device = "cuda"
else:
    print("Loading Transcribe using CPU...")


def load_model(amt=4, size="small", lang="en"):  # me <3 small.en
    """HOW TO FIX BATCH MISMATCH ERROR THING? theoretically, load multiple models at once, alternate between"""
    modelname = size+"."+lang

    print("Loading", amt, "model/s of Whisper AI ("+modelname+")")
    try:
        for i in range(amt):
            models.append([whisper.load_model(modelname, device=_device), False])
    except:
        print("Unrecognized model. Pls fix")
        quit()


def transcribe(filepath, m, verbose=True):
    model = models[m][0]

    if verbose:
        print("Transcribing", filepath, "with model #", m)
    try:
        transcription = model.transcribe(filepath)
        print(filepath, transcription["text"])
    except:
        print("Error in transcribing", filepath, "; this may be caused by simultaneous transcription, and idk how"
              " to fix that issue yet")
    models[m][1] = False
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
            print("Models all busy! Transcription cannot be done. Shutting down program...")
            quit()

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


# TRANSCRIBER

# IMPORTS
import whisper
from threading import Thread
import torch
import os
import time  # For testing only


# TRANSCRIPTION DEFAULTS
model = None
_device = "cpu"


if torch.cuda.is_available():  # Pytorch w/ cuda support is available; uses gpu
    print("Loading Transcribe using GPU...")
    _device = "cuda"
else:
    print("Loading Transcribe using CPU...")


def load_model(size="small", lang="en"):  # me <3 small.en
    modelname = size+"."+lang
    global model

    print("Loading Whisper AI ("+modelname+")")
    try:
        model = whisper.load_model(modelname, device=_device)
    except:
        print("Unrecognized model. Pls fix")
        quit()


def transcribe(filepath, verbose=True):
    global model

    if verbose:
        print("Transcribing", filepath)
    transcription = model.transcribe(filepath)
    print(transcription["text"])
    return


def start_transcribe(filepath, waitEachFile = False):  # allows multithreading. note: just realized if waitEachFile = True, this function is worthless
    t = Thread(target=transcribe, args=(filepath,))

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


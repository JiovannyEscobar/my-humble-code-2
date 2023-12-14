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
doneTranscribing = Event()
doneTranscribing.set()


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


def transcribe(filepath, m, verbose=True, deleteFinishedFiles=True, waitEachFile=False):
    model = models[m][0]

    if verbose:
        print("Transcribing", filepath, "with model #", m, "to file", transcriptPath) if verbose else None
    try:
        transcription = model.transcribe(filepath)
        print(filepath, "  ", transcription["text"])

        # Write to file
        with open(transcriptPath, mode="a", encoding="utf-8") as txt:
            txt.write(transcription["text"]+"\n")
    except:
        # print("Error in transcribing", filepath, "; this may be caused by simultaneous transcription, and idk how"
        #       " to fix that issue yet")
        raise RuntimeError
    if deleteFinishedFiles:
        os.remove(filepath)  # Delete file once done with transcription
        print("Deleted finished file", filepath) if verbose else None
    if waitEachFile:
        doneTranscribing.set()
    models[m][1] = False
    return


def start_transcribe(filepath, waitEachFile = False, verbose = False, deleteFinishedFiles=True):  # allows multithreading. note: just realized if waitEachFile = True, this function is worthless
    """Used for multithreading & simultaneous transcription of multiple wav files. Note that Whisper processing multiple
    files is unstable and regularly returns errors. NOTE: waitEachFile = True is highly unstable & should only be used
    for testing"""
    for model in models:
        if not model:
            m = models.index(model)
            model = True
            break
        if models.index(model) == len(models)-1:
            # currently just warns you and defaults back to m=0
            # print("Models all busy! Transcription cannot be done. Shutting down program...")
            m = 0
    if waitEachFile:
        doneTranscribing.clear()

    t = Thread(target=transcribe, args=(filepath, m, verbose, deleteFinishedFiles, waitEachFile,))

    t.start()


if __name__ == "__main__":
    load_model(amt=1, size="small")

    recs = [x for x in os.listdir("recordings") if ".wav" in x]
    while not recs == []:
        i = float('inf')
        for rec in recs:
            recnum = int("".join([str(x) for x in rec if x.isnumeric()]))
            if recnum <= i:
                i = recnum
    
        tstart = time.time()
        start_transcribe(os.path.join(os.getcwd(), "recordings", "output"+str(i)+".wav"), waitEachFile=False, verbose=True, deleteFinishedFiles=False)
        tstop = time.time()
        print("     Time taken to transcribe output"+str(i)+".wav:", str(tstop-tstart))
        recs.pop(recs.index("output"+str(i)+".wav"))
    """for rec in os.listdir("recordings"):
        if ".wav" in rec:
            tstart = time.time()
            start_transcribe(os.path.join(os.getcwd(), "recordings", rec), True, verbose=True, deleteFinishedFiles=False)
            tstop = time.time()"""


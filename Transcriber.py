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
global transcriptPath
transcriptPath = "transcriptions/"+str(datetime.date.today())+"-"+str(int(time.time()))+".txt"
global transcriptStartTime
transcriptStartTime = None
doneTranscribing = Event()
doneTranscribing.set()
model = None  # Contains Whisper model to load


def load_model(size="small", lang="en"):  # me <3 small.en
    _device = "cpu"
    global model
    
    if torch.cuda.is_available():  # Pytorch w/ cuda support is available; uses gpu
        print("Loading Transcribe using GPU...")
        _device = "cuda"
    else:
        print("Loading Transcribe using CPU...")

    if lang != "":
        lang = "." + lang
    modelname = size+lang

    print("Loading", modelname, "model of Whisper AI")
    model = whisper.load_model(modelname, device=_device)


def transcribe(filepath, waitEachFile=True, deleteFinishedFiles=True, verbose=True):
    print("Transcribing", filepath, "to file", transcriptPath) if verbose else None
    transcription = model.transcribe(filepath)
    print(filepath, "  ", transcription["text"])

    # Write to file
    with open(transcriptPath, mode="a", encoding="utf-8") as txt:
        txt.write(transcription["text"]+"\n")
    
    if deleteFinishedFiles:
        os.remove(filepath)  # Delete file once done with transcription
        print("Deleted finished file", filepath) if verbose else None
    if waitEachFile:
        doneTranscribing.set()
    return


def start_transcribe(filepath, waitEachFile = True,  deleteFinishedFiles=True, verbose = False):  
    # allows multithreading. NOTE: may be unstable if waitEachFile is False
    """Used for multithreading & simultaneous transcription of multiple wav files. Note that Whisper processing multiple
    files is unstable and regularly returns errors. NOTE: waitEachFile = True is highly unstable & should only be used
    for testing"""
    if waitEachFile:
        doneTranscribing.clear()

    try:
        t = Thread(target=transcribe, args=(filepath, waitEachFile, deleteFinishedFiles, verbose,))

        t.start()
    except:
        doneTranscribing.set()


if __name__ == "__main__":
    load_model(amt=1, size="small")

    recs = [x for x in os.listdir("recordings") if ".wav" in x]
    while not recs == []:
        if doneTranscribing.is_set():
            i = float('inf')
            for rec in recs:
                recnum = int("".join([str(x) for x in rec if x.isnumeric()]))
                if recnum <= i:
                    i = recnum
        
            tstart = time.time()
            start_transcribe(os.path.join(os.getcwd(), "recordings", "output"+str(i)+".wav"), waitEachFile=True, verbose=True, deleteFinishedFiles=False)
            tstop = time.time()
            print("     Time taken to transcribe output"+str(i)+".wav:", str(tstop-tstart))
            recs.pop(recs.index("output"+str(i)+".wav"))
        """for rec in os.listdir("recordings"):
            if ".wav" in rec:
                tstart = time.time()
                start_transcribe(os.path.join(os.getcwd(), "recordings", rec), True, verbose=True, deleteFinishedFiles=False)
                tstop = time.time()"""


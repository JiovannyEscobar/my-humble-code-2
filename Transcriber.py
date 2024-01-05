# TRANSCRIBER - Made for the Whisper Transcription Desktop Research
# Written by geebees

# IMPORTS
import whisper
from threading import Thread, Event
import torch
import os
import time
import datetime
import langdetect


# TRANSCRIPTION DEFAULTS
global transcriptPath
transcriptPath = "transcriptions/tr-"+str(datetime.date.today())+"-"+str(int(time.time()))+".txt"
global transcriptStartTime
transcriptStartTime = None
doneTranscribing = Event()
doneTranscribing.set()
model = None  # Contains Whisper model to load
usedLang = ""
langdetect.DetectorFactory.seed = 0


def load_model(size="small", lang="en"):  # me <3 small.en
    _device = "cpu"
    global model, usedLang
    
    if torch.cuda.is_available():  # Pytorch w/ cuda support is available; uses gpu
        print("Loading Transcribe using GPU...")
        _device = "cuda"
    else:
        print("Loading Transcribe using CPU...")

    if lang != "":
        usedLang = "english"  # Hardcoded: language in English (en)
        lang = "." + lang
    else:
        usedLang = "tagalog"  # Hardcoded: all other langs are filipino
    modelname = size+lang

    print("Loading", modelname, "model of Whisper AI")
    model = whisper.load_model(modelname, device=_device)


    with open(transcriptPath, mode="w", encoding="utf-8") as txt:
        txt.write("")


def IsModelLoaded(size, lang):
    modelsPath = os.path.join(os.path.expanduser("~"), ".cache", "whisper")
    if lang == "en":
        lang = "."+lang
    else:
        lang = ""
    if size+lang+".pt" in os.listdir(modelsPath):
        print("Model is downloaded locally")
        return True
    else:
        print("Model is not downloaded locally")
        return False


def transcribe(filepath, deleteFinishedFiles=True, verbose=True):
    global usedLang
    print("Transcribing", filepath, "to file", transcriptPath, "in lang", usedLang) if verbose else None
    try:
        transcription = model.transcribe(filepath, language=usedLang)

        """try:
            if not usedLang == "en":
                detLang = langdetect.detect(transcription["text"])
                print("    Language:", detLang)
                if not detLang == "tl":
                    print("     Not in selected language. Skip")
                    doneTranscribing.set()
                    return
        except:
            print("    Error detecting language")"""
    except:
        print("Error transcribing", filepath)
        doneTranscribing.set()
        return
    print(filepath, "  ", transcription["text"])

    # Write to file
    with open(transcriptPath, mode="a", encoding="utf-8") as txt:
        txt.write(transcription["text"]+"\n")
    
    if deleteFinishedFiles:
        try:
            os.remove(filepath)  # Delete file once done with transcription
            print("Deleted finished file", filepath) if verbose else None
        except:
            print("Error deleting", filepath)
    doneTranscribing.set()
    return


def start_transcribe(filepath,  deleteFinishedFiles=True, verbose = False):  
    # allows multithreading. NOTE: may be unstable if waitEachFile is False
    """Used for multithreading & simultaneous transcription of multiple wav files. Note that Whisper processing multiple
    files is unstable and regularly returns errors. NOTE: waitEachFile = True is highly unstable & should only be used
    for testing"""
    doneTranscribing.clear()

    try:
        t = Thread(target=transcribe, args=(filepath, deleteFinishedFiles, verbose,), daemon=True)

        t.start()
    except:
        doneTranscribing.set()


if __name__ == "__main__":
    load_model(size="small", lang="en")

    recs = [x for x in os.listdir("recordings") if ".wav" in x]
    while not recs == []:
        if doneTranscribing.is_set():
            i = float('inf')
            for rec in recs:
                recnum = int("".join([str(x) for x in rec if x.isnumeric()]))
                if recnum <= i:
                    i = recnum
        
            start_transcribe(os.path.join(os.getcwd(), "recordings", "rec-"+str(i)+".wav"), verbose=True, deleteFinishedFiles=False)
            recs.pop(recs.index("rec-"+str(i)+".wav"))
            doneTranscribing.wait()
        """for rec in os.listdir("recordings"):
            if ".wav" in rec:
                tstart = time.time()
                start_transcribe(os.path.join(os.getcwd(), "recordings", rec), True, verbose=True, deleteFinishedFiles=False)
                tstop = time.time()"""


import os
import wave
import numpy
from faster_whisper import WhisperModel
from threading import Thread
import datetime
import time
import langid
import translate
import whisper
import tkinter
from tkinter import messagebox

def convwavtoarr(filepath):
    wav = wave.open("recordings/output16.wav")
    samples = wav.getnframes()
    audio = wav.readframes(samples)

    audioasnpint16 = numpy.frombuffer(audio, dtype=numpy.int16)
    audioasnpfl32 = audioasnpint16.astype(numpy.float32)

    max_int16 = 2**15
    audionormalized = audioasnpfl32/max_int16
    print(audionormalized)

"""
# FASTERWHISPER TESTING
model = WhisperModel("medium.en", device="cpu")
def transcribe(filepath):
    segments, _ = model.transcribe(filepath, beam_size=5)
    segments = list(segments)
    print(filepath, segments)


def s_t(filepath):
    t = Thread(target=transcribe, args=(filepath, ))

    t.start()"""

"""global transcriptPath
transcriptPath = "transcriptions/"+str(datetime.date.today())+"-"+str(int(time.time()))+".txt"

def write():
    with open(transcriptPath, "a", encoding="utf-8") as txt:
        txt.write("Hello world")

write()"""
"""
with open("transcriptions/2023-12-03-1701542236.txt") as f:
    lines = f.readlines()
print(lines)"""

"""# HUGGINGFACE TESTING
import wave  
import numpy
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
model.config.forced_decoder_ids = WhisperProcessor.get_decoder_prompt_ids(language="english", task="transcribe")

def conv_wav_to_arr(filepath):
    wav = wave.open(filepath)
    samples = wav.getnframes()
    audio = wav.readframes(samples)

    audioasnpint16 = numpy.frombuffer(audio, dtype=numpy.int16)
    audioasnpfl32 = audioasnpint16.astype(numpy.float32)

    max_int16 = 2**15
    audionormalized = audioasnpfl32/max_int16
    return audionormalized


def start_transcribe(filepath, waitEachFile = False):
    wavArr = conv_wav_to_arr(filepath)
    inputFeatures = processor(wavArr, 16000, return_tensors="pt").inputfeatures
    predids = model.generate(inputFeatures)
    t = processor.batch_decode(predids, skip_special_tokens=True)


start_transcribe("recordings/output16.wav")"""

# print(os.listdir(os.path.join(os.getcwd(), "recordings")))

"""listy = [1, 2, 3, 4, 5]
print(listy)
listy.remove(3)
print(listy)"""

"""with open("transcriptions/2023-12-26-1703571023.txt", mode='r') as txt:
    txtList = txt.readlines()
    for x  in range(len(txtList)):
        txtList[x] = txtList[x].strip()
    print(txtList)"""

"""lang, _ = langid.classify("Hello world!")"""
translator = translate.Translator(to_lang="fil")
"""translation = translator.translate("Hello world!")
print(lang)
print(translation)"""

model = whisper.load_model("large")
for file in os.listdir("recordings"):
    if ".wav" in file:
        transcript = model.transcribe("recordings/"+file)
        print(transcript["text"])
        ttranscript = model.transcribe("recordings/"+file, language="tagalog")
        print(ttranscript["text"])


"""def IsModelLoaded(size, lang):
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
print(IsModelLoaded("large", ""))

root = tkinter.Tk()
box = messagebox.askokcancel(title="Model not downloaded", message="Model not found locally. Will now download missing model (requires internet connection). Continue?")
if box:
    print(True)
else:
    print(False)
root.mainloop()"""

import os
import wave
import numpy
from faster_whisper import WhisperModel
from threading import Thread
import datetime
import time

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

with open("transcriptions/2023-12-03-1701542236.txt") as f:
    lines = f.readlines()
print(lines)

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
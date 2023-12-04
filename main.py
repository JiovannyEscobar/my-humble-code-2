# Whisper Transcription Desktop Research
# Run this file to run the app in console mode

import Recorder
import Transcriber
from threading import *

transcribedFilepaths = []
isRecordingNew = False

def StartLiveTranscription(_lang, _size):
    Transcriber.load_model(lang=_lang, size=_size)
    Recorder.setup()

    t = Thread(target=Recorder.record)
    t.start()


def TranscribeSelectedClip(filepath):
    if filepath != "" and not filepath in transcribedFilepaths:
        transcribedFilepaths.append(Recorder.recpath)
        Transcriber.start_transcribe(Recorder.recpath)

if __name__ == "__main__":
    Transcriber.load_model()
    Recorder.setup()
    function = Recorder.record()
    while True: 
        try:
            Transcriber.start_transcribe(function.__next__())
        except:
            break
    

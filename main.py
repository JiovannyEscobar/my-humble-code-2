
import Recorder
import Transcriber


Transcriber.load_model()
Recorder.setup()
function = Recorder.record()
while True: 
    try:
        Transcriber.start_transcribe(function.__next__())
    except:
        break
    
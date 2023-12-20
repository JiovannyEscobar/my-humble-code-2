
Hello my friends. 

# whisper transcriber software
run gui.py to see app
run main.py for console mode (currently nonfunctional)
[<img src="https://i.ytimg.com/vi/aAtF-Zzdnc8/hqdefault.jpg" width="50%">](https://www.youtube.com/embed/aAtF-Zzdnc8?si=Y2RkNxhsbKnsCPrN)

## PATCH NOTES VER 0.4.3.6 (PYAUDIO VERSION)
- GUI reactivated; GUI now (partially) functional
- issues:
    - flickering text box
    - multithreading issue in GUI
    - stop not working properly
    - not automatically scroll down when update
    - stop button is available during model load
    - TLDR gui is not good working

### ISSUES
also in [here](https://github.com/JiovannyEscobar/my-humble-code-2/issues)
- currently can't display transcription in text box
    - needs to transcribe only when transcription of a file is done, not all the time (for efficiency)
- there is no fili model actually? just left lang as blank when fili is selected, meaning it may transcribe in other languages?
- drag&drop not yet implemented; will require a LOT more coding
    - split drag&dropped audio into 30sec intervals
    - preprocess intervals (samplerate, audio resolution, etc)
    - transcribe intervals
- i feel like code is now spaghetti bc i didnt add events and other stuff
- doesn't output transcript DURING recording, usually does it AFTER stop recording is pressed now
    - idk why ????!
- closing window doesn't stop app
- stop button automatically stops entire program without final update of output textbox
- gui needs to update during live transcription
    - no indicator of model loading
    - model customization still accessible during live transcription (may result in ![your computer blowing up](https://img.freepik.com/premium-psd/nuclear-bomb-explosion-isolated-transparent-background_879541-787.jpg?w=2000))
- other stuff i forgot lol
![me when coding](https://static-00.iconduck.com/assets.00/loudly-crying-face-emoji-1013x1024-xg3rnr6e.png)

### V4.0
- recorder basic functionality implemented
- transcriber basic functionality implemented
- using pyaudio as audio handling module
- seamless recording
    - microphone is now constantly active
    - no more missing audio between files
- gui is currently not implemented
    - gui.py is ignored by Recorder and Transcriber
- deletes 4 files per 5 recordings as per leedr's request
    - no u cant delete the other recording bc it will return error while transcribing
- supports cuda; whisper will now use gpu by default
- transcriber may return runtimeerrors:
    - this happens mostly when there is quiet/noisy(no speech) file
    - so far i've chosen to ignore it
    - might be a problem? who knows ???
- clean1
- not very accurate
    - clip cutting speech affects accuracy
- works

### COMMENTS ON PATCH NOTES VER 4

Great work my friend.

    Let's not do VAD
    It's fine if it is not accurate, so no need to combine (let's see first how inaccurate actually)
    Let's not do subtitling function (for now)
    Let's not do voice commands (Unless you like). Have a button to stop start and stop stuff.

If you have any more questions or need further assistance with anything, feel free to ask. Happy coding!

## DEPENDENCIES
### List
pls update with any new modules
1. Whisper AI
2. Pytorch
3. Pyaudio
4. Wave(?)
5. Tkinterdnd2(?)

### Installation & Reference code
You must have Whisper AI working first.
See this video.
https://www.youtube.com/watch?v=ABFqbY_rmEk&ab_channel=KevinStratvert

Also, this is my reference code.
https://github.com/JohnZolton/scribe


## To complete program:
### GBS's list
#### main.py
~~- create new file where all functions can be called~~
~~- adjust how input stream & wav writing is done in Recorder~~
~~- find way to return wav filepath from ongoing recorder function~~
#### GUI
~~- GUI currently not supported by code~~
~~- get this crap workin on d GUI J.E. made~~
- fix issues during live transcribe
    - not greyed out customization options
    - closing gui doesn't terminate program
- stop button doesn't "stop" accurately
- conditions for stopping and starting
    - only stop when
        - models loaded
        - program setup complete
    - only start when
        - prev models deleted
        - prev transcriptions finished
        - output box updated to display final transcription
- fix updating of text box
    - immediately update only when new transcript is available 
### Transcriber
- fix issues where transcript is unavailable until after live transcribe is stopped
#### language and model choices
~~- fili not yet supported; easy fix but i'm lazy~~
~~- allow customization of model size? (J.E.#1)~~
#### more functionality?
- voice commands?
    - maybe look for keyword in transcription hmm....
- subtitling?
    - might be possible, see .srt file format

-gdc

### J.E.'s list
1. Incorporate more advanced user input?
- make them have option to change whisper model? 

2. GUI / App interface must have the following:
-- set countdown timer/start button for recording
-- stop button/extend button? (voice command "stop"?)
-- area of transcripted text
-- Whisper Ai working checkmark?
-- Python version compatible checkmark?

3. Translation if u want
4. Get approved by Res tchr

5. Make efficient program
-- delete recordings per loop? delete button in GUI? will recordings be stored?
-- sound when start recording in GUI?
-- make code cleaner
-- make sure transcription of each clip is ASAP after recording each clip (the multiprocess join and stuff idk how it reaally works)
-- for problem/limitation 1, we can check if seconds are divisible by best # of seconds per clip OR start and stop button (IDK how to do without fr GUI). Ex. IF ODD seconds ==> duration per clip is odd # of seconds. ELSE, IF EVEN seconds ==> duration per clip is 2 seconds. 
-- limitation 5 and 1 can be remedied by having optimal seconds per clip. i think.

Porblems/Limitation of program so far:
1. Not for subtitling, but mainly for transcribing
-- when used for subtitling, it will have delayed subtitles due to not fast enough hardware and inefficient code/process (XP).
2. Will only transcribe in English and common foreign words unless specified language i think
3. "Words" "transcribed" during long silence (can be fixed but i did not look into it yet)
4. I don't know how to get rid of "The 'nopython' keyword argument was not supplied to the 'numba.jit' d...."
5. There may be Words not be caught between "Recording 0 Saved" and "Recording 1 Started"
-- maybe code is not efficient enough and/or not fast enough hardware  

- J.E.





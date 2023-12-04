
Hello my friends. 

# whisper transcriber software

## PATCH NOTES VER 4 (PYAUDIO VERSION)
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

### COMMENTS ON PATCH NOTES VER 4 (PYAUDIO VERSION)

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





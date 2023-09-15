
Hello my friends. 


PATCH NOTES VER 3
- improved recording timer function
- improved user input mechanics

You must have Whisper AI working first.
See this video.
https://www.youtube.com/watch?v=ABFqbY_rmEk&ab_channel=KevinStratvert

Also, this is my reference code.
https://github.com/JohnZolton/scribe

To complete program:
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





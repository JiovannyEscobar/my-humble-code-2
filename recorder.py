#import warnings
#from numba import NumbaDeprecationWarning
#warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
# This removes the NumbaDepWarning. The latest version of numba is still 57.1. 59 is not out yet, so i think this is 
# the best u can do. to remove it. its just in the log though, not in the gui

import os
import sounddevice as sd
import soundfile as sf
import whisper
import numpy as py
import multiprocessing
from multiprocessing import Process
import time
 


# Set the duration per clip
duration = 3  # Recording duration in seconds

# Set sampling freq for mic to record
sampling_frequency = 44100  # Sample rate (Hz)

# Create the "recordings" folder if it doesn't exist
folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "recordings")
os.makedirs(folder_path, exist_ok=True)

'''''
Program Flow
- create recordings folder
- inp() allows for user to input in secs how long to rec.
- record() opens mic; records in clips of 3 seconds or as set above
- transcribe() transcribes finished clips and writes transcribed text in transcript.txt 
'''''

start_time = time.time()
n = 0
m = 0
trans_arr = [0]
stp = 0

def inp(durnum_arr):

    # Length of operation in seconds
    durnum = int(input("How long are you going to record? "))
    durnum_arr[0] = durnum 
    trans_arr[0] = durnum

    print("Will record for " + str(durnum) + " seconds.")


def record(durnum_arr, trans_arr):
    
    # Delete previous recording files
    files = os.listdir(folder_path)
    for file in files:	
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Previous recordings deleted.")
    print("Will run for " + str(durnum_arr[0]) + " seconds" )  


    global n, stp

    #while time.time() - start_time < durnum_arr[0]:

    while stp < 5:

        stp+=1
        
        # Keep track of clips
        rd = round(time.time() - start_time)
        rectimes = "Recording started. " + str(rd)
        print(rectimes)
        
        # Record audio from the microphone
        recording = sd.rec(int(duration * sampling_frequency),
                        samplerate = sampling_frequency, channels=1)  # Mono recording

        # Wait for the recording to complete
        sd.wait()

        # Save the recording to a WAV file in the "recordings" folder
        filename = "recording" + str(n) + ".wav"

        output_file = os.path.join(folder_path, filename)
        sf.write(output_file, recording, sampling_frequency)

        print(f"Recording saved as {output_file}.")

        trans_arr[0] = n
        n = n + 1




    finalrd = round(time.time() - start_time)
    print ("Session Finished. Recorded for " + str(finalrd) + " seconds. ") # str(durnum) so its exact for user hehe even though its not the real thing i think hehe

def transcribe(trans_arr): 

    global m

    model = whisper.load_model("base")
    print ("Transcription On")

    while True:        
        #retrieve file
        getfile = "recordings/recording"+ str(m) + ".wav"
          
        print ("Transcribing " + str(m) + "...")

        #transcribe file whisper
        result = model.transcribe(getfile)

        #transcribe file as text
        with open("transcriptions/transcript.txt", "a", encoding="utf-8") as txt:
            txt.write(result["text"])
            txt.write("\n")      
            print ("Transcribed " + str(m) + " ------- " + result["text"] + " --------")
            
        
        if m == trans_arr[0]:
                print ("Transcription Complete. Transcribed recording " + str(m) + ". Final trans_arr is " + str(trans_arr[0]))
                exit()
        m = m + 1



     
                

#if __name__=='__main__':

    # For transcribe() to work until the last recording
    trans_arr = multiprocessing.Array("i", 1)

    # Timer in seconds for recording
    durnum_arr = multiprocessing.Array('i', 1) 
    
    p1 = multiprocessing.Process(target=record, args=(durnum_arr, trans_arr,))
    p2 = multiprocessing.Process(target=transcribe, args=(trans_arr,))
    
    inp(durnum_arr)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


#inp([0])
#record()
#transcribe([0])

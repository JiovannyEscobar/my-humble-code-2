# GUI - Made for the Whisper Transcription Desktop Research
# Written by Jiovanny Escobar

from main import *

import tkinter as tk

from threading import Thread, Event
from tkinterdnd2 import TkinterDnD, DND_FILES

m = 0

# COLOR CODES
lgray = "#202123"
dgray = "#343541"

outputBoxBg = '#343640'
panelBg = "#202123"

# FONTS
outputFont = 'Calibri'
outputFontSize = 14

# OTHER
modelOptions = ["Base", "Tiny", "Small", "Medium", "Large"]
langOptions = ["English", "Filipino"]


def ChangeRunButtonState(toStart: bool, activated: bool):
    if toStart:
        if activated:
            runButton.config(text="Start recording", command=start)
        else:
            runButton.config(text="Start recording", command=None)
    else:
        if activated:
            runButton.config(text="Stop recording", command=stop)
        else:
            runButton.config(text="Stop recording", command=None)

# CURRENTLY, GUI IS NON-FUNCTIONAL

# RUNNING THE PROCESS
ongoing = Event()
def start():
    modelSize = str(selModel.get())
    modelLang = str(selLang.get())
    print("Recording and transcription called\n    Model size:", modelSize, "\n    Language:", modelLang)


# STOPPING THE PROCESS
def stop():
    ongoing.clear()
    Recorder.isRecording.clear()
    print("GUI called for transcription and recording to stop")
    try:
        txtBox.delete("1.0", 'end')
        txtBox.insert("1.0", *open(Transcriber.transcriptPath).readlines())
        Transcriber.transcriptIsDone.clear()
    except:
        None


# WINDOW SETUP
root = TkinterDnD.Tk()
root.geometry("900x600")
root.configure(bg='gray')
root.title("Whisper AI Transcription")

# FRAMES
btnFrame = tk.Frame(root)
btnFrame.config(bg=lgray)
btnFrame.pack(fill="both", expand=False, side='left')

txtFrame = tk.Frame(root)
txtFrame.config(bg=dgray)
txtFrame.pack(fill="both", expand=True, side='right')

# OUTPUT BOX
txtBox = tk.Text(txtFrame, font=(outputFont, outputFontSize), width=40, height=10, bg=outputBoxBg, fg='white')
txtBox.place(relx=0.1, rely=0.2)
txtBox.pack(pady=50)

# PANEL
label = tk.Label(btnFrame, text="Speech Transcription App", bg=panelBg, fg='white')
label.pack(pady=12, padx=100)
label.config()

runButton = tk.Button(btnFrame, text="Start microphone", command= start, bg=panelBg, fg="white")
runButton.pack(padx=10, pady=12)

# future fix: change run button to stop button once input starts

# OUTPUTTING
def updateModel():
    updatemsg = "Model selected: "+selModel.get()
    print(updatemsg)
    modelLabel.config(text=updatemsg)


def updateLang():
    updatemsg = "Language selected: "+selLang.get()
    print(updatemsg)
    langLabel.config(text=updatemsg)


# MODEL SELECTION
selModel = tk.StringVar()
selModel.set("Small")

modelDropdown = tk.OptionMenu(btnFrame, selModel, *modelOptions)
modelDropdown.config(bg=panelBg, fg="white")
modelDropdown["menu"].config(bg=panelBg, fg="white")
modelDropdown.pack()

modelSelectButton = tk.Button(btnFrame, text="Set Model", command=updateModel, bg=panelBg, fg='white')
modelSelectButton.pack()

modelLabel = tk.Label(btnFrame, text="Model selected: "+selModel.get(), bg=panelBg, fg="white")
modelLabel.pack(padx=10, pady=14)

# LANGUAGE SELECTION
selLang = tk.StringVar()
selLang.set(langOptions[0])

langDropdown = tk.OptionMenu(btnFrame, selLang, *langOptions)
langDropdown.config(bg=panelBg, fg='white')
langDropdown["menu"].config(bg=panelBg, fg='white')
langDropdown.pack()

langSelectButton = tk.Button(btnFrame, text="Set Language", command=updateLang, bg=panelBg, fg='white')
langSelectButton.pack()

langLabel = tk.Label(btnFrame, text="Transcription language: "+selLang.get(), bg=panelBg, fg='white')
langLabel.pack(padx=10, pady=14)


root.mainloop()

raise SystemExit()
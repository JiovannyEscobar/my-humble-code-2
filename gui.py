# GUI - Made for the Whisper Transcription Desktop Research
# Written by Jiovanny Escobar

import tkinter as tk
from tkinter import messagebox

from main import *
from threading import Thread, Event

windowRunning = Event()


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
modelOptions = ["Base", "Tiny", "Small", "Medium", "Large", "Large (v2)", "Large (v3)"]
langOptions = ["English", "Filipino"]

# PROCESS FUNCTIONS
def ChangePanelState(toStart: bool, activated: bool):
    if toStart:
        if activated:
            runButton.config(text="Start recording", command=start)
            for child in btnFrame.winfo_children():
                child.configure(state='active')
        else:
            runButton.config(text="Stopping...", command=None)
            runButton.configure(state='disabled')
    else:
        if activated:
            runButton.config(text="Stop recording", command=stop)
            runButton.configure(state='active')
        else:
            runButton.config(text="Loading...", command=None)
            for child in btnFrame.winfo_children():
                child.configure(state='disabled')


def start():
    ChangePanelState(False, False)
    statusLabel.configure(text="Loading model...")

    if selLang.get() == "English":
        selLangStr = "en"
    else:
        selLangStr = ""
    if selModel.get() == "Large":
        selModelStr = "large"
    elif selModel.get() == "Large (v2)":
        selModelStr = "large-v2"
    elif selModel.get() == "Large (v3)":
        selModelStr = "large-v3"
    else:
        selModelStr = selModel.get().lower()
    
    if not Transcriber.IsModelLoaded(selModelStr, selLangStr):
        prompt = messagebox.askokcancel(title="Model not downloaded", message="Selected model " + selModelStr + " " \
                                           + selLangStr + "not found locally. Will now download model (requires a strong"+\
                                            " internet connection). Proceed?")
        if not prompt:
            ChangePanelState(True, True)
            statusLabel.configure(text="Transcription cancelled due to missing model. Ready for use")
            return
        statusLabel.configure(text="Downloading "+selModelStr+" "+selLangStr+" model. This might take a while")

    root.update()
    t = Thread(target=LiveTranscription, args=(selModelStr, selLangStr, False), daemon=True)
    t.start()

    flag = loadingFinished.wait()
    if flag:
        ChangePanelState(False,True)
        statusLabel.configure(text="Recording and transcribing...")
    t = Thread(target=ongoing, daemon=True)
    t.start()


def ongoing():
    linesDone = 0
    while True:
        with open(Transcriber.transcriptPath, "r") as txt:
            transcriptList = txt.readlines()
            lines = len(transcriptList)
            for x in range(lines):
                transcriptList[x] = transcriptList[x].strip()
        
        if not lines == linesDone:
            txtBox.insert("end", transcriptList[lines-1] + "\n")
            linesDone = lines
            txtBox.see("end")

        if done.is_set():
            with open(Transcriber.transcriptPath, "r") as txt:
                final = txt.readlines()
            for x in range(linesDone, len(final)):
                txtBox.insert("end", final[x]+"\n")
                txtBox.see("end")
            break
    return


def stop():
    statusLabel.configure(text="Stopping app; transcribing pending audio files. Please do not exit the app!")
    ChangePanelState(True, False)
    root.update()

    stopCalled.set()
    flag = done.wait()
    if flag:
        statusLabel.configure(text="Done! Ready for next use")
        ChangePanelState(True, True)
    return


# WINDOW SETUP
root = tk.Tk()
root.geometry("900x600")
root.configure(bg='gray')
root.title("Whisper AI Transcription - v0.5.1")

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

runButton = tk.Button(btnFrame, text="Start microphone", command=start, bg=panelBg, fg="white")
runButton.pack(padx=10, pady=12)

# MODEL SELECTION
selModel = tk.StringVar()
selModel.set("Small")

modelLabel = tk.Label(btnFrame, text="Model Size", bg=panelBg, fg="white")
modelLabel.pack(padx=10, pady=14)

modelDropdown = tk.OptionMenu(btnFrame, selModel, *modelOptions)
modelDropdown.config(bg=panelBg, fg="white")
modelDropdown["menu"].config(bg=panelBg, fg="white")
modelDropdown.pack()

def CheckModelUpdate(*args):
    print("Selected model:", selModel.get())
selModel.trace_add('write', CheckModelUpdate)

# LANGUAGE SELECTION
selLang = tk.StringVar()
selLang.set(langOptions[0])

langLabel = tk.Label(btnFrame, text="Language", bg=panelBg, fg='white')
langLabel.pack(padx=10, pady=14)

langDropdown = tk.OptionMenu(btnFrame, selLang, *langOptions)
langDropdown.config(bg=panelBg, fg='white')
langDropdown["menu"].config(bg=panelBg, fg='white')
langDropdown.pack()

# STATUS LABEL
statusLabel = tk.Label(btnFrame, text="Welcome! Please enjoy", wraplength=150, justify="center", bg=panelBg, fg='white')
statusLabel.pack(pady=50, padx=100)
statusLabel.config()

root.mainloop()
if not done.is_set():
    print("Unexpected close!")

# ONLY RUNS AFTER WINDOW CLOSE!
raise SystemExit()

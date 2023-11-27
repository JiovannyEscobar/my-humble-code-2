import tkinter as tk
import time
#from recorder import test

#import testarea
import recorder
import transcribe

from threading import Event


"""
Certainly! Here are three colors in hex code that would be visually appealing for a website:

Teal: #1CA2A8
Slate Gray: #6B6E70
Rose: #E85D75

Of course! For a more modern vibe, consider the following hex colors:

Pastel Blue: #A8DADC
Muted Coral: #FF6B6B
Soft Charcoal: #333644

chatgpt haha lol

#202123 dark left side
#343541 light right side
#343640 dark right side
#fae69e yellow in new
#fae69e green logo
"""

m = 0



    
    #else:
    #    i = 0
    #    setTextBox()

    
root = tk.Tk()
root.geometry("900x600")
root.configure(bg='gray')
root.title("GUI")



btnframe = tk.Frame(root)
btnframe.configure(bg="#202123")
btnframe.pack(fill="both", expand=False, side='left')

txtframe = tk.Frame(root)
txtframe.configure(bg="#343541")
txtframe.pack(fill="both", expand=True, side='right')



txtArea = tk.Text(txtframe, font=('Calibri', 14), width=40, height=10, bg='#343640', fg="white")
txtArea.place(relx=0.1, rely=0.2)
#txtArea.pack()


label = tk.Label(btnframe, text="Speech Transcription App", bg='#202123', fg="white")
print("set")
label.pack(pady=12, padx=100)
label.configure()

#button = tkinter.Button(master=frame, text="Test", command=lambda: inp([10])) # why its play before pressing button? lamba is fix :)
runButton = tk.Button(btnframe, text="Test", command=transcribe.setTextBox, bg='#202123', fg="white")
runButton.pack(pady=12, padx=10)


root.mainloop()
import tkinter as tk
import time
#from recorder import test

from testarea3 import *
import testarea


y = "Hello world"
c = 0

timestart = 0
curtime = 0
clix = 0

a = 0
n = 1.0

'''
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
'''

    
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


def test(txt):
    
    global n
    
    if n > 4:
        return
    testarea.count()
    a = float(txtArea.index('end-1c').split('.')[0])  # returns line count 2 
    print("Hello world!")
    txtArea.insert(n, bb)
    n+=1

def test2(txt):
    global n

    txtArea.insert(n, txt)

def test3():
    global bb

    testarea.count()
    test2(bb)
    time.sleep(1.0)

#button = tkinter.Button(master=frame, text="Test", command=lambda: inp([10])) # why its play before pressing button? lamba is fix :)
button = tk.Button(btnframe, text="Test", command=test3, bg='#202123', fg="white")
button.pack(pady=12, padx=10)




root.mainloop()


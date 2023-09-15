


def setTextBox(txt=None):
    global m, str_arr
    
    x = ""
    y = 0.0
    
    ran = 3
    i = 0

    while i < ran:
        y = float(txtArea.index('end')) + 1.0
        #x = testarea.count()
        recorder.transcribe([m])
        x = recorder.str_arr[m]
        x = str(x)
        txtArea.insert(y, x)
        root.after(0, setTextBox)
        m = m + 1
        i+=1
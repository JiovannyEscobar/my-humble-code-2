# Import the tkinter module
import tkinter

# Creating the GUI window.
window = tkinter.Tk()
window.title("Welcome to geeksforgeeks")
window.geometry("800x100")

# Creating our text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()

# Creating the function to set the text
# with the help of button
def set_text_by_button():

	# Delete is going to erase anything
	# in the range of 0 and end of file,
	# The respective range given here
	sample_text.delete(0,"end")
	
	# Insert method inserts the text at
	# specified position, Here it is the
	# beginning
	sample_text.insert(0.0, "Text set by button")

# Setting up the button, set_text_by_button()
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Set",
					command=set_text_by_button)

set_up_button.pack()

window.mainloop()

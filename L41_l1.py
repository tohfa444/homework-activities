from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("200x200")

def H_K(event):
    print(event.char)

window.bind("<Key>",H_K)

def H_C(event):
    print("\nThe button was clicked!")

button = Button(text = "Click me!")
button.pack()

button.bind("<Button-1>",H_C)

window.mainloop()
from tkinter import *
from PIL import ImageTk

signUp_window = Tk()
signUp_window.title("SignUp Page")
signUp_window.resizable(False, False)
background = ImageTk.PhotoImage(file="bg.jpg")
bgLabel = Label(signUp_window, image=background)
bgLabel.grid()


signUp_window.mainloop()

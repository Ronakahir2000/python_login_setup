from tkinter import *
from PIL import ImageTk

signUp_window = Tk()
signUp_window.title("SignUp Page")
signUp_window.resizable(False, False)
background = ImageTk.PhotoImage(file="bg.jpg")
bgLabel = Label(signUp_window, image=background)
bgLabel.grid()

frame = Frame(signUp_window)
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=(
    'times new roman', 23, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0)

signUp_window.mainloop()

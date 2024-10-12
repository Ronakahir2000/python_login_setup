from tkinter import *
from PIL import ImageTk

signUp_window = Tk()
signUp_window.title("SignUp Page")
signUp_window.resizable(False, False)
background = ImageTk.PhotoImage(file="bg.jpg")
bgLabel = Label(signUp_window, image=background)
bgLabel.grid()

frame = Frame(signUp_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=(
    'times new roman', 18, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

signUp_window.mainloop()

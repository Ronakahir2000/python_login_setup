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
    'Microsoft yahei UI light', 18, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=(
    'Microsoft yahei UI light', 10, 'bold'), bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=25, font=(
    'Microsoft yahei UI light', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

UsernameLabel = Label(frame, text='Username', font=(
    'Microsoft yahei UI light', 10, 'bold'), bg='white', fg='firebrick1')
UsernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

UsernameEntry = Entry(frame, width=25, font=(
    'Microsoft yahei UI light', 10, 'bold'), fg='white', bg='firebrick1')
UsernameEntry.grid(row=4, column=0, sticky='w', padx=25)

PasswordLabel = Label(frame, text='Password', font=(
    'Microsoft yahei UI light', 10, 'bold'), bg='white', fg='firebrick1')
PasswordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

PasswordEntry = Entry(frame, width=25, font=(
    'Microsoft yahei UI light', 10, 'bold'), fg='white', bg='firebrick1')
PasswordEntry.grid(row=6, column=0, sticky='w', padx=25)

ConfirmpasswordLabel = Label(frame, text='Confirm password', font=(
    'Microsoft yahei UI light', 10, 'bold'), bg='white', fg='firebrick1')
ConfirmpasswordLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

ConfirmpasswordEntry = Entry(frame, width=25, font=(
    'Microsoft yahei UI light', 10, 'bold'), fg='white', bg='firebrick1')
ConfirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=25)

Ckbutton = Checkbutton(frame, text="I agree to terms and conditions", font=(
    'Microsoft yahei UI light', 9, 'bold'), fg="firebrick1", bg='white', activebackground='white', activeforeground='firebrick1', cursor='hand2')
Ckbutton.grid(row=9, column=0, padx=15, pady=10)

Signupbutton = Button(frame, text='Signup', font=(
    'open sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17)
Signupbutton.grid(row=10, column=0, pady=10)

signUp_window.mainloop()

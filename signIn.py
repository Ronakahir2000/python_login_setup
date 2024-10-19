from tkinter import *
from PIL import ImageTk

# functionality


def on_click_user(event):
    if user_input.get() == "Username":
        user_input.delete(0, END)


def on_click_psw(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, END)


def hide():
    openEye.config(file='closeye.png')
    password_entry.config(show='*')
    openEyeButton.config(command=show)


def show():
    openEye.config(file='openeye.png')
    password_entry.config(show='')
    openEyeButton.config(command=hide)


# GUI part
login_window = Tk()
login_window.geometry('990x660+50+10')
login_window.resizable(0, 0)
login_window.title('Login page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')


bgLable = Label(login_window, image=bgImage)
bgLable.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=(
    'Microsoft yahei UI light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

user_input = Entry(login_window, width=25, font=(
    'Microsoft yahei UI light', 11, 'bold'), bd=0, fg='firebrick1')
user_input.place(x=580, y=200)

user_input.insert(0, "Username")

user_input.bind('<FocusIn>', on_click_user)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

password_entry = Entry(login_window, width=25, font=(
    'Microsoft yahei UI light', 11, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=580, y=260)

password_entry.insert(0, "Password")

password_entry.bind('<FocusIn>', on_click_psw)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

openEye = PhotoImage(file='openeye.png')
openEyeButton = Button(login_window, image=openEye,
                       bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
openEyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='forgot password?',
                      bd=0, bg='white', activebackground='white', cursor='hand2', font=(
                          'Microsoft yahei UI light', 11, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=705, y=295)

loginButton = Button(login_window, text="Login", font=(
    'open sans', 16, 'bold'), fg='white',
    bd=0, bg='firebrick1', activebackground='firebrick1', activeforeground='white', cursor='hand2', width='19')
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='-------------- OR -------------',
                font=('open Sans', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white', cursor='hand2')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='google.png')
gglLabel = Label(login_window, image=google_logo, bg='white', cursor='hand2')
gglLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo,
                     bg='white', cursor='hand2')
twitterLabel.place(x=740, y=440)

signUpLabel = Label(login_window, text="don't have an account?",
                    font=('open Sans', 9, 'bold'), fg='firebrick1', bg='white')
signUpLabel.place(x=590, y=500)

newAccountButton = Button(login_window, text="create new one", font=(
    'open sans', 9, 'bold', 'underline'), fg='blue', bg='white', activeforeground='blue', activebackground='white',
    cursor='hand2', bd=0)
newAccountButton.place(x=727, y=500)

login_window.mainloop()

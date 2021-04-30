
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import winsound
import sounds as mySounds 
 
# creating Tk window
root = tk.Tk()
  
# canvas dimensions
canvas = tk.Canvas(root, width = 600, height = 300)
canvas.pack() 

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Kayaba Pomodoro app")
  
# Declaration of variables

minute=StringVar()
second=StringVar()
  
# setting the default value as --

minute.set("--")
second.set("--")
  
# Use of Entry class to take input from the user

minuteEntry= Label(root, width=3, font=("Arial",25,""),
                   textvariable=minute)
minuteEntry.place(x=220,y=220)
  
secondEntry= Label(root, width=3, font=("Arial",25,""),
                   textvariable=second)
secondEntry.place(x=270,y=220)
  
  
def submit():

    Pomodoro_length.configure(text = "")
    try:
        # the input provided by the user is
        
        temp = int(Pomodoro_length.get())*60
        full = int(Break_length.get())*60 + temp
    except:
        print("Please input the right value")

    while full >-1:
         
        # divmod(firstvalue = full//60, secondvalue = full%60)
        mins,secs = divmod(full,60)
           
        # using format () method to store the value up to
        # two decimal places
        
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # full value every time
        root.update()
        time.sleep(1)

        if full == temp:
            mySounds.break_sound()
        # when full value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (full == 0):
            mySounds.play_song()
         
        # after every one sec the value of full will be decremented
        # by one
        full -= 1

# Diplay clock (extra)
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   clock.config(text=text_input)
   clock.after(200, digitalclock)

#Clock
clock = Label(root, font=("Courier", 12, 'bold'), fg="green", bd =10)
clock.place(relx= 1.0, rely = 0.01, anchor= 'ne') 
# button widget
btn = Button(root, text='Start Pomodoro', bd='5',
             command= submit)
btn.place(x = 230,y = 170)

#Title
canvas.create_text(300, 20, font="Times 16 bold", text="Welcome to Kayaba's pomodoro app!")
#Introduction
canvas.create_text(300, 50, font="Times 12", text="Enter the lenght of the pomodoro and the desired break time in minutes")

#Pomodoro lenght text
canvas.create_text(150, 90, font="Times 11", text="Enter the lenght of the pomodoro: ")
#P lenght input

Pomodoro_length = tk.Entry (root) 
canvas.create_window(350, 90, window=Pomodoro_length)

#Pomodoro break text
canvas.create_text(136, 140, font="Times 11", text="Enter the lenght of the break: ")
#B lenght input
Break_length = tk.Entry (root) 
canvas.create_window(350, 140, window=Break_length)




digitalclock()

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()
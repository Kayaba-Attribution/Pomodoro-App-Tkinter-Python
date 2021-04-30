import tkinter as tk
import datetime as dt
from tkinter import messagebox
from tkinter import simpledialog
import winsound
import time

root= tk.Tk()
root.title('Juan Pomodoro app')

def main_pomodoro(t_now, t_fut, t_fin, t_pom, delta_sec):
    total_pomodoros = 0
    while True:
        # Pomodoro time! Code for adding and maintaining the websites to be blocked!
        if t_now < t_fut:
            label1 = tk.Label(root, text= t_now)
            canvas1.create_window(200, 230, window=label1)
        elif t_fut <= t_now <= t_fin:
            # allow for browsing again. Remove websites from hosts file
            print('Break time!')
        #Pomodoro and break finished. Check if ready for another pomodoro!
        else:
            total_pomodoros += 1
            print('Pomodoro Finished!!')
            # Ring a bell (with print('\a') to alert of end of program.
            print('end')
            # Annoy!
            for i in range(10):
                winsound.Beep((i+100), 500)
            
            usr_ans = messagebox.askyesno("Pomodoro Finished!","Would you like to start another pomodoro?")
            #usr_ans = input("Timer has finished. \nWould you like to start another pomodoro? \nY/N:  ")

            if usr_ans == True:
                # user wants another pomodoro! Update values to indicate new timeset.
                t_now = dt.datetime.now()
                t_fut = t_now + dt.timedelta(0,t_pom)
                t_fin = t_now + dt.timedelta(0,t_pom+delta_sec)
                continue
            elif usr_ans == False:
                print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
                # unlock the websites
                # Show a final message)
                messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+
                "\nYou completed "+str(total_pomodoros)+" pomodoros today!")
                break
        # check every 3 seconds and update current time
        time.sleep(2)
        t_now = dt.datetime.now()
        timenow = t_now.strftime("%H:%M")

    
def start():
    user_start = entry1.get()
    p_length = Pomodoro_length.get()
    b_length = Break_length.get()

    if user_start == "y":
        # Collect time information
        t_now = dt.datetime.now()                       # Current time for reference.   [datetime object]
        t_pom = p_length*60                                   # Pomodoro time                 [int, seconds]
        t_delta = dt.timedelta(0,t_pom)                 # Time delta in mins            [datetime object]
        t_fut = t_now + t_delta                         # Future time for reference     [datetime object]
        delta_sec = b_length*60                                 # Break time, after pomodoro    [int, seconds]
        t_fin = t_now + dt.timedelta(0,t_pom+delta_sec) # Final time (w/ 5 mins break)  [datetime object]

        print(t_now)
        messagebox.showinfo("Pomodoro Started!", "\nIt is now "+t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")
        main_pomodoro(t_now, t_fut, t_fin, t_pom,delta_sec)
    elif user_start == "n":
        messagebox.showinfo("Juan pomodoro clock", "See you next time!")


canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.pack()

#Title
canvas1.create_text(300, 20, font="Times 16 bold", text="Welcome to juan's pomodoro app!")
#Introduction
canvas1.create_text(300, 50, font="Times 12", text="Enter the lenght of the pomodoro and the desired break time in minutes")

#Pomodoro lenght text
canvas1.create_text(150, 90, font="Times 11", text="Enter the lenght of the pomodoro: ")
#P lenght input
Pomodoro_length = tk.Entry (root) 
canvas1.create_window(350, 90, window=Pomodoro_length)

#Pomodoro break text
canvas1.create_text(136, 140, font="Times 11", text="Enter the lenght of the break: ")
#B lenght input
Break_length = tk.Entry (root) 
canvas1.create_window(350, 140, window=Break_length)


#answer = messagebox.askyesno(title='confirmation',message='Are you sure that you want to quit?')
Start_button = tk.Button(text='Start pomodoro', command=start)
canvas1.create_window(300, 220, window=Start_button)

root.mainloop()
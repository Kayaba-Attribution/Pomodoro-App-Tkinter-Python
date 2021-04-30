import tkinter as tk
import datetime as dt
from tkinter import messagebox
from tkinter import simpledialog
import winsound
import time

root = tk.Tk()
root.withdraw()

## Main script here:





# Main script
def main_pomodoro(t_now, t_fut, t_fin):
    total_pomodoros = 0
    while True:
        # Pomodoro time! Code for adding and maintaining the websites to be blocked!
        if t_now < t_fut:
            print(t_now)
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



user_start = messagebox.askyesno("Welcome to juan pomodoro clock","Would you like to start a pomodoro?")
if user_start == True:
    # Collect time information
    t_now = dt.datetime.now()                       # Current time for reference.   [datetime object]
    t_pom = 1*10                                   # Pomodoro time                 [int, seconds]
    t_delta = dt.timedelta(0,t_pom)                 # Time delta in mins            [datetime object]
    t_fut = t_now + t_delta                         # Future time for reference     [datetime object]
    delta_sec = 1*10                                 # Break time, after pomodoro    [int, seconds]
    t_fin = t_now + dt.timedelta(0,t_pom+delta_sec) # Final time (w/ 5 mins break)  [datetime object]

    print(t_now)
    messagebox.showinfo("Pomodoro Started!", "\nIt is now "+t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")
    main_pomodoro(t_now, t_fut, t_fin)
elif user_start == False:
    messagebox.showinfo("Juan pomodoro clock", "See you next time!")
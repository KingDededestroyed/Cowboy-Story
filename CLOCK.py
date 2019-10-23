import time
import calendar
from tkinter import*
from tkinter import ttk
from tkinter import font
import winsound

#------------------------------Actual Clock Stuff-------------------------#
alarmHour = input("Enter alarm hour: ")
alarmMinute = input("Enter alarm minute: ")
alarmSecond = input("Enter alarm second: ")


def beep():
    winsound.Beep(640,1000)
def current_time():
    
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds % 60

    totalMinutes = totalSeconds // 60
    currentMinute = totalMinutes % 60

    totalHour = totalMinutes // 60
    currentHour = (totalHour % 24) - 6

    if currentHour < 10:
        hourZero = "0"
    else:
        hourZero = ""
        
    if currentMinute < 10:
        minuteZero = "0"
    else:
        minuteZero = ""
        
    if currentSecond < 10:
        secondZero = "0"
    else:
        secondZero = ""

    if currentHour >= 12:
        amPm = "P.M."
        currentHour = currentHour - 12
        
    if currentHour < 12:
        amPm = "A.M."
        
    if currentHour == 0:
        currentHour = currentHour + 12

    a = (str.format("{0}{1}:{2}{3}:{4}{5} {6}",hourZero,\
                              alarmHour,minuteZero,alarmMinute,\
                              secondZero,alarmSecond,amPm))

    currentTime = (str.format("{0}{1}:{2}{3}:{4}{5} {6}",hourZero,\
                              currentHour,minuteZero,currentMinute,\
                              secondZero,currentSecond,amPm))
    if currentTime == a:
        beep()
    return currentTime

def show_time():
    time = current_time()
    txt.set(time)
    root.after(1000, show_time)

#-----------------------------Window Settings----------------------------#

root = Tk()

#Window Size
root.geometry("600x200")
root.configure(background = "Black")
root.title("Clock")

#Font
root.after(1000,show_time)
fnt = font.Font(family = "Times", size = 60, weight = "bold")
txt = StringVar()

lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "White",background = "Black")

lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()


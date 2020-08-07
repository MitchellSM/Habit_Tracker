from tkinter import *
from DataXMLHandeler import *

hh = habitParser("/home/mitchell/Desktop/HabitTracker/HabitData.xml")

window = Tk() # Create new window object
window.geometry('600x600')
window.title("Habit Tracker (v0.1)")

toplbl = Label(window, text="Date:")
toplbl.grid(column = 0, row = 0)

daylbl = Label(window, text="day (dd):")
daylbl.grid(column = 0, row = 1)
daytxt = Entry(window, width=2)
daytxt.grid(column = 1, row = 1)

monthlbl = Label(window, text="Month (mm):")
monthlbl.grid(column = 2, row = 1)
monthtxt = Entry(window, width=2)
monthtxt.grid(column = 3, row = 1)

yearlbl = Label(window, text="Year (yyyy):")
yearlbl.grid(column = 4, row = 1)
yeartxt = Entry(window, width=4)
yeartxt.grid(column = 5, row = 1)

txtList = list()


selected = StringVar()
selected.set("DEFAULT")

def selectedDay():
    txtList[0].focus()

rad1 = Radiobutton(window,text='MON', value="MONDAY", variable=selected, command=selectedDay)
rad2 = Radiobutton(window,text='TUE', value="TUESDAY", variable=selected, command=selectedDay) 
rad3 = Radiobutton(window,text='WED', value="WEDNESDAY", variable=selected, command=selectedDay)
rad4 = Radiobutton(window,text='THU', value="THURSDAY", variable=selected, command=selectedDay)
rad5 = Radiobutton(window,text='FRI', value="FRIDAY", variable=selected, command=selectedDay)
rad6 = Radiobutton(window,text='SAT', value="SATURDAY", variable=selected, command=selectedDay)
rad7 = Radiobutton(window,text='SUN', value="SUNDAY", variable=selected, command=selectedDay)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
rad4.grid(column=3, row=2)
rad5.grid(column=4, row=2)
rad6.grid(column=5, row=2)
rad7.grid(column=6, row=2)

txt = Entry(window, width=10)
txtList.append(txt)
txt.grid(column=0, row=3)

def newdataclicked():
    newtxt = Entry(window, width=10)
    txtops = txtList[-1].grid_info()
    newtxt.grid(column= txtops['column'], row = txtops['row']+1)

    txtList.append(newtxt)
    
    savebtnops = save_data_btn.grid_info()
    save_data_btn.grid(column=savebtnops['column'], row=savebtnops['row']+1)
    newtxt.focus()
    pass

def submit():
    date = daytxt.get()+"-"+monthtxt.get()+"-"+yeartxt.get()
    day = selected.get()
    timelist = list()
    for txt in txtList:
        time = txt.get()
        if not time == "":
            if len(time) < 4:
                time = "0" + time
            timelist.append(time)
        txt.delete(0, len(txt.get()))
    hh.writeToDay(date, timelist, day)
    daytxt.delete(0, len(daytxt.get()))
    daytxt.focus()

daytxt.focus()

new_data_btn = Button(window, text="+", command=newdataclicked)
save_data_btn = Button(window, text="SAVE", command=submit)

new_data_btn.grid(column=1, row=3)
save_data_btn.grid(column=1, row=4)

window.mainloop()
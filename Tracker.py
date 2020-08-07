"""
Graphical Interface for Habit Tracking application. 
Allows user to input habitual data which can then be submitted and saved to an XML,
    using a custom XML parser. 

Author: Mitchell Sulz-Martin
Date: 24-02-2020
Version: 1.0
"""

from DataXMLHandeler import * 
from tkinter import *


class Application:
    """ Habit Tracker Interface and Data Handeling """
    def __init__(self, filename, title, size='600x600'):
        self.parser = habitParser(filename)
        self.window = Tk()
        
        self.daytxt, self.monthtxt, self.yeartxt = None, None, None
        self.txtlist = list()

        self.selected = StringVar()
        self.selected.set("DEFAULT")
        self.additionEntry = None
        self._run(title, size)


    def _windowInit(self, title, size):
        """ Initialize window geometry and metadata """
        self.window.geometry(size)
        self.window.title(title)
        return 

    def _topLabelsInit(self):
        """ Initialize the static top level labels """
        toplbl = Label(self.window, text="Date:")
        toplbl.grid(column = 0, row = 0)

        daylbl = Label(self.window, text="day (dd):")
        daylbl.grid(column = 0, row = 1)
        daytxt = Entry(self.window, width=2)
        daytxt.grid(column = 1, row = 1)

        monthlbl = Label(self.window, text="Month (mm):")
        monthlbl.grid(column = 2, row = 1)
        monthtxt = Entry(self.window, width=2)
        monthtxt.grid(column = 3, row = 1)

        yearlbl = Label(self.window, text="Year (yyyy):")
        yearlbl.grid(column = 4, row = 1)
        yeartxt = Entry(self.window, width=4)
        yeartxt.grid(column = 5, row = 1)
        return daytxt, monthtxt, yeartxt
    
    def _selectedDay(self):
        """ Forces focus on first textbox after day selection """
        self.txtlist[0].focus()

    def _radioBtnInit(self):
        """ Initialize day selection radio buttons """
        DisplayNames = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
        radlist = list()
        for d in Day:
            if d == Day.DEFAULT:
                continue
            r = Radiobutton(self.window, text=DisplayNames[d.value-1], value=d.name, variable=self.selected, command=self._selectedDay)
            r.grid(column=d.value, row=2)
            radlist.append(r)
        return 
    
    def newdataclicked(self):
        """ Creates n new Entry objects and reconfigures window with new additions"""
        for i in range(int(self.additionEntry.get())):
            newtxt = Entry(self.window, width=10)
            txtops = self.txtlist[-1].grid_info()
            newtxt.grid(column= txtops['column'], row = txtops['row']+1)
            self.txtlist.append(newtxt)
        self.additionEntry.delete(0, len(self.additionEntry.get()))
        self.additionEntry.insert(END, "1")
        self.txtlist[-1].focus()
        return 
        
    def submit(self):
        """ Data handeler """
        date = "-".join([self.daytxt.get(), self.monthtxt.get(), self.yeartxt.get()])
        day = self.selected.get()
        timelist = list()
        for txt in self.txtlist:
            time = txt.get()
            if not time == "":
                if len(time) < 4:
                    time = "0".join([time])
                timelist.append(time)
            txt.delete(0, len(txt.get()))
        self.parser.writeToDay(date, timelist, day)
        self.daytxt.delete(0, len(self.daytxt.get()))
        self.daytxt.focus()
        return
        
    def _othersInit(self):
        """ Initialize the remaining window objects and functionality """ 
        self.txtlist.append(Entry(self.window, width=10))
        self.txtlist[0].grid(column=0, row=3)
        
        newdatabtn = Button(self.window, text="+", command=self.newdataclicked)
        savedatabtn = Button(self.window, text="SAVE", command=self.submit)
        self.additionEntry = Entry(self.window, width=10)
        self.additionEntry.insert(END, "1")
        self.additionEntry.grid(column=2, row=3)
        newdatabtn.grid(column=1, row=3)
        savedatabtn.grid(column=1, row=4)
        return 
        
    def _run(self, title, size):
        """ Run method """ 
        self._windowInit(title, size)
        self.daytxt, self.monthtxt, self.yeartxt = self._topLabelsInit()
        self._radioBtnInit() 
        self._othersInit()
        self.daytxt.focus()
        self.window.mainloop()

def main():
    filename = "/home/mitchell/Desktop/HabitTracker/HabitData.xml"
    app = Application(filename, "Habit Tracker (v1.0)", '600x600')

if __name__ == "__main__":
    main()

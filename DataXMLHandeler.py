"""
XML File I/O for DailyDataHandeler
"""

from xml.etree import ElementTree as ET
from enum import Enum


class Day(Enum):
    DEFAULT = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class habitParser():
    def __init__(self, filename):
        self.filename = filename
        self.tree = ET.ElementTree(file=filename)
        self.root = self.tree.getroot()
        
    
    def getAllSmokeTimes(self):
        """ Returns a list containing all smoketimes across entire document """
        times = list()
        for daydata in self.root.findall("dayData"):
            for timesets in daydata:
                for smokes in timesets.findall('time'):
                    times.append(smokes.text)
        return times
    
    def getDayTimes(self, day):
        """ Given a specific day from Day, read and return times as a list from xml """
        times = list()
        for daydata in self.root.findall("dayData"):
            if daydata.attrib['day'] == day:
                for timesets in daydata:
                    for smokes in timesets.findall('time'):
                        times.append(smokes.text)
        return times

    def getAllDayTimes(self):
        """ Generates a dictionary with Day enum as key and list as value """
        alldays = dict()
        for days in Day:
            if not days == Day.DEFAULT:
                alldays[days] = self.getDayTimes(days.name)
        return alldays

    def checkExistingDate(self, date):
        """ Searches Document to find an exisiting date """
        for daydate in self.root.findall("dayData"):
            if daydate.attrib['date'] == date:
                return True, daydate.attrib['day']
        return False, Day.DEFAULT

    def getExistingDay(self, date):
        """ Searches Document to find an exisiting date """
        for daydate in self.root.findall("dayData"):
            if daydate.attrib['date'] == date:
                return daydate
        return None

    def writeToDay(self, date, dataStream=None, day=Day.DEFAULT.name):
        """ Finds corresponding date element and appends the dataStream """
        element = self.getExistingDay(date)
        
        if not element == None:
            timeset = element.find('smokes')
            for newEntry in dataStream:
                smoketime = ET.SubElement(timeset, 'time')
                smoketime.text = newEntry
        else:
            print(date)
            self.writeDayStruct(date, day)
            self.writeToDay(date, dataStream)

        self.tree.write(self.filename,xml_declaration=True, method="xml")
        return 

    def writeDayStruct(self, date, day=Day.DEFAULT.name):
        """ If no date matches the desired, create an empty shell"""
        attrib = {"date": date, "day": day}
        daydata = ET.SubElement(self.root, 'dayData', attrib)
        daydata.tail = "\n"
        # Level 2 children
        smokes = ET.SubElement(daydata, 'smokes', {})
        meals = ET.SubElement(daydata, "meals", {})
        drinks = ET.SubElement(daydata, "drinks", {})
        others = ET.SubElement(daydata, "others", {})

        return None

def main():
    x = habitParser("/home/mitchell/Desktop/HabitTracker/HabitData.xml")
    print(x.getAllDayTimes())
    return

if __name__ == "__main__":
    main()




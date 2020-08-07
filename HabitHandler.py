"""
Interface and input processing
"""
from DataXMLHandeler import habitParser, Day
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

class Histogram:
    def __init__(self, numOfBuckets=None, keySet=None):
        self.numberofbuckets = numOfBuckets
        self.histogram = self.createEmpty(numOfBuckets, keySet)
        

    def createEmpty(self, bucketCount, keySet=None):
        """ Creates an empty Histogram """
        if not keySet is None:
            histogram = dict()
            for key in keySet:
                if not key == Day.DEFAULT:
                    subhistogram = Histogram()
                    histogram[key] = subhistogram.populateEmpty()  
        else:
            histogram = self.populateEmpty() 
        return histogram

    def populateEmpty(self, bucketCount=24):
        histogram = dict()
        for key in range(bucketCount):
            histogram[key] = 0      
        return histogram

    def printHistogram(self):
        """ Prints the histogram"""
        strOut = ""
        for key in self.histogram:
            strOut += str(key.name) + ": " + str(self.histogram[key]) + " |\n"
        print(strOut)

    def histogramize(self, dataDictionary):
        """ Receives a dictionary as input and writes converts dictionary into a histogram"""
        """ eg. {MONDAY: [...], ... , SUNDAY: [...]} """
        for dayKeys in dataDictionary.keys():
            for value in dataDictionary[dayKeys]:
                self.writeToHistogram(dayKeys, value)

    def writeToHistogram(self, key, value):
        """ Increases count of the {key, value} pair"""
        subKey = self.findClosestBucket(value)
        subhist = self.histogram[key]
        subhist[subKey] += 1
        return 

    def findClosestBucket(self, data):
        """ Finds the closest bucket to hour given """
        bucketKeys = [x for x in range(24)]
        hour = int(data[:2])
        if hour in bucketKeys:
            return bucketKeys[hour]

    def plotHistogram(self):
        plt.show()  

class DataHandler:
    def __init__(self, file=None):
        self.histogram = Histogram(7, Day)
        self.parser = habitParser(file)
        self.filename = file

    def getXMLdata(self):
        """ Parses XML file and pulls smoking data"""
        xmlData = self.parser.getAllDayTimes()
        self.histogram.histogramize(xmlData)
        return 
    
    def getData(self):
        """ Gets time data from user for all days"""
        for day in Day:
            if not day == Day.DEFAULT:
                self.processInput(day)
        return
    
    def getDataWithKey(self, key):
        """ Gets Time data from user for a specific day """
        if key == Day.DEFAULT:
            key = self.daySelection()
        return key, self.processInput(key)
    
    def processInput(self, key):
        values = list()
        while True:
            item = input(key + " Enter time (4-digit): ")
            if item == "":
                break
            if len(item) < 4:
                    item = "0" + item
            values.append(item)
        return values
    
    def daySelection(self):
        inputstr = input("1: Monday\n2: Tuesday\n3: Wednesday\n4: Thursday\n5: Friday\n6: Saturday\n7: Sunday\nSelect Day:")
        return Day(int(inputstr))

    def printData(self):
        self.histogram.printHistogram()
        #self.histogram.plotHistogram()
        return 

    def interface(self):
        while(True):
            print("Habit Tracker v0.1\n")
            option = input("1: Input new data to XML.\n2: View current histogram\n3: Exit\nEnter one of the options above: ")
            if option == "1":
                self.newDataInput()
            elif option == "2":
                self.getXMLdata()
                self.printData()
            else:
                self.exitProgram()
        return

    def newDataInput(self, date=None):
        if data == None:
            print("Please enter the date you would like to record.")
            date = self.getDate()
        exists, day = verifyDate(date)
        if exists:
            # NOTE need to add some time checking to ensure entries are duped
            print("This day has been recorded already")
            daykey, values = self.getDataWithKey(day)
            self.parser.writeToDay(date, values, daykey)
        else:
            daykey, values = self.getDataWithKey(day)
            self.parser.writeDayStruct(date, daykey.name)
            self.parser.writeToDay(date, values)
            
        return

    def verifyDate(self, date):
        return self.parser.checkExistingDate(date)

    
    def getDate(self):
        day = input("Enter two-digit day: ")
        month = input("Enter two-digit month: ")
        year = input("Enter four-digit year: ")
        return day+"-"+month+"-"+year

    def exitProgram(self):
        print("Goodbye!")
        exit(0)


def main():
    # h = DataHandler("/home/mitchell/Desktop/HabitTracker/HabitData.xml")
    # h.interface()
    pass
    
if __name__ == "__main__":
    main()
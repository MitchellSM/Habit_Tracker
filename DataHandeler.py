""" 
Interface for smoking data
Mitchell Sulz-Martin
01/30/2020
"""

import xml.etree.ElementTree as ET
from enum import Enum
from DataXMLHandeler import habitParser, Day



class Date:
    def __init__(self, day= None, month=None, year=None):
        self.__day = self.setDay(day)
        self.__month = self.setMonth(month)
        self.__year = self.setYear(year)

    def setDay(self, d):
        self.__day = d
    
    def getDay(self):
        return self.__day
    
    def setMonth(self, m):
        self.__month = m
    
    def getMonth(self):
        return self.__month
    
    def setYear(self, y):
        self.__year = y
    
    def getYear(self):
        return self.__year
    
    def printDate(self):
        dateString = "Date: " + self.getDay() + "-" + self.getMonth() + "-" + self.getYear() + ".\n"
        print(dateString)

class Histogram:
    def __init__(self, numOfBuckets=None, keySet=None):
        self.numberofbuckets = numOfBuckets
        self.histogram = self.createEmpty(numOfBuckets, keySet)
        pass

    def printHistogram(self):
        """ Prints the histogram"""
        strOut = ""
        for key in self.histogram:
            strOut += str(key) + ": " + str(self.histogram[key]) + " |\n"
        print(strOut)
        

    def increaseCount(self, dataKey):
        """ increases count of corresponding item bucket """
        if dataKey in self.histogram:
            self.histogram[dataKey] += 1
        else:
            return False
        return True

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

    def get(self, key):
        return self.histogram[key]

    def histogramize(self, dataList):
        for dayDict in dataList:
            for dayKey in Day:
                if not dayKey == Day.DEFAULT:
                    for vals in dayDict[dayKey]:
                        self.writeHistogramData(dayKey, vals)
    
    def writeHistogramData(self, key, dataItem):
        subKey = self.findClosestBucket(dataItem)
        subhist = self.histogram.get(key)
        subhist[subKey] += 1
        return 





    def writeHistogramToFile(self):
        """ File I/O for writing a histogram to a file """
        file = open(self.filename, "a")
        for day in self.histogram.histogram.keys():
            file.write(day.name + "\n")
            for item in self.histogram.histogram[day]:
                # print()
                file.write(str(item) + ": " + str(self.histogram.histogram[day][item]) + "\n")
            file.write("\n\n")
        file.close()

        return

    def readHistogramFromFile(self, file):
        """ Reads histogram data from a file """

        return 
    
    
            
        
    def analyzeData(fileName):
        """ Runs an analysis on read data """
        pass


def main():
    h = DataHandler("test.txt")
    h.getDataWithKey()
    h.histogram.printHistogram()
    # h.writeHistogramToFile()
    
if __name__ == "__main__":
    main()
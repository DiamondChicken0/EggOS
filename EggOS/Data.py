from datetime import time, date, datetime
from re import T
import time
tempList = []
def main():
    tempSent = True
    weatherSent = True
    weatherRequest = True
    weather = "none"
    averageTemps = []
    weatherList = []
    tempRequest = True
    averageTemp = 60
    tempTotal = 0
    test = 10
    #loop to keep the code running you have to type in a value for initial temp fist then weather
    while 1 == 1:
        #if you type in 0 you get to input a temperature
        if test == 0:
            tempSent = True
        #if you type in 1 it shows the code to display temps
        if test == 1:
            tempRequest = True
        #if you type in 2 you get to input a weather
        if test == 2:
            weatherSent = True
        # if you type in a 3 you get to view the current weather
        if test == 3:
            weatherRequest = True
        #adds current temp to daily temp list
        if tempSent:
            tempList.append(input())
            tempSent = False
            #inputs current weather to program
        if weatherSent:
            weather = input()
            weatherSent = False
        if weatherRequest:
            print("Current Weather", weather)
            weatherRequest = False
        if tempRequest:
            #code to display current temp
            tempTotal = 0
            print("Current Temp",tempList[-1])
            for temp in tempList:
                tempTotal = int(temp) + int(tempTotal)
                averageTemp = tempTotal/len(tempList)
                print("Average Temp", averageTemp)
            tempRequest = False 
            #should reset temperatures and add average to running list at midnight
        if '00:00' == datetime.now().strftime('%H:%M'):
            for temp in tempList:
                tempTotal = int(temp) + int(tempTotal)
                averageTemp = tempTotal/len(tempList)
                print("Average Temp", averageTemp)
            averageTemps.append(averageTemp)
            weatherList.append(weather)
            tempList.clear()
        test = int(input())
            
        
main()
    
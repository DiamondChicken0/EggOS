from datetime import datetime
def main():
    tempSent = True
    time = (0, 0, 0, 1)
    averages= [[][]]
    tempRequest = True
    averageTemp = 60
    tempTotal = 0
    tempList = []
    while 1 == 1:
        if tempSent:
            tempList.append(input())
            tempSent = False
        if tempRequest:
            tempTotal = 0
            print(tempList[-1])
            for temp in tempList:
                tempTotal += temp
            averageTemp = tempTotal/len(tempList)
            print(averageTemp)
        if (t)
    
main()
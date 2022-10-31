import calendar
from cmath import rect
from datetime import datetime
from multiprocessing.connection import wait
from random import randint

import sys
import threading
from time import sleep
import pygame as py
import Data
from pygame.locals import *

# just a lot of declaration, images have a lot of variables to mess with
py.init()

dataThread = threading.Thread(target = Data.main)
dataThread.start()

rng = randint(0,2)
print(rng)
if rng == 0:
    chickenCondtion = "happy"
elif rng == 1:
    chickenCondtion = "meh"
elif rng == 2:
    chickenCondtion = "angry"

clock = py.time.Clock()
screen = py.display.set_mode((1280, 720))
py.display.set_caption("EggOS")
screen.fill("WHITE")
running = True

background = py.Rect((0, 0), (1280, 720))
py.draw.rect(screen, (255, 255, 255), background)

grassBackground = py.image.load("grass.jpg")
grassBackground = py.transform.scale(grassBackground, (1280, 720))
screen.blit(grassBackground, (0, 0))

gaggleChicken = py.image.load("gaggleofchickens.png")
gaggleChicken = py.transform.scale(gaggleChicken, (420, 325))
screen.blit(gaggleChicken, (440, 100))

titleFont = py.font.SysFont("Bahnschrift", 100, bold=True)
EggOStxt = py.image.load("EggOS logo.png")
screen.blit(EggOStxt, (470, 410))

X = 440
Y = 100

py.display.update()
py.event.get()
py.time.wait(3000)

# animates the chicken on startup
while (X > -550):

    py.event.get()

    screen.blit(grassBackground, (0, 0))
    X = X - 10
    Y = Y - 0.1

    screen.blit(gaggleChicken, (X, Y))
    screen.blit(EggOStxt, (470, 410))
    py.display.update()
    clock.tick(60)

mainMenu = True
time = datetime.now()
currentSeason = 'winter'

# checks the month and assigns a season so the background is seasonal

if time.month >= 3 and time.month <= 5:
    seasonBackground = py.image.load("spring.jpg")
    season = "spring"

elif time.month >= 6 and time.month <= 8:
    seasonBackground = py.image.load("summer.jpg")
    season = "summer"

# if you are wondering, why the name leaffall.jpg?
# the original names were autumn and fall
# but it kept recognizing \a and \f as escape characters and wouldnt read the file name
# just accept it

elif time.month >= 9 and time.month <= 11:
    seasonBackground = py.image.load("leaffall.jpg")
    season = "fall"

else:
    seasonBackground = py.image.load("winter.jpg")
    season = "winter"

seasonBackground = py.transform.scale(seasonBackground, (1280, 720))

calendarBackground = py.image.load("Calendar.png")

currentMonth = calendar.month_name[time.month]
monthFont = py.font.SysFont("Aharoni", 100, bold=True)
calendarMonthText = monthFont.render(currentMonth, 1, (0, 0, 0))

uiBar = py.image.load("UI Bar.png")

titleFont = py.font.SysFont("Bahnschrift", 100, bold=True)
EggOStxt = titleFont.render("EggOS", 1, (247, 255, 82))
screen.blit(EggOStxt, (470, 410))

timeFont = py.font.SysFont("Franklin Gothic", 90)
currentTimeReadout = time.strftime("%H:%M:%S")
currentTime = timeFont.render(currentTimeReadout, 1, (0, 0, 0))
screen.blit(currentTime, (0, 0))

dateFont = py.font.SysFont("Arial", 70)

inUse = False
selectedMonth = int(time.month)
labelFont = py.font.SysFont("Bahnschrift", 20)

def fixWeekends(org):
    org = org + 1
    if org >= 7:
        return 0
    return org

class Day:
    def __init__(self):
        self.day = -1
        self.temperature = -1
        self.weather = -1
        self.weekday = -1
        self.calendarText = labelFont.render("Test", 1, (0,0,0))

    def change(self, d,t,w):
        self.day = d
        self.temperature = t
        self.weather = w
        self.weekday = calendar.weekday(time.year,selectedMonth, self.day)
        self.weekday = fixWeekends(self.weekday)
        self.calendarText = labelFont.render(f"{self.day}", 1, (0,0,0))
        self.calendarTextTemperature = labelFont.render(f"{self.temperature}° F", 1, (0,0,0))
        self.calendarTextSun = labelFont.render(f"{self.weather}", 1, (0,0,0))

day0, day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15, day16, day17, day18, day19, day20, day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31, day32, day33, day34, day35, day36, day37, day38, day39, day40, day41 = Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day(),Day()

listOfDays = [day0, day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15, day16, day17, day18, day19, day20, day21, day22, day23, day24, day25, day26, day27, day28, day29, day30, day31, day32, day33, day34, day35, day36, day37, day38, day39, day40, day41]

# this is a function just so it can be called when new data is gained and to update the screen
def updateMenu(rotation, CC):
    chickenCondition = CC
    py.event.get()
    time = datetime.now()
    currentTimeReadout = time.strftime("%I:%M:%S %p")
    currentTime = timeFont.render(currentTimeReadout, 1, (0, 0, 0))


    chicken = py.image.load("chicken.png")
    chicken = py.transform.flip(chicken, True, False)
    chicken = py.transform.scale(chicken, (700, 500))
    newChicken = py.transform.rotate(chicken, rotation)
    if (randint(0, 20) == 2):
        if rotation > 0:
            rotation = rotation - 5
        elif rotation < 20:
            rotation = rotation + 5

    currentMonthReadout = time.strftime("%m")
    currentMonth1 = dateFont.render(currentMonthReadout, 1, (0, 0, 0))
    currentDayReadout = time.strftime("%d")
    currentDay = dateFont.render(currentDayReadout, 1, (0, 0, 0))

    screen.blit(seasonBackground, (0, 0))
    screen.blit(calendarBackground, (0, 115))
    screen.blit(calendarMonthText, (250, 135))
    screen.blit(uiBar, (20, 4))
    screen.blit(currentTime, (190, 30))
    screen.blit(currentMonth1, (620, 1))
    screen.blit(currentDay, (705, 40))
    screen.blit(newChicken, (800, 350))

    thoughtBubble = py.image.load("thinking.png")
    thoughtBubble = py.transform.scale(thoughtBubble, (400,400))

    if chickenCondition == "happy":
        emote = py.image.load("happy_face.png")
    elif chickenCondition == "meh":
        emote = py.image.load("meh_spiral.png")
    else:
        emote = py.image.load("angry_face2.png")

    emote = py.transform.scale(emote, (200,200))

    screen.blit(thoughtBubble, (875,0))

    noOfDays = calendar.monthrange(2022, selectedMonth)[1]
    week = 0
    Data.generateData(season)
    for i in range(1, noOfDays+1):
        calendar.firstweekday
        weatherList = Data.pullWeather()
        tempList = Data.pullTemps()
        listOfDays[i-1].change(i,tempList[i],weatherList[i])
        screen.blit(listOfDays[i-1].calendarText, ((115*((listOfDays[i-1].weekday)%7))+10,250+(week * 75)))
        screen.blit(listOfDays[i-1].calendarTextTemperature, ((115*((listOfDays[i-1].weekday)%7))+10,270+(week * 75)))
        screen.blit(listOfDays[i-1].calendarTextSun, ((115*((listOfDays[i-1].weekday)%7))+10,290+(week * 75)))
        environmentPercent = 0

        #this metric is based of personal expirience
        if listOfDays[i-1].temperature >= 60 and listOfDays[i-1].temperature <= 80:
            environmentPercent = environmentPercent + 50
        elif listOfDays[i-1].temperature >= 50 and listOfDays[i-1].temperature <= 90:
            environmentPercent = environmentPercent + 25
        if listOfDays[i-1].weather == "Sunny":
            environmentPercent = environmentPercent + 50
        elif listOfDays[i-1].weather == "Clear":
            environmentPercent = environmentPercent + 30
        elif listOfDays[i-1].weather == "Cloudy":
            environmentPercent = environmentPercent + 30
        elif listOfDays[i-1].weather == "Foggy":
            environmentPercent = environmentPercent + 10

        if environmentPercent >= 65:
            image = py.image.load("happy_thumbsup.png")
            
        elif environmentPercent <= 35:
            image = py.image.load("angry_face.png")
            
        else:
            image = py.image.load("meh_face.png")
            
        image = py.transform.scale(image,(30,30))
        screen.blit(image, ((115*((listOfDays[i-1].weekday)%7))+60,255+(week * 75)))
        screen.blit(emote, (975,40))

        if listOfDays[i-1].weekday == 6:
            week = week + 1


    py.display.update()
    return rotation


chickenRotation = 0
chickenRotation = updateMenu(chickenRotation,chickenCondtion)

while running == True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    chickenRotation = updateMenu(chickenRotation, chickenCondtion)

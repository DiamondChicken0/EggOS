import calendar
from cmath import rect
from datetime import datetime
from multiprocessing.connection import wait
from random import randint
from sqlite3 import Time
import sys
import threading
from time import sleep
import pygame as py

from pygame.locals import *

# just a lot of declaration, images have a lot of variables to mess with
py.init()

chickenCondition = "happy"

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

elif time.month >= 6 and time.month <= 8:
    seasonBackground = py.image.load("summer.jpg")

# if you are wondering, why the name leaffall.jpg?
# the original names were autumn and fall
# but it kept recognizing \a and \f as escape characters and wouldnt read the file name
# just accept it

elif time.month >= 9 and time.month <= 11:
    seasonBackground = py.image.load("leaffall.jpg")

else:
    seasonBackground = py.image.load("winter.jpg")

seasonBackground = py.transform.scale(seasonBackground, (1280, 720))

calendarBackground = py.image.load("Calendar.png")

currentMonth = calendar.month_name[time.month]
monthFont = py.font.SysFont("Aharoni", 100, bold=True)
calendarMonthText = monthFont.render(currentMonth, 1, (0, 0, 0))

uiBar = py.image.load("UI Bar.png")

titleFont = py.font.SysFont("Bahnschrift", 100, bold=True)
EggOStxt = titleFont.render("EggOS", 1, (247, 255, 82))
screen.blit(EggOStxt, (470, 410))

timeFont = py.font.SysFont("Arial", 90)
currentTimeReadout = time.strftime("%H:%M:%S")
currentTime = timeFont.render(currentTimeReadout, 1, (0, 0, 0))
screen.blit(currentTime, (0, 0))

dateFont = py.font.SysFont("Arial", 70)

inUse = False
selectedMonth = int(time.month)
# this is a function just so it can be called when new data is gained and to update the screen
def updateMenu(rotation, newImage):
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
    screen.blit(currentTime, (160, 6))
    screen.blit(currentMonth1, (620, 1))
    screen.blit(currentDay, (705, 40))
    screen.blit(newChicken, (800, 350))

    firstDayOfTheWeek = calendar.weekday(time.year, selectedMonth, 1)
    print(firstDayOfTheWeek)

    


    thoughtBubble = py.image.load("thinking.png")
    thoughtBubble = py.transform.scale(thoughtBubble, (400,400))

    if chickenCondition == "happy":
        emote = py.image.load("happy_face.png")
    elif chickenCondition == "meh":
        emote = py.image.load("meh_spiral.png")
    elif chickenCondition == "angry":
        emote = py.image.load("angry_face2.png")
    else:
        emote = py.image.load("egg,png")

    emote = py.transform.scale(emote, (200,200))

    screen.blit(thoughtBubble, (875,0))
    screen.blit(emote, (975,40))

    py.display.update()
    return rotation


chickenRotation = 0
chickenRotation = updateMenu(chickenRotation, False)

while running == True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    chickenRotation = updateMenu(chickenRotation, False)

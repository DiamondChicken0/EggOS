import calendar
from cmath import rect
from datetime import datetime
from multiprocessing.connection import wait
from sqlite3 import Time
import sys
from time import sleep
import pygame as py

from pygame.locals import *

# just a lot of declaration, images have a lot of variables to mess with
py.init()

clock = py.time.Clock()
screen = py.display.set_mode((1280,720))
py.display.set_caption("EggOS")
screen.fill("WHITE")
running = True

background = py.Rect((0,0), (1280,720))
py.draw.rect(screen, (255,255,255), background)

grassBackground = py.image.load("EggOS Assets\grass.jpg")
grassBackground = py.transform.scale(grassBackground, (1280,720))
screen.blit(grassBackground, (0,0))

gaggleChicken = py.image.load("EggOS Assets\gaggleofchickens.png")
gaggleChicken = py.transform.scale(gaggleChicken, (420,325))
screen.blit(gaggleChicken, (440,100))

titleFont = py.font.SysFont("Bahnschrift", 100, bold= True)
EggOStxt = titleFont.render("EggOS", 1, (247, 255, 82))
screen.blit(EggOStxt, (470,410))

X = 440
Y = 100

py.display.update()
py.event.get()
py.time.wait(3000)

#animates the chicken on startup
while (X > -550):

    py.event.get()
    
    screen.blit(grassBackground,(0,0))
    X = X - 10
    Y = Y - 0.1
    
    screen.blit(gaggleChicken, (X,Y))
    screen.blit(EggOStxt, (470,410))
    py.display.update()
    clock.tick(60)

mainMenu = True
today = datetime.now()
currentSeason = 'winter'

# checks the month and assigns a season so the background is seasonal

if today.month >= 3 and today.month <= 5:
    seasonBackground = py.image.load("EggOS Assets\spring.jpg")

elif today.month >= 6 and today.month <= 8:
    seasonBackground = py.image.load("EggOS Assets\summer.jpg")

# if you are wondering, why the name leaffall.jpg? 
# the original names were autumn and fall
# but it kept recognizing \a and \f as escape characters and wouldnt read the file name
# just accept it

elif today.month >= 9 and today.month <= 11:
    seasonBackground = py.image.load("EggOS Assets\leaffall.jpg")

else:
    seasonBackground = py.image.load("EggOS Assets\winter.jpg")

seasonBackground = py.transform.scale(seasonBackground, (1280,720))
screen.blit(seasonBackground, (0,0))

calendarBackground = py.image.load("EggOS Assets\Calendar.png")

currentMonth = calendar.month_name[today.month]
monthFont = py.font.SysFont("Aharoni", 100, bold= True)
calendarMonthText = monthFont.render(currentMonth, 1, (0,0,0))
screen.blit(calendarMonthText, (0,0))


# this is a function just so it can be called when new data is gained
running = True
def updateMenu():
       py.event.get()
       screen.blit(seasonBackground, (0,0))
       screen.blit(calendarBackground, (0,115))
       screen.blit(calendarMonthText, (250,135))
       py.display.update()
       py.time.delay(1000)

updateMenu()

while running == True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
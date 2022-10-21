from cmath import rect
from sre_parse import WHITESPACE
from time import sleep
import pygame as py

from pygame.locals import *

py.init()

screen = py.display.set_mode((800,600))
py.display.set_caption("EggOS")
screen.fill("WHITE")
running = True

background = py.Rect((0,0), (800,600))
py.draw.rect(screen, (255,255,255), background)

gaggleChicken = py.image.load("EggOS\EggOS Assets\gaggleofchickens.png")
gaggleChicken = py.transform.scale(gaggleChicken, (250,200))
screen.blit(gaggleChicken, (275,125))

titleFont = py.font.SysFont("Bahnschrift", 100, bold= True)
EggOStxt = titleFont.render("EggOS", 1, (247, 255, 82))
screen.blit(EggOStxt, (225,310))

X = 275
Y = 125

py.display.update()
sleep(3)

ascension = False
while (X > -400):
    py.draw.rect(screen, (255,255,255), background)
    X = X - 2
    Y = Y - 0.1
    

    print(str(X) + ", " + str(Y))
    
    sleep(0.01)
    screen.blit(gaggleChicken, (X,Y))
    screen.blit(EggOStxt, (225,310))
    py.display.update()






while running:

    for event in py.event.get():
        print(event)
        if event.type == py.QUIT:
            running = False


    py.display.update()

py.quit()

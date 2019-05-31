import pygame
from display import *

sprites = [pygame.image.load('images/idle.png'),
           pygame.image.load('images/runing01.png'),
           pygame.image.load('images/runing02.png')]

width = 45
height = 60
x = (Canvas.width/2) - (width/2)
y = 400+2-height

class Player:
    xspeed = 5
    yspeed = 5


    def jump(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
            print('jump')


    def show(self):
        for f in range(len(sprites)):
            Canvas.display.blit(sprites[0], (x, y))
            # pygame.display.update()

import pygame
from display import *

sprites = [pygame.image.load('images/idle.png'),
           pygame.image.load('images/runing01.png'),
           pygame.image.load('images/runing02.png')]


class Player:

    def __init__(self):
        self.xspeed = 5
        self.width = 45
        self.height = 60
        self.y = 400+2-self.height-2
        self.x = (Canvas.width/2) - (self.width/2)
        self.on_ground = True
        self.yspeed = 2
        self.sup_limit = 200
        self.inf_limit = 400+2-self.height-2
        self.accel = 0.1
        print('iinit')

    # @staticmethod
    def jump(self):

        if self.on_ground == True:
            self.yspeed *= -1
            self.on_ground = False

        if self.y < self.sup_limit:
            self.yspeed *= -1

        elif self.y >= self.inf_limit:
            self.on_ground = True
            self.yspeed = 0

        if self.y <= self.inf_limit:
            self.y -= self.yspeed + -self.accel

        return self.y

    def show(self):
        for f in range(len(sprites)):
            Canvas.display.blit(sprites[0], (self.x, self.y))
            # pygame.display.update()

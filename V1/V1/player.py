import pygame
from display import *

sprites = [pygame.image.load('images/idle.png'),
        pygame.image.load('images/runing01.png'),
        pygame.image.load('images/runing02.png')]

sprites_rotated = [pygame.image.load('images/idle_rotated.png'),
        pygame.image.load('images/runing01_rotated.png'),
        pygame.image.load('images/runing02_rotated.png')]

jumping = [pygame.image.load('images/jumping_rotated.png'),
        pygame.image.load('images/jumping.png')]

class Player:
    # play_y = 400
    def __init__(self):

        self.xspeed = 5
        self.width = 45
        self.height = 60
        self.x = (Canvas.width/2) - (self.width/2)
        self.y = 350
        self.on_ground = True
        self.yspeed = 2
        self.sup_limit = 200
        self.inf_limit = 400+2-self.height-2
        self.accel = 0.1
        print("ALOU")

    def jump(self, py):

        if self.on_ground == True:
            self.yspeed *= -1
            self.on_ground = False

        else:
            if py < self.sup_limit:
                print()
                self.yspeed *= -1

            elif py >= self.inf_limit:
                self.on_ground = True
                pyspeed = 0

            if py <= self.inf_limit:
                py -= self.yspeed + -self.accel

        return py

    def show(self, a, rotated=False, jump=False):
        a = int(a)

        if jump == True:
            if rotated == True:
                Canvas.display.blit(jumping[0], (self.x, 0))
            else:
                Canvas.display.blit(jumping[1], (self.x, 0))

        else:
            if rotated == True:
                Canvas.display.blit(sprites_rotated[a], (self.x, self.y))
            else:
                Canvas.display.blit(sprites[a], (self.x, self.y))

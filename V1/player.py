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
    play_y = 400
    def __init__(self):
        self.xspeed = 5
        self.width = 45
        self.height = 60
        self.x = (Canvas.width/2) - (self.width/2)
        self.on_ground = True
        self.yspeed = 2
        self.sup_limit = 200
        self.inf_limit = 400+2-self.height-2
        self.accel = 0.1
        print("ALOU")

    def jump(self):

        if self.on_ground == True:
            self.yspeed *= -1
            self.on_ground = False

        '''if play_y < self.sup_limit:
            self.yspeed *= -1

        elif play_y >= self.inf_limit:
            self.on_ground = True
            self.yspeed = 0

        if play_y <= self.inf_limit:
            play_y -= self.yspeed + -self.accel

        return play_y'''

    def show(self, a, rotated=False, jump=False):
        a = int(a)

        if jump == True:
            if rotated == True:
                Canvas.display.blit(jumping[0], (self.x, 0))
            else:
                Canvas.display.blit(jumping[1], (self.x, 0))

        else:
            if rotated == True:
                Canvas.display.blit(sprites_rotated[a], (self.x, Player.play_y))
            else:
                Canvas.display.blit(sprites[a], (self.x,  Player.play_y))

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
    def __init__(self):
        self.width  = 45
        self.height = 60
        self.x = int((Canvas.width/2) - (self.width/2))
        self.y = int(400-self.height)
        self.sup_limit = 150
        self.inf_limit = 400-self.height

        self.speed_animation = 0.15
        self.on_ground = True
        self.rotated = False
        self.frame  = 0

        self.xspeed = 5
        self.yspeed = 7
        self.accel  = 0

    def jump(self):
        # print('player.y = ', self.y)
        if self.y < self.sup_limit:
            self.yspeed *= -1

        elif self.y > self.inf_limit:
            self.y = self.inf_limit
            self.on_ground = True
            self.yspeed *= -1

        self.y -= self.yspeed
        # self.yspeed += self.accel
        return self.y


    def show(self, frame, rotated=False, jump=False):
        frame = int(frame)

        if jump != True:
            if rotated == True:
                Canvas.display.blit(jumping[0], (self.x, self.y))
            else:
                Canvas.display.blit(jumping[1], (self.x, self.y))
        else:
            if rotated == True:
                Canvas.display.blit(sprites_rotated[frame], (self.x, self.y))
            else:
                Canvas.display.blit(sprites[frame], (self.x, self.y))

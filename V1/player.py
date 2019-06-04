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
        self.xspeed = 50
        self.width = 45
        self.height = 60
        self.x = (Canvas.width/2) - (self.width/2)
        self.y = int(400-self.height)
        self.on_ground = True
        self.yspeed = 2
        self.sup_limit = 200
        self.inf_limit = 400-self.height
        self.accel = 0.1
        print("ALOU")

    def jump(self):
        print('player.y = ', self.y)
        print()

        if self.on_ground == True:
            print('pullow')
            self.on_ground = False
        else:
            print('nao pulou')
            if self.y <= self.sup_limit:
                print('passou para cima')
            elif self.y >= self.inf_limit:
                print('passou para baixo')
                self.on_ground = True

        while self.y > 0:
            self.y -= self.yspeed
            return self.y


    def show(self, frame, rotated=False, jump=False):
        frame = int(frame)

        if jump == True:
            if rotated == True:
                Canvas.display.blit(jumping[0], (self.x, self.y))
            else:
                Canvas.display.blit(jumping[1], (self.x, self.y))

        else:
            if rotated == True:
                Canvas.display.blit(sprites_rotated[frame], (self.x, self.y))
            else:
                Canvas.display.blit(sprites[frame], (self.x, self.y))

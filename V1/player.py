import pygame
from display import *

# load sprite frames to the animation
sprites = [pygame.image.load('images/idle.png'),
        pygame.image.load('images/runing01.png'),
        pygame.image.load('images/runing02.png')]

sprites_rotated = [pygame.image.load('images/idle_rotated.png'),
        pygame.image.load('images/runing01_rotated.png'),
        pygame.image.load('images/runing02_rotated.png')]

jumping = [pygame.image.load('images/jumping_rotated.png'),
        pygame.image.load('images/jumping.png')]


class Player:
    # initializes player variables
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
        self.yspeed = 5
        self.accel  = 0

    # makes player jump
    def jump(self):
        # print('player.y = ', self.y)
        if self.y < self.sup_limit:
            self.yspeed *= -1

        elif self.y > self.inf_limit:
            self.y = self.inf_limit
            self.on_ground = True
            self.yspeed *= -1

        self.y -= self.yspeed
        # print(self.inf_limit)
        # self.yspeed += self.accel
        return self.y

    # detect if player is in collision with anything
    def collision(self, bkgd, obj):
        # holes hit boxes
        for i in range(len(obj.holes)):
            ohx1 = obj.holes[i][0]
            ohx2 = obj.holes[i][1]
            bx = abs(bkgd.x)

            if ohx1 <= bx and bx < ohx2:
                self.inf_limit = bkgd.height + 200
                return self.inf_limit
            else:
                self.inf_limit = 400-self.height

            if self.on_ground == True and self.y < self.inf_limit:
                self.y += self.yspeed
                return self.y

        # bloco especial
        for b in range(0, len(obj.special_block)):
            spx = obj.special_block[-b][0]
            spy = obj.special_block[-b][1]
            spw = 30
            sph = 30

            # no eixo - X
            if spx < self.x and self.x < spx + spw or spx < self.x + self.width and self.x + self.width < spx + spw:
                # no eixo - Y
                if spy < self.y and self.y < spy + sph:
                    obj.special_block.pop(-b)

        # block padrao
        for c in range(0, len(obj.brick_block)):
            bpx = obj.brick_block[-c][0]
            bpy = obj.brick_block[-c][1]
            bpw = 30
            bph = 30

            # no eixo - X
            if bpx < self.x and self.x < bpx + bpw or bpx < self.x + self.width and self.x + self.width < bpx + bpw:
                # no eixo - Y
                if bpy < self.y and self.y < bpy + bph:
                    obj.brick_block.pop(-c)

    # function that handle the frames animation of player
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

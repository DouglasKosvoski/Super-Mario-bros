import pygame
from display import *

# load sprite frames for the animation
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
        self.jump_height = 120
        self.inf_limit = 400-self.height                        # where the player will stand
        self.sup_limit = self.inf_limit - self.jump_height      # how high can player jump

        self.speed_animation = 0.15
        self.on_ground = True           # player starts on the ground
        self.rotated = False            # player is facing right
        self.frame  = 0
        self.facing_wall = False

        self.xspeed = 5
        self.yspeed = 8
        self.accel  = -0.5

    # makes player jump
    def jump(self):
        if self.y < self.sup_limit:
            self.yspeed *= -1

        elif self.y > self.inf_limit:
            self.y = int(407-self.height)
            self.on_ground = True
            self.yspeed = 8

        self.y -= self.yspeed
        self.yspeed += self.accel
        return self.y

    # detect if player is in collision with anything
    def collision(self, bkgd, obj):
        # standart brick
        for c in range(0, len(obj.brick_block)):
            bpx = obj.brick_block[-c][0]
            bpy = obj.brick_block[-c][1]
            bpw, bph = 30, 30

            # no eixo - X
            if bpx < self.x and self.x < bpx + bpw or bpx < self.x + self.width and self.x + self.width < bpx + bpw:
                if self.y < bpy:
                    self.inf_limit = bpy
                    self.y = bpy - self.height - 1
                    self.on_ground = True

                # no eixo - Y
                if bpy < self.y and self.y < bpy + bph: # player is in the same y as the block
                    obj.brick_block.pop(-c)             # delete collected block
                    obj.qtd_blocks -= 1                 # remove one from remaing blocks to collect

    # function that handle the frames animation of player
    def show(self, frame, rotated=False, jump=False):
        frame = int(frame)

        # basically checks is player is running, standing still, jumping, facing directions etc
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

    # check if player completed the level
    def win(self, bkgd):
        if bkgd.x < -3430:
            return True
        return False

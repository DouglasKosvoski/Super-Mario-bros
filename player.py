import pygame
from display import *

# load sprite frames for the player animation
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
        # image dimensions
        self.width  = 76
        self.height = 64
        # start pos on the screen
        self.x = int((Canvas.width/2) - (self.width/2))
        self.y = int(Canvas.height/1.116) - self.height

        # xspeed is constant... yspeed will be modified when jumping
        self.xspeed = 8
        self.yspeed = 20
        # force that will bring player back to the ground
        self.gravity  = -1
        # set 'where is the ground' for player to stand
        self.inf_limit = 600 - self.height

        # variables of player sprite controls
        self.on_ground = True
        self.rotated = False
        self.facing_wall = False
        self.speed_animation = 0.18
        self.frame  = 0


    # player jump
    def jump(self):
        # if player is under the ground
        if self.y > self.inf_limit:
            # realocate player Y-axi
            self.y = int(600-self.height-self.yspeed)
            # tell the player to keep stand
            self.on_ground = True
            # redefine speed due to gravity influence
            self.yspeed = 20

        # player goes up
        self.y -= self.yspeed
        # add gravity to Y-axi
        self.yspeed += self.gravity


    # detect if player is in collision with anything
    def collision(self, bkgd, obj):
        # for each block in matrix hitbox
        for c in range(0, len(obj.brick_block)):
            bpx = obj.brick_block[-c][0]
            bpy = obj.brick_block[-c][1]
            # block dimensions
            bpw, bph = 45, 45

            # detect if player is in the same X
                # left player corner
            if (bpx < self.x and self.x < bpx + bpw or
                # right player corner
                bpx < self.x + self.width and self.x + self.width < bpx + bpw or
                # if center if in the same X but corners are outside
                self.x < bpx and self.x + self.width > bpx + bpw):

                # detect if player is in the same Y
                if bpy < self.y and self.y < bpy + bph:
                    # if it is delete item from matrix
                    obj.brick_block.pop(-c)
                    # remove one from remaing blocks to collect
                    obj.qtd_blocks -= 1


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
        if bkgd.x < -5145:
            return True
        return False

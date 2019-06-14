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
        self.jump_height = 100
        self.inf_limit = 400-self.height
        self.sup_limit = self.inf_limit - self.jump_height

        self.speed_animation = 0.15
        self.on_ground = True
        self.rotated = False
        self.frame  = 0
        self.last_key = ''
        self.facing_wall = False
        # self.mid_air = False

        self.xspeed = 5
        self.yspeed = 8
        self.accel  = 0

    # makes player jump
    def jump(self):
        # print('player.y = ', self.y)
        if self.y < self.sup_limit:
            self.yspeed *= -1

        elif self.y > self.inf_limit:
            self.y = int(400-self.height) + 7
            self.on_ground = True
            self.yspeed *= -1

        self.y -= self.yspeed
        # self.yspeed += self.accel
        return self.y

    # detect if player is in collision with anything
    def collision(self, bkgd, obj):
        # bloco especial
        for b in range(0, len(obj.special_block)):
            spx = obj.special_block[-b][0]
            spy = obj.special_block[-b][1]
            spw = 30
            sph = 30

            # no eixo - X
            if spx < self.x and self.x < spx + spw or spx < self.x + self.width and self.x + self.width < spx + spw:
                if self.y < spy:
                    # self.mid_air = True
                    self.inf_limit = spy
                    # self.sup_limit = self.inf_limit - self.jump_height
                    self.y = spy - self.height - 1
                    self.on_ground = True
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
                if self.y < bpy:
                    # self.mid_air = True
                    self.inf_limit = bpy
                    self.y = bpy - self.height - 1
                    self.on_ground = True

                # no eixo - Y
                if bpy < self.y and self.y < bpy + bph:
                    obj.brick_block.pop(-c)


        # pipe
        for d in range(len(obj.pipe)):
            px = int(self.x) + obj.pipe[d][0]
            py = obj.pipe[d][1]
            pw = 60
            ph = 300

            pygame.draw.rect(Canvas.display, (120,240,120), [px, py,pw,ph])


            if px < self.x and self.x < px + pw or px < self.x + self.width and self.x + self.width < px + pw:
                if self.y + self.height -30 < py:
                    self.inf_limit = py
                    self.sup_limit = self.inf_limit - self.jump_height
                    self.y = py - self.height - 1
                    self.on_ground = True
                    self.facing_wall = False

                else:
                    if self.last_key == 'right':
                        bkgd.x = -obj.pipe_copy[d][0] + self.width + 5
                    else: # if last_key == `left`
                        bkgd.x = -obj.pipe_copy[d][0] - pw - 5

                    self.facing_wall = True

        self.inf_limit = int(400-self.height) + 7

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

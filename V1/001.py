import pygame, time, math, random, sys
from pygame.locals import *

background = pygame.Surface((640, 400))
background.fill((30, 90, 120))

W, H = 640, 400
HW, HH = W / 2, H / 2
AREA = W * H
FPS = 60
bg_x = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))


class Mario():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # isJump and jumpCount should be attributes of Mario.
        self.isJump = False
        self.jumpCount = 10

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 40, 40))

    def move(self):
        global bg_x
        if pressed_keys[K_RIGHT] and bg_x > -920:
            if self.x > 490:
                bg_x -= 5
            else:
                self.x += 5
        if pressed_keys[K_LEFT] and self.x > 5:
            self.x -= 5

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10


mario = Mario(50, 270)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start to jump by setting isJump to True.
                mario.isJump = True

    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (bg_x,0))
    mario.move()
    mario.draw()
    mario.jump()
    pygame.display.update()

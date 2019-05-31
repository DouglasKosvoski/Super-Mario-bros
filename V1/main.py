import pygame
from player import *
from event import *
from display import *


bkgd = Canvas()
play = Player()
ev = Event()

while True:
    bkgd.show()
    bkgd.move()
    play.show()
    play.jump()
    ev.check_event()


    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

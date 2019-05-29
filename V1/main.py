import pygame
from event import *
from display import *

bkgd = Canvas()
ev = Event()
play = Player()

while True:
    bkgd.show()
    bkgd.move()
    ev.check_event()


    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

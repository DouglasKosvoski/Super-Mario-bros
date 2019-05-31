import pygame, player
import event, display


bkgd = display.Canvas()
play = player.Player()
ev = event.Event()

while True:
    bkgd.show()
    # play.show()
    ev.check_event()
    # play.jump()
    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

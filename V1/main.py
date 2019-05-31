import pygame, player, event, display


bkgd = display.Canvas()
play = player.Player()
ev = event.Event()

while True:

    bkgd.show()
    ev.check_event()
    
    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

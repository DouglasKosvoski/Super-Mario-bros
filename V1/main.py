import pygame
import player, event, display


play = player.Player()
bkgd = display.Canvas(play)
ev = event.Event()

while True:

    bkgd.show(play)
    ev.check_event(play, bkgd)
    print(play.y)

    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

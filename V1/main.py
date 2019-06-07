import pygame
import player, event, display, hit_boxes


play = player.Player()
bkgd = display.Canvas(play)
ev = event.Event()
blocks = hit_boxes.HitBox()

while True:

    bkgd.show(play)
    ev.check_event(play, bkgd, blocks)
    play.collision(bkgd, blocks)
    blocks.show(bkgd)

    bkgd.time.tick(bkgd.fps)
    pygame.display.update()

import pygame
import player, event, display, hit_boxes    # import files

pygame.font.init()                          # initializes internal fonts

# create objects
ev = event.Event()
play = player.Player()
bkgd = display.Canvas(play)
coins = hit_boxes.HitBox()

# game loop
while True:
    bkgd.show(play)                                             # draw the background
    ev.check_event(play, bkgd, coins)                           # check for user input
    play.collision(bkgd, coins)                                 # check if player is within any hitbox
    coins.show(bkgd)                                            # draw the coins
    play.win(bkgd, coins)

    bkgd.time.tick(bkgd.fps)                                    # cap frames at a certain variable
    pygame.display.update()                                     # update the screen each frame

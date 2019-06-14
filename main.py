import pygame, time
import player, event, display, hit_boxes    # import files
import display_msg as msg   # import function from file

pygame.font.init()  # initializes internal fonts

# create objects
ev = event.Event()
play = player.Player()
bkgd = display.Canvas(play)
blocks = hit_boxes.HitBox()

# game loop
while True:
    bkgd.show(play)                         # draw the background
    ev.check_event(play, bkgd, blocks)      # check for user input
    play.collision(bkgd, blocks)            # check if player is within any hitbox
    blocks.show(bkgd)                       # draw the blocks


    if play.win(bkgd) == True:                      # is player is in the end of the level
        if blocks.qtd_blocks < 1:                   # if it collected all blocks
            msg.message_display('You Win!', bkgd)   # show message
            time.sleep(2)                           # freeze the screen for 2 seconds
            pygame.quit()                           # exit the game
        else:                                       # if player didn't collect all
            bkgd.x = -3430
            msg.message_display('Not Yet!', bkgd)   # display a warning
            time.sleep(0.5)                         # freeze for half a second
    else:
        msg.message_display('%d' % (blocks.qtd_blocks), bkgd)   # display how many blocks left
    bkgd.time.tick(bkgd.fps)                                    # cap frames at a certain variable
    pygame.display.update()                                     # update the screen each frame

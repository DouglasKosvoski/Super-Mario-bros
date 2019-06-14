import pygame


class Event():
    def __init__(self):
        pygame.key.set_repeat(1,1)


    def check_event(self, player, bkgd, hit_boxes):
        for event in pygame.event.get():
            # check is 'close' buttom was clicked
            if event.type == pygame.QUIT:
                # closes the game
                pygame.quit()
                quit()

            # if any key is pressed
            elif event.type == pygame.KEYDOWN:
                # if key pressed is ESCAPE quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                # if key pressed is SPACE or UP ARROW makes player jump
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    # since player is jumping
                    player.on_ground = False
                    player.show(0, player.rotated, jump=player.on_ground)


        # key 'a' or LEFT ARROW
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if bkgd.x < bkgd.left_limit:
                hit_boxes.move_left(bkgd)

                # moves background to right
                bkgd.x += bkgd.speed
                # rotate player to face left direction
                player.rotated = True
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)

        # key 'd' or RIGHT ARROW
        elif pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if bkgd.x > bkgd.right_limit:
                hit_boxes.move_right(bkgd)

                # moves background to left
                bkgd.x -= bkgd.speed
                # rotate player to normal position (right)
                player.rotated = False
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)
        else:
            # show player as idle position but rotation matters
            player.show(0, player.rotated, jump=player.on_ground)

        # increase frame var to change sprite image
        player.frame += player.speed_animation


        # go up and down and return True when is on ground
        if player.on_ground == False:
            player.jump()

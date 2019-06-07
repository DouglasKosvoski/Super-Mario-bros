import pygame


class Event():
    def __init__(self):
        pygame.key.set_repeat(1,1)


    def check_event(self, player, bkgd, hit_boxes):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if any key is pressed
            elif event.type == pygame.KEYDOWN:
                # if key pressed is ESCAPE quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                # if jey pressed is SPACE or UP ARROW makes player jump
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.on_ground = False
                    player.show(0, player.rotated, jump=player.on_ground)


        # key 'a' or LEFT ARROW
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if bkgd.x < bkgd.left_limit:
                # moves background to right
                bkgd.x += bkgd.speed
                # rotate player to face left direction
                player.rotated = True
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)
                hit_boxes.move_left(bkgd)

        # key 'd' or RIGHT ARROW
        elif pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if bkgd.x > bkgd.right_limit:
                # moves background to left
                bkgd.x -= bkgd.speed
                # rotate player to normal position (right)
                player.rotated = False
                player.show(player.frame % 2, player.rotated, jump=player.on_ground)
                hit_boxes.move_right(bkgd)
        else:
            # show player as idle position but rotation matters
            player.show(0, player.rotated, jump=player.on_ground)

        # increase frame var to change sprite image
        player.frame += player.speed_animation



        # go up and down and return True when is on ground
        if player.on_ground != True:
            player.jump()

import pygame


class Event():
    def __init__(self):
        pygame.key.set_repeat(1,1)

    def check_event(self, player, py):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump(py)

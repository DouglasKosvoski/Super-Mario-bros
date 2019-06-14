import pygame

class Canvas():
    width  = 600
    height = 450
    display = pygame.display.set_mode((width, height))

    def __init__(self, player):
        self.image = pygame.image.load('images/world.png')
        self.time  = pygame.time.Clock()
        self.fps = 60
        self.speed = player.xspeed

        self.x = 0
        self.y = 0
        self.left_limit  = 0
        self.right_limit = -6120

    def show(self, player):
        # display title and fps
        self.caption = pygame.display.set_caption('Super Mario Bros - %.1f' % (self.time.get_fps()))
        # draw the background
        self.display.blit(self.image, (self.x, self.y))
        # x and y are changed on event.py

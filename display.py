import pygame

class Canvas():
    # screen dimensions (resolution)
    width  = 900
    height = 670
    # create the screen
    display = pygame.display.set_mode((width, height))

    def __init__(self, player):
        # load image backgroud
        self.image = pygame.image.load('images/world.png')
        # define internal clock
        self.time  = pygame.time.Clock()
        # move the background in the velocity as the player
        self.speed = player.xspeed
        # define how many updates per second
        self.fps   = 60

        # initial pos for the background (will be changed a lot)
        self.x = 0
        self.y = 0
        # how much left can player go
        self.left_limit  = 0
        # how much right can the player go
        # is negative cause the bkgd moves in the oposite direction
        self.right_limit = -5175

    def show(self, player):
        # display title and fps
        self.caption = pygame.display.set_caption('Super Mario Bros - %.1f' % (self.time.get_fps()))
        # draw the background
        self.display.blit(self.image, (self.x, self.y))
        # x and y are changed on event.py

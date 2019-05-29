import pygame

class Player:
    def __init___(self):
        self.image = pygame.image.load('world.png')
        self.width = 30
        self.height = 30
        self.x = 300
        self.y = 400
        # self.left_limit = 0
        # self.right_limit = -6180 # background image width
        self.speed = 10

    def show(self):
        self.display.blit(self.image, (self.x, self.y))

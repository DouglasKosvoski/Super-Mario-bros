import pygame
import player

class Canvas():
    def __init__(self):
        self.time = pygame.time.Clock()
        self.fps = 60
        self.width = 600
        self.height = 450
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption('Super Mario Bros - Douglas Kosvoski')
        self.image = pygame.image.load('world.png')
        self.x = 0
        self.y = 0
        self.left_limit = 0
        self.right_limit = -6180 # background image width
        self.speed = player.Player.speed


    def show(self):
        self.display.blit(self.image, (self.x, self.y))

    def move(self):
        if pygame.key.get_pressed()[pygame.K_d]:
            if self.x > self.right_limit:
                self.x -= self.speed

        elif pygame.key.get_pressed()[pygame.K_a]:
            if self.x < self.left_limit:
                self.x += self.speed

        return self.x

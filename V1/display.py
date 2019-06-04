import pygame

class Canvas():
    width = 600
    height = 450
    display = pygame.display.set_mode((width, height))

    def __init__(self, player):
        self.time = pygame.time.Clock()
        self.fps = 600
        self.image = pygame.image.load('images/world.png')
        self.x = 0
        self.y = 0
        self.left_limit = 0
        self.right_limit = -6120
        self.speed = player.xspeed
        self.var = 0     # which frame will be displayed
        self.rot = False # rotation
        self.jum = False # jumping
        self.anim_speed = 0.15

    def show(self, player):
        self.caption = pygame.display.set_caption('Super Mario Bros - %.1f' % (self.time.get_fps()))
        self.display.blit(self.image, (self.x, self.y))

        if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]:
            self.jum = True
            player.show(0, self.rot, jump=self.jum)

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self.x > self.right_limit:
                self.x -= self.speed
                self.rot = False
                player.show(self.var % 2, self.rot, jump=self.jum)

        elif pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if self.x < self.left_limit:
                self.x += self.speed
                self.rot = True
                player.show(self.var % 2, self.rot, jump=self.jum)

        else:
            # self.jum = False
            player.show(0, self.rot, jump=self.jum)

        self.var += self.anim_speed
        return self.x

import pygame

class HitBox:
    # initializes some images and vars
    def __init__(self):
        self.brick_image = pygame.image.load('images/brick.png')
        self.width = 30

        # default block (brick) vertices x, y
        self.brick_block = [
                 [510,270],  [640,270],  [670,270],
                 [700,270],  [730,270],  [760,270],
                [1460,270], [1490,270], [1520,270],
                [2000,270], [2200,270], [2230,270],
                [2390,270], [2480,270], [2580,270],
                [2770,270], [3110,270], [3340,270]]

        self.qtd_blocks = len(self.brick_block)

    # display the blocks through the matrix
    def show(self, display):
        for b in range(len(self.brick_block)):
            display.display.blit(self.brick_image, (self.brick_block[b][0], self.brick_block[b][1]))

    # makes every single block move along with the background
    def move_right(self, bkgd):
        for i in range(len(self.brick_block)):
            self.brick_block[i][0] -= bkgd.speed


    # makes every single block move along with the background
    def move_left(self, bkgd):
        for i in range(len(self.brick_block)):
            self.brick_block[i][0] += bkgd.speed

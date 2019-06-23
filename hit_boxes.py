import pygame

class HitBox:
    def __init__(self):
        self.brick_image = pygame.image.load('images/brick.png')

        # matrix of block vertices x, y (superior left corner)
        self.brick_block = [
                 [1000,300],[1200,300],[1300,300],
                 [1600,300],[1700,300],[2300,300],
                 [2400,300],[2500,300],[3000,300],
                 [3300,300],[3800,300],[4000,300],
                 [4100,300],[4200,300],[4300,300],
                 [4800,300],[4900,300],[5000,300]]

        # count how many block are in the matrix
        self.qtd_blocks = len(self.brick_block)

    # display the blocks through the matrix
    def show(self, display):
        for b in range(len(self.brick_block)):
            display.display.blit(self.brick_image, (self.brick_block[b][0], self.brick_block[b][1]))

    # makes every single block move along with the background
    def move_right(self, bkgd):
        for i in range(len(self.brick_block)):
            # the block moves in the oposite direction of the player
            self.brick_block[i][0] -= bkgd.speed


    # makes every single block move along with the background
    def move_left(self, bkgd):
        for i in range(len(self.brick_block)):
            # the block moves in the oposite direction of the player
            self.brick_block[i][0] += bkgd.speed

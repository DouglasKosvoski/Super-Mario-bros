import pygame

class HitBox:
    # initializes some images and vars
    def __init__(self):
        self.brick_image = pygame.image.load('images/brick.png')
        self.special_image = pygame.image.load('images/special_brick.png')
        self.width = 30

        # holes vertices
        self.holes =[
                [1920, 1965], [2460, 2535], [4605, 4645]]

        # special block vertices x, y
        self.special_block = [
                [510, 270], [670,270], [700,145], [730,270],
                [2490,270],[3000,145],[3390,270],[3480,145],
                [3480,270],[3580,270],[4110,145],[4140,145],
                [5430,270]]

        # default block (brick) vertices x, y
        self.brick_block = [
                [640,270], [700,270], [760,270], [2460,270],
                [2520,270],[2550,145],[2580,145],[2610,145],
                [2640,145],[2670,145],[2700,145],[2730,145],
                [2760,145],[2790,145],[2910,145],[2940,145],
                [2970,145],[3000,270],[3200,270],[3230,270],
                [3770,270],[3870,145],[3900,145],[3930,145],
                [4080,145],[4110,270],[4140,270],[4170,145],
                [5370,270],[5400,270],[5460,270]]

    # display the blocks through the matrix
    def show(self, display):
        for b in range(len(self.brick_block)):
            display.display.blit(self.brick_image, (self.brick_block[b][0], self.brick_block[b][1]))

        for s in range(len(self.special_block)):
            display.display.blit(self.special_image, (self.special_block[s][0], self.special_block[s][1]))

    # makes every single block move along with the background
    def move_right(self, bkgd):
        for i in range(len(self.brick_block)):
            self.brick_block[i][0] -= bkgd.speed

        for j in range(len(self.special_block)):
            self.special_block[j][0] -= bkgd.speed

    # makes every single block move along with the background
    def move_left(self, bkgd):
        for i in range(len(self.brick_block)):
            self.brick_block[i][0] += bkgd.speed

        for j in range(len(self.special_block)):
            self.special_block[j][0] += bkgd.speed

import pygame

class HitBox:
    def __init__(self):
        self.coin_image = pygame.image.load('images/coin.png')

        # matrix of coin vertices x, y (superior left corner)
        self.coin = [
                 [1000,300],[1200,300],[1300,300],
                 [1600,300],[1700,300],[2300,300],
                 [2400,300],[2500,300],[3000,300],
                 [3300,300],[3800,300],[4000,300],
                 [4100,300],[4200,300],[4300,300],
                 [4800,300],[4900,300],[5000,300]]

        # count how many coins are in the matrix
        self.qtd_coin = len(self.coin)

    # display the coins through the matrix
    def show(self, display):
        for b in range(len(self.coin)):
            display.display.blit(self.coin_image, (self.coin[b][0], self.coin[b][1]))

    # makes every single coin move along with the background
    def move_right(self, bkgd):
        for i in range(len(self.coin)):
            # the coins moves in the oposite direction of the player
            self.coin[i][0] -= bkgd.speed


    # makes every single coin move along with the background
    def move_left(self, bkgd):
        for i in range(len(self.coin)):
            # the coins moves in the oposite direction of the player
            self.coin[i][0] += bkgd.speed

import pygame

pygame.init()
pygame.key.set_repeat(1,1)
time = pygame.time.Clock()

class Canvas:
    def __init__(self):
        Canvas.x = 0
        self.y = 0
        Canvas.width = 600
        Canvas.height = 450
        Canvas.display = pygame.display.set_mode((Canvas.width, Canvas.height))
        pygame.display.set_caption("Super Mario - Douglas Kosvoski")

    def background(self):
        self.image = pygame.image.load("world1-1.png")
        # self.image = pygame.image.load("world1-1.png")
        self.display.blit(self.image, (Canvas.x, self.y))

    def move_right(self):
        Canvas.x -= Player.speed
        return Canvas.x

    def move_left(self):
        if Canvas.x < 0:
            Canvas.x += Player.speed
        return self.x

    def move_up(self):
        Player.y -= Player.speed
        return Player.y

    def move_down(self):
        Player.y += Player.speed
        return Player.y

class Event:
    def __init__(self):
        pass

    def check_event():
        mario.on_collision()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            mario.jump()

        # if pygame.key.get_pressed()[pygame.K_w]:
        #     bkgd.move_up()
        #
        # if pygame.key.get_pressed()[pygame.K_s]:
        #     bkgd.move_down()


        if pygame.key.get_pressed()[pygame.K_d]:
            if mario.on_collision() == False:
                mario.ultima_tecla = 'right'
                bkgd.move_right()
                brick.move_right()
                spec.move_right()

        elif pygame.key.get_pressed()[pygame.K_a]:
            if mario.on_collision() == False:
                mario.ultima_tecla = 'left'
                bkgd.move_left()
                brick.move_left()
                spec.move_left()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

class Player(Canvas):

    def __init__(self):
        self.ultima_tecla = 0
        Player.width = 28
        self.height = 30
        Player.speed = 10
        Player.x = (Canvas.width/ 2) - (self.width / 2) + 4
        Player.y = 370
        self.on_ground = True
        self.g_force = 15
        self.jump_force = 150
        self.display = Canvas.display

    def show(self):
        pygame.draw.rect(self.display, (255,255,255), [self.x, self.y, self.width, self.height])
        # self.image = pygame.image.load("world1-1.png")
        # self.display.blit(self.image, (self.x, self.y))

    def jump(self):
        if self.on_ground == True:
            self.y -= self.jump_force
            self.on_ground = False
        return self.y

    def gravity(self, limit):
        if self.y < limit - self.height:
            self.y += self.g_force
        else:
            self.on_ground = True

        return self.y

    def on_collision(self):
        atual_pos_x = Canvas.x - self.width + 10
        atual_pos_y = self.y - self.height
        # print()
        # print(self.x, self.y)

        ############# PIPES HIT-BOX ########################
        #### pipe 1
        if -595 > atual_pos_x and atual_pos_x > -686:
            if 335 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -577
                else:
                    Canvas.x = -640 - self.width
                return True
            else:
                self.on_ground = True
            self.y = 335 - self.height

        #### pipe 2
        #### pipe 2
        elif -918 > atual_pos_x and atual_pos_x > -1003:
            if 300 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -900
                else:
                    Canvas.x = -998
                return True
            else:
                self.on_ground = True
            self.y = 305 - self.height
        #### pipe 3
        elif -1174 > atual_pos_x and atual_pos_x > -1260:
            if 272 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -1156
                else:
                    Canvas.x = -1242
                return True
            else:
                self.on_ground = True
            self.y = 272 - self.height
        #### pipe 4
        elif -1527 > atual_pos_x and atual_pos_x > -1612:
            if 272 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -1508
                else:
                    Canvas.x = -1594
                return True
            else:
                self.on_ground = True
            self.y = 272 - self.height
        #### pipe 5
        elif -4916 > atual_pos_x and atual_pos_x > -5000:
            if 335 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -4898
                else:
                    Canvas.x = -4984
                return True
            else:
                self.on_ground = True
            self.y = 335 - self.height
        #### pipe 6
        elif -5428 > atual_pos_x and atual_pos_x > -5518:
            if 335 < atual_pos_y:
                if self.ultima_tecla == 'right':
                    Canvas.x = -5410
                else:
                    Canvas.x = -5500
                return True
            else:
                self.on_ground = True
            self.y = 335 - self.height

        ############# BURACOS HIT-BOX ########################
        #### buraco 1
        elif -1936 > atual_pos_x and atual_pos_x > -1970:
            mario.gravity(800)
            mario.on_ground = False
            if 400 < atual_pos_y:
                print('game over')
        #### buraco 2
        elif -2478 > atual_pos_x and atual_pos_x > -2546:
            mario.gravity(800)
            mario.on_ground = False

            if 400 < atual_pos_y:
                print('game over')
        #### buraco 3
        elif -4620 > atual_pos_x and atual_pos_x > -4656:
            mario.gravity(800)
            mario.on_ground = False

            if 400 < atual_pos_y:
                print('game over')

        else:
            mario.gravity(365+self.height)
        return False


class Special_Brick:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.broken = False
        self.image = pygame.image.load("tijolo_especial.png")
        self.spec_pos = [
        [510, 270], [670,270], [700,145], [730,270],
        [2490,270],[3000,145],[3390,270],[3480,145],
        [3480,270],[3580,270],[4110,145],[4140,145],
        [5430,270]
        ]



    def show(self):
        for b in range(0, len(self.spec_pos)):
            sx = self.spec_pos[-b][0]
            sy = self.spec_pos[-b][1]
            sw = self.width
            sh = self.height
            Canvas.display.blit(self.image, (sx, sy))

            if sx < mario.x and mario.x < sx + sw or sx < mario.x + mario.width and mario.x + mario.width < sx + sw:
                if sy < mario.y and mario.y < sy + sh:
                    self.spec_pos.pop(-b)



    def move_left(self):
        if Canvas.x < 0:
            for i in range(len(self.spec_pos)):
                self.spec_pos[i][0] = self.spec_pos[i][0] + 10
        return self.spec_pos

    def move_right(self):
        for i in range(len(self.spec_pos)):
            self.spec_pos[i][0] = self.spec_pos[i][0] - 10
        return self.spec_pos


class Brick:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.broken = False
        self.image = pygame.image.load("tijolo_padrao.png")
        self.brick_pos = [
        [640,270], [700,270], [760,270], [2460,270],
        [2520,270],[2550,145],[2580,145],[2610,145],
        [2640,145],[2670,145],[2700,145],[2730,145],
        [2760,145],[2790,145],[2910,145],[2940,145],
        [2970,145],[3000,270],[3200,270],[3230,270],
        [3770,270],[3870,145],[3900,145],[3930,145],
        [4080,145],[4110,270],[4140,270],[4170,145],
        [5370,270],[5400,270],[5460,270]]


    def show(self):
        for b in range(0, len(self.brick_pos)):
            bx = self.brick_pos[-b][0]
            by = self.brick_pos[-b][1]
            bw = self.width
            bh = self.height
            Canvas.display.blit(self.image, (bx, by))

            if bx < mario.x and mario.x < bx + bw or bx < mario.x + mario.width and mario.x + mario.width < bx + bw:
                if by < mario.y and mario.y < by + bh:
                    self.brick_pos.pop(-b)



    def move_left(self):
        if Canvas.x < 0:
            for i in range(len(self.brick_pos)):
                self.brick_pos[i][0] = self.brick_pos[i][0] + 10
        return self.brick_pos

    def move_right(self):
        for i in range(len(self.brick_pos)):
            self.brick_pos[i][0] = self.brick_pos[i][0] - 10
        return self.brick_pos



bkgd = Canvas()
mario = Player()
brick = Brick()
spec = Special_Brick()

while True:
    # print(mario.__dict__)
    bkgd.background()
    mario.show()
    brick.show()
    spec.show()



    Event.check_event()
    time.tick(60)
    pygame.display.update()

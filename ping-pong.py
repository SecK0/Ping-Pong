from pygame import *

font.init()
back = (200,255,255)
win_height = 500
win_width = 1000
window = display.set_mode((win_width, win_height))
window.fill(back)
clock = time.Clock()

clock = time.Clock()
FPS = 60
game = True
finish = False


class GameSpirit(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSpirit):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_width - 80: 
            self.rect.y += self.speed
class Player2(GameSpirit):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_width - 80: 
            self.rect.y += self.speed

font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 50)
win = font2.render("1 PLAYER WIN!", True, (255, 255, 255))
lose = font2.render("2 PLAYER WIN!", True, (180, 0, 0))
racket = Player("racket.png", 100, 200, 25, 80, 5)
racket2 = Player2("racket.png", 900, 200, 25, 80, 5)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket.update()
    racket.reset()
    racket2.update()
    racket2.reset()

    display.update()
    clock.tick(FPS)

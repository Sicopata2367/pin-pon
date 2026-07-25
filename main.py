from pygame import *

window = display.set_mode((700, 500))
display.set_caption('pin pon')
bg = transform.scale(image.load('OIP (2).jpg'), (700, 500))

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, speed, w, h):
        super().__init__(img, x, y, speed, w, h)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        if sprite.collide_rect(self, p1) or sprite.collide_rect(self, p2):
            self.speed_x *= -1
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1


p1 =  Player1('racket.png', 0, 200, 5, 10, 80)
p2 =  Player2('racket.png', 690, 200, 5, 10, 80)
bal = Ball('tenis_ball.png', 456, 239, 5, 50, 50)

font.init()
font1 = font.SysFont('verdana', 50)

win = font1.render('p1 gano!', True, (0, 255, 0))
win2 = font1.render('p2 gano!', True, (0, 255, 0))

game = True
finish = False
while game:

    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg,(0, 0))
        p1.update()
        p1.reset()
        p2.update()
        p2.reset()
        bal.update()
        bal.reset()
        if bal.rect.x < 0:
            window.blit(win2, (50, 50))
            finish = True
        if bal.rect.x > 650:
            window.blit(win, (50, 50))
            finish = True




    display.update()
    clock.tick(60)
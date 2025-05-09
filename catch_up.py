from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        display_.blit(self.image, (self.rect.x, self.rect.y))


class Hunter(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


class Innocent1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


class Innocent2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_k] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_h] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_u] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_j] and self.rect.y < 500 - 80:
            self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, wall_x, wall_y):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        display_.blit(self.image, (self.rect.x, self.rect.y))



display_ = display.set_mode((700, 500))
display.set_caption('Догонялки')

background = transform.scale(image.load('background.png'), (700, 500))
player1 = Hunter('sprite1.png', 50, 200, 4)
player2 = Innocent1('sprite2.png', 50, 300, 7)

fps = 60
game_cycle = time.Clock()
run = True
finish = False

font.init()
font = font.Font(None, 70)
hunter = font.render('Охотники победили', True, (255, 0, 0))
innocents = font.render('Выжившие победили', True, (255, 0, 0))
while run:
    display_.blit(background, (0, 0))
    for click in event.get():
        if click.type == QUIT:
            run = False
    
    if finish != True:
        display_.blit(background, (0, 0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
    if sprite.collide_rect(player1, player2):
        display_.blit(hunter, (80, 200))
    
    display.update()
    game_cycle.tick(fps)
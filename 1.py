import pygame
import os
import random


z = 0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, va):
        super().__init__(all_sprites)
        self.y = y
        self.add(balls)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x - 20, y, 2 * radius, 2 * radius)
        self.vx = -2 * (va[0])
        self.vy = 2 * (va[1])

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        self.y += self.vy
        if self.y >= 800:
            all_sprites.remove(self)


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.add(ground)
        self.radius = 800
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(0, 102, 51), (self.radius, self.radius), self.radius)
        self.rect = pygame.Rect(-540, 750, 2 * self.radius, 2 * self.radius)

    def update(self):
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            pass


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        self.n = 0
        self.hp = hp
        self.hod1 = hod
        self.hod = hod
        self.x = x
        super().__init__(all_sprites)
        self.add(cube)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("blue"), (0, 0, 100, 100))
        self.rect = pygame.Rect(x, y, 101, 101)

    def update(self):
        if hod > self.hod:
            self.hod = hod
            self.rect = self.rect.move(0, 100)
        if pygame.sprite.spritecollideany(self, balls):
            self.hp -= 1
        if self.hp == 0:
            self.rect = pygame.Rect(1000, 0, 100, 100)
            all_sprites.remove(horizontal_borders, vertical_borders)
            horizontal_borders.remove(horizontal_borders)
            vertical_borders.remove(vertical_borders)
            Border(5, 5, width - 5, 5)
            Border(5, 5, 5, height - 5)
            Border(width - 5, 5, width - 5, height - 5)
            cube.remove(self)
        elif self.hp == 1:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("red"), (0, 0, 100, 100))
        elif self.hp > 1 and self.hp <= 5:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("orange"), (0, 0, 100, 100))
        elif self.hp > 5 and self.hp <= 10:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("yellow"), (0, 0, 100, 100))
        elif self.hp > 10 and self.hp <= 15:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("green"), (0, 0, 100, 100))
        elif self.hp > 15 and self.hp <= 20:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("blue"), (0, 0, 100, 100))
        elif self.hp > 20:
            self.image = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, pygame.Color("black"), (0, 0, 100, 100))
        if not(pygame.sprite.spritecollideany(self, ground)) and self.n != 1 and self.hp != 0:
            Border(self.x, 5 + self.hod - self.hod1, 100 + self.x, 5 + self.hod - self.hod1)
            Border(self.x, 5 + self.hod - self.hod1, self.x, 105 + self.hod - self.hod1)
            Border(100 + self.x, 5 + self.hod - self.hod1, 100 + self.x, 105 + self.hod - self.hod1)
            Border(self.x, 105 + self.hod - self.hod1, 100 + self.x, 105 + self.hod - self.hod1)
        else:
            self.rect = pygame.Rect(1000, 0, 100, 100)
            all_sprites.remove(self)
            self.n = 1


all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
balls = pygame.sprite.Group()
ground = pygame.sprite.Group()
cube = pygame.sprite.Group()

fps = 100
clock = pygame.time.Clock()

size = width, height = 510, 810
screen = pygame.display.set_mode(size)
pygame.init()
running = True
x = 0
v = 10  # пикселей в секунду
a = ' '
hod = 0
c4et = 0
voz = [[-5, -1], [-4, -2], [-4, -3],
       [-3, -4], [-2, -4], [-1, -5], [0, -5],
       [1, -5], [2, -4], [3, -4], [4, -3],
       [4, -2], [5, -1]]
num = 6
Border(5, 5, width - 5, 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
Cube(5 + random.choice((0, 100, 200, 300, 400)), 5, 1)

col = 1
col2 = 1

while running:
    screen.fill((155, 155, 255))
    font = pygame.font.Font(None, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_DOWN:
                if col != 0:
                    Ball(20, 255, 700, voz[num])
                    col -= 1
            if event.key == pygame.K_LEFT:
                if num < 12:
                    num += 1
            if event.key == pygame.K_RIGHT:
                if num > 0:
                    num -= 1
            if event.key == pygame.K_r:
                if col2 < 50:
                    col2 += 1
                elif col == 50:
                    z = 1
                col = col2
                hod += 100
                c = [0, 100, 200, 300, 400]
                if col2 <= 5:
                    for i in range(1):
                        d = random.choice(c)
                        c.remove(d)
                        Cube(5 + d, 5, col2)
                elif col2 > 5 and col2 <= 10:
                    for i in range(2):
                        d = random.choice(c)
                        c.remove(d)
                        Cube(5 + d, 5, col2)
                elif col2 > 10 and col2 <= 15:
                    for i in range(3):
                        d = random.choice(c)
                        c.remove(d)
                        Cube(5 + d, 5, col2)
                elif col2 > 15 and col2 <= 20:
                    for i in range(4):
                        d = random.choice(c)
                        c.remove(d)
                        Cube(5 + d, 5, col2)
                elif col2 > 20 and col2 <= 25:
                    for i in range(5):
                        d = random.choice(c)
                        c.remove(d)
                        Cube(5 + d, 5, col2)
                elif col2 > 25:
                    pass
    if z == 0:
        text = font.render('', 1, (100, 255, 100))
    elif z == 1:
        text = font.render('Игра окончена', 1, (255, 100, 100))
        text_x = width / 2 - width / 5
        text_y = height / 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        text2 = font.render('Ваш счёт:' + str(75 - len(cube)), 1, (255, 100, 100))
        text2_x = width / 2 - width / 5
        text2_y = height / 2 + height / 10
        text2_w = text.get_width()
        text2_h = text.get_height()
        screen.blit(text2, (text2_x, text2_y))
    text_x = width / 2 - width / 5
    text_y = height / 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    if col2 < 30:
        all_sprites.update()
        all_sprites.draw(screen)
    else:
        z = 1
    all_sprites.remove(horizontal_borders, vertical_borders)
    horizontal_borders.remove(horizontal_borders)
    vertical_borders.remove(vertical_borders)
    Border(5, 5, width - 5, 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    x += v / fps
    clock.tick(fps)
    Ground()
    pygame.draw.line(screen, (0, 0, 0), (255, 700), (255 - voz[num][0] * 50, 700 + voz[num][1] * 50), 1)
    pygame.display.flip()

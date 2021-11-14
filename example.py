import pygame
import random
width = 700
height = 600
fps = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
size_y = 5
class Player(pygame.sprite.Sprite):#класс наследуется от объекта  библиотеки pugame
    def __init__(self):#метод запускается при обращении к классу

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 , height )

    def update(self):#запускается при каждом кадре
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.right >= 630:
            self.rect.right = 630
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height
class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((random.randrange(40,70),random.randrange(30,80)))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 9)

    def update(self):


            self.rect.y += self.speedy

            if self.rect.top > height + 10:
                self.rect.x = random.randrange(width - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 16)

class Player_3(pygame.sprite.Sprite):
    def __init__(self):#метод запускается при обращении к классу

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (420 , height )

    def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            if keystate[pygame.K_UP]:
                self.speedy = -8
            if keystate[pygame.K_DOWN]:
                self.speedy = 8
            self.rect.y += self.speedy

            self.rect.x += self.speedx
            if self.rect.right >= width:
                self.rect.right = width
            if self.rect.left <= 70:
                self.rect.left = 70
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= height:
                self.rect.bottom = height




pygame.init()# создаём окно
pygame.mixer.init()# создаём настройки для звука
screen = pygame.display.set_mode((width, height))# переменная отвечающая за окно с настройками
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
play = True
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
player_3 = Player_3()
all_sprites.add(player)
all_sprites.add(player_3)
for i in range(16):
    m = Player_2()
    all_sprites.add(m)
    mobs.add(m)
while play:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

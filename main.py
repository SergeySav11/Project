import pygame
width = 700
height = 600
fps = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
size_x = 10
size_y = 5
class Player(pygame.sprite.Sprite):#класс наследуется от объекта  библиотеки pugame
    def __init__(self):#метод запускается при обращении к классу

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (65 , height / 2 )

    def update(self):#запускается при каждом кадре
        global size_y

        if self.rect.bottom == height:
            size_y = -5
        if self.rect.top == 0:
            size_y = 5
        self.rect.y += size_y

size_y2 = -5
class Player_2(pygame.sprite.Sprite):

        def __init__(self):

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((60,60))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.center = ( 180, height / 2)

        def update(self):
            global size_y2

            if self.rect.top == 0:
                size_y2 = 5
            if self.rect.bottom == height:
                size_y2 = -5
            self.rect.y += size_y2


class Player_3(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (295 , height / 2 )

    def update(self):
        global size_y

        if self.rect.bottom == height:
            size_y = -5
        if self.rect.top == 0:
            size_y = 5
        self.rect.y += size_y

class Player_4(pygame.sprite.Sprite):
        def __init__(self):

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((60, 60))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (400, height / 2)

        def update(self):
            global size_y2

            if self.rect.top == 0:
                size_y2 = 5
            if self.rect.bottom == height:
                size_y2 += -5
            self.rect.y += size_y2









pygame.init()# создаём окно
pygame.mixer.init()# создаём настройки для звука
screen = pygame.display.set_mode((width, height))# переменная отвечающая за окно с настройками
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
play = True
all_sprites = pygame.sprite.Group()
player = Player()
player_2 = Player_2()
player_3 = Player_3()
player_4 = Player_4()
all_sprites.add(player)
all_sprites.add(player_2)
all_sprites.add(player_3)
all_sprites.add(player_4)
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

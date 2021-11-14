import pygame
import random

WIDTH = 800
HEIGHT = 650
FPS = 15

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Загрузка изображения
image_all = pygame.image.load('img.png',)
stay_down = image_all.subsurface(10,12,30,65)
stay_left = image_all.subsurface(116,90,30,65)
stay_up = image_all.subsurface(116,240,30,60)
stay_right = image_all.subsurface(116,165,35,63)


down_left = image_all.subsurface(60,12,35,60)
down_right = image_all.subsurface(165,13,35,60)
left_left = image_all.subsurface(60,92,45,60)
left_right = image_all.subsurface(162,92,45,60)
up_left = image_all.subsurface(162,244,45,60)
up_right = image_all.subsurface(60,244,45,60)
right_left = image_all.subsurface(155,165,53,63)
right_right = image_all.subsurface(58,165,53,63)

steps_d = [down_left,down_right]
steps_l = [left_right,left_left]
steps_u = [up_left,up_right]
steps_r = [right_left,right_right]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = stay_down
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
p = 0
i = 0
o = 0
t = 0
flag = 'down'
# Цикл игры
running = True
while running:
    speedx = 0
    speedy = 0
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            speedy = -7
            o = (o + 1) % 2
            player.image = steps_u[o]
            flag = 'up'
        if keys[pygame.K_s]:
            speedy = 7
            p = (p + 1) % 2
            player.image = steps_d[p]
            flag = 'down'
        if keys[pygame.K_a]:
            speedx = -7
            i = (i + 1) % 2
            player.image = steps_l[i]
            flag = 'left'
        if keys[pygame.K_d]:
            speedx = 7
            t = (t + 1) % 2
            player.image = steps_r[t]
            flag = 'right'
        player.rect.x += speedx
        player.rect.y += speedy
        print(speedy)
        print(speedx)
        # Обновление
    all_sprites.update()
    #Проверка стоим ли мы на месте
    if speedy == 0 and speedx == 0:
        if flag == 'left':
            player.image = stay_left
        elif flag == 'down':
            player.image = stay_down
        elif flag == 'up':
            player.image = stay_up
        elif flag == 'right':
            player.image = stay_right
        # elif flag == 'right':
        #     player.image = stay_right
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()


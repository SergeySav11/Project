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
flag = 0
speedx = 0
speedy = 0


#Написать функцию удара которую удаляет обьекты из группы по нажатию на пробел



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
objects_cords = [[700,325],[525,-200],[-100,250],[400,1000]]
trees_cords = [[490,300],[508,319],[524,300],[540,280]]
image_objects = [pygame.image.load('tree.png'), pygame.image.load('rock.png')]
objects = pygame.sprite.Group()
class Object(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(image_objects)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def walk(self):
            global speedx
            global speedy
            speedx = 0
            speedy = 0
            if flag == 'left':
                speedx = 8
            self.rect.x += speedx
            if flag == 'right':
                speedx = -8
            self.rect.x += speedx
            if flag == 'up':
                speedy = 8
            self.rect.y += speedy
            if flag == 'down':
                speedy = -8
            self.rect.y += speedy

class Tree(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        tree_pict = pygame.image.load('tree.png')
        self.image = pygame.transform.scale(tree_pict,(25,40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def walk(self):
        global speedx
        global speedy
        speedx = 0
        speedy = 0
        if flag == 'left':
            speedx = 8
        self.rect.x += speedx
        if flag == 'right':
            speedx = -8
        self.rect.x += speedx
        if flag == 'up':
            speedy = 8
        self.rect.y += speedy
        if flag == 'down':
            speedy = -8
        self.rect.y += speedy


    #Написать функцию премещенмя обьектов в которой подается один параметр верх,вниз,вправо или лево


for i in objects_cords:
    x = i[0]
    y = i[1]
    a = Object(x,y)
    objects.add(a)

for b in trees_cords:
    t = Tree(b[0],b[1])
    objects.add(t)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        global steps_d
        global steps_u
        global steps_l
        global steps_r
        global stay_left
        global stay_right
        global stay_up
        global stay_down
        pygame.sprite.Sprite.__init__(self)
        image_all = pygame.image.load('img.png').convert()
        stay_down = image_all.subsurface(10, 12, 30, 65)
        stay_left = image_all.subsurface(116, 90, 30, 65)
        stay_up = image_all.subsurface(116, 240, 30, 60)
        stay_right = image_all.subsurface(116, 165, 35, 63)
        self.image = pygame.transform.scale(stay_down,(40,70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        down_left = image_all.subsurface(60, 12, 35, 60)
        down_right = image_all.subsurface(165, 13, 35, 60)
        left_left = image_all.subsurface(60, 92, 45, 60)
        left_right = image_all.subsurface(162, 92, 45, 60)
        up_left = image_all.subsurface(162, 244, 45, 60)
        up_right = image_all.subsurface(60, 244, 45, 60)
        right_left = image_all.subsurface(155, 165, 53, 63)
        right_right = image_all.subsurface(58, 165, 53, 63)

        steps_d = [down_left, down_right]
        steps_l = [left_right, left_left]
        steps_u = [up_left, up_right]
        steps_r = [right_left, right_right]



player = Player()
all_sprites.add(player)
q = 0
p = 0
k = 0
v = 0
flag = 'down'
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
    # check
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            for o in objects:
                o.walk()
            o = (v + 1) % 2
            player.image = steps_u[v]
            flag = 'up'
        if keys[pygame.K_s]:
            for o in objects:
                o.walk()
            p = (p + 1) % 2
            player.image = steps_d[p]
            flag = 'down'
        if keys[pygame.K_a]:
            for o in objects:
                o.walk()
            i = (k + 1) % 2
            player.image = steps_l[k]
            flag = 'left'
        if keys[pygame.K_d]:
            for o in objects:
                o.walk()
            t = (q + 1) % 2
            player.image = steps_r[q]
            flag = 'right'

        if speedy == 0 and speedx == 0:
            if flag == 'left':
                player.image = stay_left
            elif flag == 'down':
                player.image = stay_down
            elif flag == 'up':
                player.image = stay_up
            elif flag == 'right':
                player.image = stay_right
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(GREEN)
    all_sprites.draw(screen)
    objects.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

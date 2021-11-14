# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH, HEIGHT = 10, 20
FPS = 60
SIZE = 45

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH * SIZE, HEIGHT * SIZE))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
grid = [pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE) for x in range(WIDTH) for y in range(HEIGHT)]

# Цикл игры
running = True
while running:
# Держим цикл на правильной скорости
    clock.tick(FPS)
# Ввод процесса (события)
    for event in pygame.event.get():
# check for closing window
        if event.type == pygame.QUIT:
            running = False
    [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]
# Обновление

# Рендеринг
    screen.fill(BLACK)
# После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
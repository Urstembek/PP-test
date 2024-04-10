import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Lines")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование случайных линий
    for _ in range(20):  # Число линий
        # Генерация случайных координат начала и конца линии
        start_pos = (random.randint(0, width), random.randint(0, height))
        end_pos = (random.randint(0, width), random.randint(0, height))
        # Генерация случайного цвета
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Рисование линии
        pygame.draw.line(screen, color, start_pos, end_pos, random.randint(1, 5))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
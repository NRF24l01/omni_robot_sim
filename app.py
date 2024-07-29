import pygame
from pygame.transform import scale

from omni_robot import Omni

pygame.init()

width, height = 900, 600

# 900 / 3000 * размер в мм = размер в пикселях

# создаем окно размера 800 на 600
screen = pygame.display.set_mode((width, height))
# загружаем картинку из папки
big_sky = pygame.image.load("static/images/field.png")
# масштабируем картинку под размер экрана
sky = scale(big_sky, (width, height))

# указываем название
pygame.display.set_caption("Omni sim")
clock = pygame.time.Clock()

main_robot = Omni(20, 20)

main_robot.set_target(50, 50, 0, 20)

# игровой цикл
while True:
    dt = clock.tick(10)
    # обрабатываем события
    for e in pygame.event.get():
        # если нажали на крестик
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")

    # рисуем картинку с небом на экране
    screen.blit(sky, (0, 0))

    main_robot.update(dt)
    main_robot.draw(screen)

    # перерисовать окно
    pygame.display.update()

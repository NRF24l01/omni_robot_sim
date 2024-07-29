import pygame
from pygame import draw
from pygame.transform import scale, rotate
from omni_calc import calculate_resultant_vector, polar_to_cartesian
from time import time


class Omni(pygame.sprite.Sprite):
    def __init__(self, x, y, width=84, height=84, sprite_path="static/images/omni_main.png", radius=128, debug_draw=True):
        pygame.sprite.Sprite.__init__(self)

        self.radius = 0.3 * radius

        # Coliders
        self.rect = pygame.Rect(x, y, width, height)
        self.angle = 0

        # Graphics
        self.image = scale(pygame.image.load(sprite_path), (width, height))

        # Help drawing
        self.ddraw = debug_draw
        self.dots = []

        # Move
        self.ltime = 0
        self.xax = 0  # x axel
        self.yax = 0  # y axel
        self.xlost = 0  # x lost
        self.ylost = 0  # y lost
        self.in_moving = False
        self.motor_speeds = [0, 0, 0]  # mm/s
        self.time_remain = 0  # seconds

    def set_target(self, m1, m2, m3, time):
        self.motor_speeds = [m1, m2, m3]
        self.time_remain = time

        resultant_length, resultant_angle = calculate_resultant_vector(self.motor_speeds[0], self.motor_speeds[1],
                                                                       self.motor_speeds[2], self.radius)

        resultant_length, resultant_angle = round(resultant_length, 2), round(resultant_angle, 2)

        print("Resulta: ", resultant_length, resultant_angle)

        self.dots.clear()

        if round(resultant_length) != 0:
            self.angle += resultant_angle
            self.angle %= 360
            v_x, v_y = polar_to_cartesian(resultant_length, self.angle)
            v_x = 900 / 3000 * v_x
            v_y = 600 / 2000 * v_y
            print("movingi: ", v_x, v_y)
            self.xax = round(v_x, 4)
            self.yax = round(v_y, 4)
            self.xlost = round(v_x * time, 4)
            self.ylost = round(v_y * time, 4)
            print("target: ", v_x * time, v_y * time)
            self.dots.append({"type": "target", "x": self.rect.x+self.xlost+self.radius, "y": self.rect.y+self.ylost+self.radius})
        else:
            self.angle += resultant_angle
            self.angle %= 360

    # функция рисования корабля
    def draw(self, screen):
        # рисуем корабль на экране на месте занимаемой им прямоугольной области
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for dot in self.dots:
            draw.circle(screen, "#FFFFFF", (dot["x"], dot["y"]), 5)

    # функция перемещения, параметры - нажата ли стрелочки влево и вправо
    def update(self, dt):
        print("Axas: ", self.xax, self.yax)
        print(self.xlost, self.ylost)
        if self.xlost > 0:
            self.rect.x += self.xax * (dt / 1000)
            # self.rect.y += self.yax * (dt / 1000)
            self.xlost -= round(self.xax * (dt / 1000))
            # self.ylost -= round(self.yax * (dt / 1000))
            # print("Rectas: ", self.rect.x, self.rect.y, dt)

            # print("Reetapending: ", self.xax * (dt / 1000), self.yax * (dt / 1000))



        if self.ylost > 0:
            self.rect.y += self.yax * (dt / 1000)
            self.ylost -= round(self.yax * (dt / 1000))

import customtkinter as ctk
import time
import math


class OmniRobot:
    def __init__(self, distance_to_wheels, wheel_width, wheel_height):
        self.distance_to_wheels = distance_to_wheels  # расстояние от центра робота до каждого колеса
        self.wheel_width = wheel_width  # ширина каждого колеса
        self.wheel_height = wheel_height  # высота каждого колеса

    def draw(self, canvas, x, y, angle):
        # Углы, под которыми расположены колеса относительно центра (в градусах)
        wheel_angles = [0, 120, 240]

        # Рисуем тело робота как круг
        robot_radius = self.distance_to_wheels + max(self.wheel_width, self.wheel_height) / 2
        canvas.create_oval(
            x - robot_radius, y - robot_radius,
            x + robot_radius, y + robot_radius,
            outline="black", fill="lightgrey"
        )

        # Рисуем три прямоугольных колеса, перпендикулярных радиусам
        for wheel_angle in wheel_angles:
            # Учитываем угол поворота робота
            adjusted_angle = math.radians(wheel_angle + angle)
            wheel_x = x + self.distance_to_wheels * math.cos(adjusted_angle)
            wheel_y = y + self.distance_to_wheels * math.sin(adjusted_angle)

            # Поворачиваем каждое колесо на 90 градусов относительно радиуса, чтобы оно было перпендикулярно
            wheel_rotation = adjusted_angle + math.radians(90)
            cos_a, sin_a = math.cos(wheel_rotation), math.sin(wheel_rotation)

            # Вычисляем углы прямоугольника колеса
            dx1 = (-self.wheel_width / 2) * cos_a - (-self.wheel_height / 2) * sin_a
            dy1 = (-self.wheel_width / 2) * sin_a + (-self.wheel_height / 2) * cos_a
            dx2 = (self.wheel_width / 2) * cos_a - (-self.wheel_height / 2) * sin_a
            dy2 = (self.wheel_width / 2) * sin_a + (-self.wheel_height / 2) * cos_a
            dx3 = (self.wheel_width / 2) * cos_a - (self.wheel_height / 2) * sin_a
            dy3 = (self.wheel_width / 2) * sin_a + (self.wheel_height / 2) * cos_a
            dx4 = (-self.wheel_width / 2) * cos_a - (self.wheel_height / 2) * sin_a
            dy4 = (-self.wheel_width / 2) * sin_a + (self.wheel_height / 2) * cos_a

            # Рисуем прямоугольное колесо
            canvas.create_polygon(
                wheel_x + dx1, wheel_y + dy1,
                wheel_x + dx2, wheel_y + dy2,
                wheel_x + dx3, wheel_y + dy3,
                wheel_x + dx4, wheel_y + dy4,
                outline="black", fill="darkgrey"
            )

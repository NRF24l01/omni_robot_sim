import numpy as np

# Параметры робота
r = 0.05  # Радиус колеса (м)
L = 128  # Расстояние от центра до колес (м)

# Углы расположения колес
theta = np.array([0, 120, 240]) * np.pi / 180

# Матрица Джейкоби
J = np.array([
    [-np.sin(theta[0]), np.cos(theta[0]), L],
    [-np.sin(theta[1]), np.cos(theta[1]), L],
    [-np.sin(theta[2]), np.cos(theta[2]), L]
])


def inverse_kinematics(vx, vy, omega):
    velocities = np.array([vx, vy, omega])
    wheel_speeds = np.dot(J, velocities) / r
    return wheel_speeds


# Пример использования
vx = 0.0  # Линейная скорость по оси x (м/с)
vy = 0.0  # Линейная скорость по оси y (м/с)
omega = 10.0  # Угловая скорость (рад/с)

wheel_speeds = inverse_kinematics(vx, vy, omega)
print("Скорости колес:", wheel_speeds)

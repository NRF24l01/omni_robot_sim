import math


def degrees_traveled(radius, distance):
    # Calculate the number of degrees traveled
    degrees = (180 * distance) / (math.pi * radius)
    return degrees


def calculate_resultant_vector(l1, l2, l3, robot_radius=128):
    if l1 == l2 and l1 == l3:
        traveled = l1 + l2 + l3
        degrees = degrees_traveled(robot_radius, traveled)
        return 0, degrees

    # Угол между векторами в радианах
    angle = 120 * math.pi / 180

    # Координаты векторов
    x1, y1 = l1, 0
    x2, y2 = l2 * math.cos(angle), l2 * math.sin(angle)
    x3, y3 = l3 * math.cos(-angle), l3 * math.sin(-angle)

    # Итоговые координаты
    resultant_x = x1 + x2 + x3
    resultant_y = y1 + y2 + y3

    # Итоговая длина вектора
    resultant_length = math.sqrt(resultant_x ** 2 + resultant_y ** 2)

    # Итоговый угол вектора
    resultant_angle = math.atan2(resultant_y, resultant_x)

    return resultant_length, math.degrees(resultant_angle)


def test(l1, l2, l3, r=128):
    print(f"Values to test: {l1}, {l2}, {l3}, {r}")
    resultant_length, resultant_angle = calculate_resultant_vector(l1, l2, l3)
    print(f"Resultant vector length: {round(resultant_length, 2)}")
    print(f"Resultant vector angle: {round(resultant_angle, 2)} degrees")


def polar_to_cartesian(distance, angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the change in coordinates
    delta_x = distance * math.cos(angle_radians)
    delta_y = distance * math.sin(angle_radians)

    return delta_x, delta_y


if __name__ == "__main__":
    test(1, 1, 1)
    test(1, 1, 0)
    test(10, 10, 10)

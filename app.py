import customtkinter as ctk
import math

class Omni:
    def __init__(self, canvas, x, y, radius):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.motor_speeds = [0, 0, 0]
        self.angle = 0  # Инициализация угла
        self.dots = []

    def set_target(self, m1, m2, m3, duration):
        self.motor_speeds = [m1, m2, m3]
        resultant_length, resultant_angle = self.calculate_resultant_vector()
        self.dots.clear()

        if round(resultant_length) != 0:
            self.angle = (self.angle + resultant_angle) % 360
            self.xax = round(resultant_length * math.cos(math.radians(self.angle)), 4)
            self.yax = round(resultant_length * math.sin(math.radians(self.angle)), 4)
            self.xlost = round(self.xax * duration, 4)
            self.ylost = round(self.yax * duration, 4)
            self.dots.append((self.x + self.xlost, self.y + self.ylost))

    def calculate_resultant_vector(self):
        resultant_length = math.sqrt(sum([speed ** 2 for speed in self.motor_speeds]))
        resultant_angle = math.atan2(self.motor_speeds[1], self.motor_speeds[0]) * (180 / math.pi)
        return resultant_length, resultant_angle

    def draw(self):
        self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                self.x + self.radius, self.y + self.radius, fill="blue")
        for dot in self.dots:
            self.canvas.create_oval(dot[0] - 5, dot[1] - 5, dot[0] + 5, dot[1] + 5, fill="red")

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600")
        self.root.title("Omni Robot Simulation")
        self.canvas = ctk.CTkCanvas(self.root, width=900, height=600, bg="white")
        self.canvas.pack()

        self.omni_robot = Omni(self.canvas, 100, 100, 30)
        self.omni_robot.set_target(50, 50, 0, 1)  # Пример скорости и времени

        self.update()

    def update(self):
        self.canvas.delete("all")
        self.omni_robot.draw()
        self.root.after(100, self.update)

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()

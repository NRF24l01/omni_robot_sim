import customtkinter as ctk
from PIL import Image, ImageTk
import math
from omnirobot import OmniRobot
from field


class App:
    def __init__(self, root, background="static/images/field.png", xsize=960, ysize=640):
        self.root = root
        self.root.geometry(f"{str(xsize)}x{str(ysize)}")
        self.root.title("Omni Robot Simulation")
        self.canvas = ctk.CTkCanvas(self.root, width=xsize, height=ysize, bg="white")
        self.canvas.pack()

        self.xsize = xsize
        self.ysize = ysize

        self.bg = Image.open(background).resize((xsize, ysize), Image.LANCZOS)

        self.

        self.update()

    def update(self):
        self.canvas.delete("all")

        self.canvas.image = ImageTk.PhotoImage(self.bg)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

        # Создаем объект робота
        robot = OmniRobot(distance_to_wheels=30, wheel_width=30, wheel_height=15)
        # Рисуем робота на canvas в центре с поворотом на 45 градусов
        robot.draw(self.canvas, x=100, y=200, angle=90)

        self.root.after(100, self.update)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)

    root.mainloop()

import customtkinter as ctk
from PIL import Image, ImageTk
import math
from modules.omnirobot import OmniRobot
from modules.field_items import Background
from modules.pointer import Pointer


class App:
    def __init__(self, root, background="static/images/field.png", xsize=960, ysize=640):
        self.root = root
        self.root.geometry(f"{str(xsize)}x{str(ysize)}")
        self.root.title("Omni Robot Simulation")
        self.root.resizable(False, False)

        self.canvas = ctk.CTkCanvas(self.root, width=xsize, height=ysize, bg="white")
        self.canvas.pack()

        self.xsize = xsize
        self.ysize = ysize

        self.bg = Background(background, xsize, ysize)

        self.pointer = Pointer()

        self.root.bind('<Motion>', self.on_move)

        self.update()

    def update(self):
        # Pre update
        self.canvas.delete("all")

        # Draw static
        self.bg.draw(self.canvas)

        # Draw non static
        self.pointer.draw(self.canvas)

        robot = OmniRobot(distance_to_wheels=30, wheel_width=30, wheel_height=15)
        robot.draw(self.canvas, x=100, y=200, angle=90)

        self.root.after(1, self.update)

    def on_move(self, event):
        self.pointer.update(event.x, event.y)


if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)

    root.mainloop()

import customtkinter as ctk

from PIL import Image, ImageTk
import math

from modules.omnirobot import OmniRobot
from modules.field_items import Background
from modules.pointer import Pointer

from config import key_binds_txt


class App(ctk.CTk):
    def __init__(self, background="static/images/field.png", xsize=960, ysize=640):
        super().__init__()

        # Init
        self.title("Omni Robot Simulation")
        self.resizable(False, False)

        #
        self.canvas = ctk.CTkCanvas(self, width=xsize, height=ysize, bg="white")
        self.canvas.grid(row=0, column=0)

        # Create right frame
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.keybinds_map = ctk.CTkLabel(self.right_frame, text=key_binds_txt)
        self.keybinds_map.grid(row=0, column=0, pady=(10, 0), sticky="n")

        self.mode_label = ctk.CTkLabel(self.right_frame, text="Режим: ничего")
        self.mode_label.grid(row=1, column=0, pady=(10, 0), sticky="n")

        self.xsize = xsize
        self.ysize = ysize

        self.bg = Background(background, xsize, ysize)

        self.pointer = Pointer()

        self.bind('<Motion>', self.on_move)

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

        self.after(1, self.update)

    def on_move(self, event):
        self.pointer.update(event.x, event.y)


if __name__ == "__main__":
    app = App()
    app.mainloop()

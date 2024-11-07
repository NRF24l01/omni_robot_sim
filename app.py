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

        # Create canvas
        self.canvas = ctk.CTkCanvas(self, width=xsize, height=ysize, bg="white")
        self.canvas.grid(row=0, column=0)

        # Create right frame
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        # Create mode lable
        self.mode_label = ctk.CTkLabel(self.right_frame, text="Режим: ничего")
        self.mode_label.grid(row=0, column=0, pady=(10, 0), sticky="n")

        # Create keybind map
        self.keybinds_map = ctk.CTkLabel(self.right_frame, text=key_binds_txt)
        self.keybinds_map.grid(row=1, column=0, pady=(10, 0), sticky="n")

        # Defines
        self.xsize = xsize
        self.ysize = ysize
        self.state = 0  # 0 - chill, 1 - set start point, 2 - add point

        # Add bg
        self.bg = Background(background, xsize, ysize)

        # Add pointer
        self.pointer = Pointer()

        # Binds
        self.bind('<Motion>', self.on_move)
        self.bind('s', self.on_button_click)
        self.bind('n', self.on_button_click)
        self.bind('c', self.on_button_click)
        self.bind("<Escape>", self.on_button_click)

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

    def on_button_click(self, event):
        print(event.keysym)
        if event.keysym == "s":
            # Change start point
            self.state = 1
            self.pointer.change_state(2)
        elif event.keysym == "n":
            # Change start point
            self.state = 2
            self.pointer.change_state(3)
        elif event.keysym == "c":
            # Change start point
            self.state = 3
            self.pointer.change_state(4)
        elif event.keysym == "Escape":
            # Change start point
            self.state = 0
            self.pointer.change_state(1)
        self.static_update()

    def static_update(self):
        if self.state == 0:
            self.mode_label.configure(text="Режим: ничего")
        if self.state == 1:
            self.mode_label.configure(text="Режим: установка стартовой точки")
        if self.state == 2:
            self.mode_label.configure(text="Режим: установка путевой точки")

    def on_move(self, event):
        self.pointer.update(event.x, event.y)


if __name__ == "__main__":
    app = App()
    app.mainloop()

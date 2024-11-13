import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk
import math
from json import dumps

from modules.field_items import Background, Path
from modules.pointer import Pointer
from modules.CtkListbox import CtkHoverSelectListbox

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

        self.dotbox = CtkHoverSelectListbox(self.right_frame)
        self.dotbox.grid(row=2, column=0, pady=(10, 0), sticky="n")

        # Пример элементов в Listbox
        for item in ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]:
            self.dotbox.insert(tk.END, item)

        # Create mode lable
        self.mode_label = ctk.CTkLabel(self.right_frame, text="Режим: ничего")
        self.mode_label.grid(row=0, column=0, pady=(10, 0), sticky="n")

        # Create keybind map
        self.keybinds_map = ctk.CTkLabel(self.right_frame, text=key_binds_txt)
        self.keybinds_map.grid(row=1, column=0, pady=(10, 0), sticky="n")

        # Defines
        self.xsize = xsize
        self.ysize = ysize
        self.status = 0  # 0 - chill, 1 - set start point, 2 - add point

        # Add bg
        self.bg = Background(background, xsize, ysize)

        # Add pointer
        self.pointer = Pointer()

        self.path = Path()

        # Binds
        self.canvas.bind('<Motion>', self.on_move)
        self.canvas.bind("<Button-1>", self.on_left_mouse)
        self.bind('s', self.on_button_click)
        self.bind('n', self.on_button_click)
        self.bind('c', self.on_button_click)
        self.bind("<Escape>", self.on_button_click)

        self.update()

    def update(self):
        # Update dots list
        dots_txt = []
        for index, dot in enumerate(self.path.path):
            dots_txt.append(f"{index}: {dumps(dot)}")
        self.dotbox.sync_with_data(dots_txt)

        # Pre update
        self.canvas.delete("all")

        # Draw static
        self.bg.draw(self.canvas)

        # Draw non static
        self.pointer.draw(self.canvas)
        self.path.draw(self.canvas)

        self.after(1, self.update)

    def on_button_click(self, event):
        print(event.keysym)
        if event.keysym == "s":
            # Change start point
            self.status = 1
            self.pointer.change_state(2)
        elif event.keysym == "n":
            # Change start point
            self.status = 2
            self.pointer.change_state(3)
        elif event.keysym == "c":
            # Change start point
            self.status = 3
            self.pointer.change_state(4)
        elif event.keysym == "Escape":
            # Change start point
            self.status = 0
            self.pointer.change_state(1)
        self.static_update()

    def static_update(self):
        if self.status == 0:
            self.mode_label.configure(text="Режим: ничего")
        if self.status == 1:
            self.mode_label.configure(text="Режим: установка стартовой точки")
        if self.status == 2:
            self.mode_label.configure(text="Режим: установка путевой точки")

    def on_move(self, event):
        self.pointer.update(event.x, event.y)

    def on_left_mouse(self, event):
        print("lkm")
        if self.status == 1:
            self.path.set_start_point(event.x, event.y)
        elif self.status == 2:
            self.path.add_point(event.x, event.y)


if __name__ == "__main__":
    app = App()
    app.mainloop()

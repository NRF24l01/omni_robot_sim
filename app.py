from time import time

st_time = time()

import customtkinter as ctk
import tkinter as tk

from PIL import Image, ImageTk
import math
from json import dumps

from modules.field_items import Background, Path
from modules.pointer import Pointer
from modules.listbox import CtkHoverSelectListbox
from modules.confirm_window import ConfirmationWindow

from config import key_binds_txt

from logger import Logger

st_time = time() - st_time

# Dear reader, dot = pathpoint

class App(ctk.CTk):
    def __init__(self, logger: Logger, background="static/images/field.png", xsize=960, ysize=640):
        app_init_time = time()
        super().__init__()
        self.logger = logger
        self.logger.info("Papa window inited!")

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

        # Create mode lable
        self.mode_label = ctk.CTkLabel(self.right_frame, text="Режим: ничего")
        self.mode_label.grid(row=0, column=0, pady=(10, 0), sticky="n")

        # Create keybind map
        self.keybinds_map = ctk.CTkLabel(self.right_frame, text=key_binds_txt)
        self.keybinds_map.grid(row=1, column=0, pady=(10, 0), sticky="n")

        self.logger.info("Added elements")

        # Defines
        self.xsize = xsize
        self.ysize = ysize
        self.status = 0  # 0 - chill, 1 - set start point, 2 - add point
        self.current_dot = None

        # Initing
        self.bg = Background(background, xsize, ysize, logger=self.logger)
        self.pointer = Pointer()
        self.path = Path()
        self.logger.info("Items inited")

        # Binds
        self.canvas.bind('<Motion>', self.on_move)
        self.canvas.bind("<Button-1>", self.on_left_mouse)

        # Bind path adding
        self.bind('s', self.on_button_click)  # Add start button
        self.bind('n', self.on_button_click)  # Add new path point

        # Binds for changing path
        self.bind('d', self.on_button_click)  # Delite dot
        self.bind('m', self.on_button_click)  # Move dots

        self.bind("<Escape>", self.on_button_click)
        self.dotbox.bind("<<ListboxSelect>>", self.dot_selected)
        self.logger.info("Binded!")

        app_init_time = time()-app_init_time

        self.logger.info("Modules imported by", st_time)
        self.logger.info("App inited by", app_init_time)
        self.logger.info("Total running time:", st_time+app_init_time)

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

    def dot_selected(self, event):
        self.current_dot = self.dotbox.curselection()[0]
        self.path.underline_point(self.current_dot)

    def on_button_click(self, event):
        if event.keysym == "s":
            # Change start point
            self.status = 1
            self.pointer.change_state(2)
        elif event.keysym == "n":
            # Add new point
            self.status = 2
            self.pointer.change_state(3)
        elif event.keysym == "d":
            # Change start point
            self.delite_dot()
        elif event.keysym == "Escape":
            # Escape :)
            self.status = 0
            self.current_dot = None
            self.pointer.change_state(1)
            self.path.deunderline_point()
        self.static_update()

    def delite_dot(self):
        if not self.current_dot or self.current_dot >= len(self.path.path):
            self.logger.warning("No dot selected")
            self.current_dot = None
            return
        confirm_window = ConfirmationWindow(self, title="Потвердите удаление.",
                                            message="Вы уверены, что хотите удалить точку?")
        self.wait_window(confirm_window)
        if confirm_window.result:
            self.path.path.pop(self.current_dot)

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
        if self.status == 1:
            self.path.set_start_point(event.x, event.y)
        elif self.status == 2:
            self.path.add_point(event.x, event.y)


if __name__ == "__main__":
    logger = Logger()
    logger.info("Started loading")
    app = App(logger=logger)
    app.mainloop()

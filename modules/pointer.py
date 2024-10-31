from modules.field_items import Dot
from customtkinter import CTkCanvas
from time import time


class Pointer(Dot):
    def __init__(self, pointer_radius=10, pointer_color="#ffffff"):
        super().__init__(dot_radius=pointer_radius, dot_colors=[pointer_color])

        self.x = 0
        self.y = 0

        self.color_pallet = {1: "#ffffff", 2: "#9cff17", 3: "#17ff39", 4: "#ff17dd"}
        self.blinkers = {1: None, 2: 0.5, 3: 0.5, 4: 0.5}
        self.last_upd_time = 0
        self.draw = 0

        self.ccolor = ""  # Current color
        self.state = 2

    def change_color(self, color: str):
        self.colors = [color]

    def change_state(self, state: int):
        """

        :param state: 1 - waiting for command; 2 - set start point; 3 - set path point; 4 - remove point
        """
        if 0 < state < 5:
            raise IndexError
        self.state = state

    def _color_update(self):
        self.ccolor = self.color_pallet[self.state]

    def update(self, mouseX: int, mouseY: int):
        self.x = mouseX
        self.y = mouseY

    def draw(self, canvas: CTkCanvas):
        if self.blinkers[self.state]:
            if time() - self.last_upd_time > self.blinkers[self.state]:
                if self.draw == 1:
                    self.draw_dot(canvas, self.x, self.y, self.ccolor)
                    self.draw = 0
                else:
                    self.draw = 1

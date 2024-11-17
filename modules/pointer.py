from modules.field_items import Dot
from customtkinter import CTkCanvas
from time import time


class Pointer(Dot):
    def __init__(self, pointer_radius=10, pointer_color="#ffffff"):
        super().__init__(dot_radius=pointer_radius, dot_color=[pointer_color])

        self.x = 0
        self.y = 0

        self.color_pallet = {1: "#ffffff", 2: "#9cff17", 3: "#17ff39", 4: "#ff17dd"}

        self.ccolor = ""  # Current color
        self.state_m = 2

    def change_color(self, color: str):
        self.colors = [color]

    def change_state(self, state: int):
        """

        :param state: 1 - waiting for command; 2 - set start point; 3 - set path point; 4 - remove point
        """
        if 0 > state > 5:
            raise IndexError
        self.state_m = state
        self._color_update()

    def _color_update(self):
        self.ccolor = self.color_pallet[self.state_m]

    def update(self, mouseX: int, mouseY: int):
        self.x = mouseX
        self.y = mouseY

    def draw(self, canvas: CTkCanvas):
        if self.state_m != 4:
            self.draw_outline(canvas, self.x, self.y, ocolor=self.ccolor)
        else:
            self.draw_dot(canvas, self.x, self.y, fcolor=self.ccolor)

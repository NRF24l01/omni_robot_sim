from PIL import Image, ImageTk
from customtkinter import CTkCanvas
from random import choice


class Item:
    def image_resize(self, image: str, width: int, height: int):
        return Image.open(image).resize((width, height), Image.LANCZOS)


class Background(Item):
    def __init__(self, image: str, width: int, height: int):
        self.image_path = image
        self.xsize = width
        self.ysize = height

        self.image = self.image_resize(self.image_path, self.xsize, self.ysize)
        self.tkimage = ImageTk.PhotoImage(self.image)

    def draw(self, canvas):
        canvas.create_image(0, 0, image=self.tkimage, anchor='nw')


class Dot(Item):
    def __init__(self, dot_radius=10, dot_colors=("#fb0")):
        self.dot_radius = dot_radius
        self.colors = dot_colors

    def draw_dot(self, canvas: CTkCanvas, x: int, y: int, color: str=None):
        if not color: colot = choice(self.colors)
        x1 = x - self.dot_radius / 2
        x2 = x + self.dot_radius / 2
        y1 = y - self.dot_radius / 2
        y2 = y + self.dot_radius / 2
        canvas.create_oval(x1, y1, x2, y2, outline=color, fill=color)


class Path(Dot):
    def __init__(self, statr_point: tuple = (10, 10), path=None, dot_radius=10, dot_colors=("#fb0")):
        """

        :param statr_point: Tuple with x and y start points
        :param path: Path, list with dots, dot is list with x and y coordinates
        :param dot_radius: Dot radius in px
        :param dot_colors: Dot colors, tuple
        """
        super().__init__(dot_radius, dot_colors)

        if path is None:
            path = []
        self.start_point = statr_point
        self.path = path

    def draw(self, canvas: CTkCanvas):
        self.draw_dot(canvas, self.start_point[0], self.start_point[1])
        for dot in self.path:
            self.draw_dot(canvas, dot[0], dot[1])

    def new_dot(self, x, y):
        self.path.append([x, y])

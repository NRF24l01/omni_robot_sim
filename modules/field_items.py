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
    def __init__(self, dot_radius=10, dot_color="#fade91"):
        self.dot_radius = dot_radius
        self.color = dot_color

    def draw_dot(self, canvas: CTkCanvas, x: int, y: int, fcolor: str=None):
        if not fcolor: fcolor = self.color
        x1 = x - self.dot_radius / 2
        x2 = x + self.dot_radius / 2
        y1 = y - self.dot_radius / 2
        y2 = y + self.dot_radius / 2
        canvas.create_oval(x1, y1, x2, y2, outline=fcolor, fill=fcolor)

    def draw_outline(self, canvas: CTkCanvas, x: int, y: int, ocolor: str=None):
        if not ocolor: ocolor = self.color
        x1 = x - self.dot_radius / 2
        x2 = x + self.dot_radius / 2
        y1 = y - self.dot_radius / 2
        y2 = y + self.dot_radius / 2
        canvas.create_oval(x1, y1, x2, y2, outline=ocolor)


class Path(Dot):
    def __init__(self, statr_point: tuple=None, path=None, dot_radius=10, dot_color="#fade91"):
        """

        :param statr_point: Tuple with x and y start points
        :param path: Path, list with dots, dot is list with x and y coordinates
        :param dot_radius: Dot radius in px
        :param dot_colors: Dot colors, tuple
        """
        super().__init__(dot_radius, dot_color)

        if path is None:
            path = []
        self.start_point = statr_point
        self.path = path

    def draw(self, canvas: CTkCanvas):
        if self.start_point:
            self.draw_dot(canvas, self.start_point[0], self.start_point[1])
            px, py = self.start_point[0], self.start_point[1]
            for dot in self.path:
                canvas.create_line(px, py, dot[0], dot[1])
                px, py = dot[0], dot[1]
                self.draw_dot(canvas, dot[0], dot[1])

    def add_point(self, x, y):
        self.path.append([x, y])

    def set_start_point(self, x, y):
        self.start_point = (x, y)

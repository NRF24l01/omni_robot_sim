from PIL import Image, ImageTk


class Item:
    def resize(self, image: str, width: int, height: int):
        return Image.open(image).resize((width, height), Image.LANCZOS)


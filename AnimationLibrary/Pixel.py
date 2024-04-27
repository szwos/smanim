class Pixel():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

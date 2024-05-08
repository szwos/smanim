class Pixel():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __repr__(self):
        return f"(Pixel: x: {self.x}, y: {self.y}, color: ())"
        # TODO: return f"(Pixel: x: {self.x}, y: {self.y}, color: (TODO: color repr))"

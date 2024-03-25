
#TODO: Qol overrides (e.g. taking tuples, tables instead of other objects for construction)

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color

class Rect():
    """
    @args:
    A - top left corner of the rectangle
    B - bottom right corner of the rectangle
    """
    #TODO: in current implementation A Point is useless, because rectangle is always describing it's internal coordinates, hence we can cope with width height described in B Point
    #TODO: default position
    def __init__(self, A: Point, B: Point, color: Color = Color(0, 0, 0, 255), position: Point = Point(0, 0)) -> None:
        self.A = A
        self.B = B

        self.position = position

        self.color = color

    def rasterize(self):

        pixels = []

        for i in range(self.B.y): #TODO: i don't like swapping y with x here, but i was getting index out of range, like it should be swapped idk
            for j in range(self.B.x):
                pixels.append(Pixel(i + self.position.x, j + self.position.y, self.color)) # TODO: take color from somewhere

        return pixels

    # def __iter__(self):
    #     self.i = 0
    #     self.j = 0
    #     return self
    #
    # def __next__(self):
    #     if self.j >= self.B.y:
    #         raise StopIteration
    #
    #     pixel = self.pixels[self.i][self.j]
    #     self.i += 1
    #     if self.i >= self.B.x:
    #         self.i = 0
    #         self.j += 1
    #     return pixel



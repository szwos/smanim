import math

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.drawable.Rect import Rect
from typing import Callable
from AnimationLibrary.drawable.DrawableObject import DrawableObject
from AnimationLibrary.Animation import Animation

class Circle(DrawableObject):
    """
    @args:natur
    center - a Point in the center of the circle
    r - Radius of the circle
    position - offset of shape's rect top left point from Point(0, 0), default is Point(0, 0)
    """
    
    def __init__(self, r: float, animation: Animation, color: Color = Color(25, 25, 225),
                 path: Callable[[float], float] = None, position: Point = Point(0, 0), parent: DrawableObject = None):


        super().__init__(animation, position, color, path, parent)
        self.radius = r

        #position is ALWAYS top left of rect describing the shape
        self.position = position

        self.color = color

        #TODO: calculate rect with radius, use it for drawing
        self.rect = Rect(Point(0, 0), Point(2 * r, 2 * r))

        self.center = Point(self.rect.A.x + r/2, self.rect.A.y + r/2)



    def rasterize(self):

        pixels = []

        # TODO: explore better ways to do this: e.g. Midpoint Circle Algorithm
        for i in range(self.rect.B.x):
            for j in range(self.rect.B.y):
                distance_from_center = math.sqrt((self.radius - i) ** 2 + (self.radius - j) ** 2)
                if distance_from_center < self.radius:
                    pixels.append(Pixel(i, j, self.color))

        return pixels

    # def __iter__(self):
    #     self.i = 0
    #     self.j = 0
    #     return self
    #
    # def __next__(self):
    #     if self.j >= self.rect.B.y:
    #         raise StopIteration
    #
    #     pixel = self.pixels[self.i][self.j]
    #     self.i += 1
    #     if self.i >= self.rect.B.x:
    #         self.i = 0
    #         self.j += 1
    #
    #     if pixel == 0:
    #         return self.__next__()
    #     else:
    #         return pixel



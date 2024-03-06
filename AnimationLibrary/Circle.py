import math

from .Pixel import Pixel
from .Point import Point
from .Color import Color
from .Rect import Rect

# TODO: use Rect class as base rectangle for this sprite, it will be needed in calculations
# TODO: make some kind of interface or smth, that will implement this Rectangle base for all
# TODO: objects

class Circle():
    """
    @args:natur
    center - a Point in the center of the circle
    r - Radius of the circle
    position - offset of shape's rect top left point from Point(0, 0), default is Point(0, 0)
    """
    
    def __init__(self, r: float, position: Point = Point(0, 0)) -> None:
        # this should be handled by base class (super() ??)
        self.r = r

        #position is ALWAYS top left of rect describing the shape
        self.position = position


        #TODO: calculate rect with radius, use it for drawing
        self.rect = Rect(Point(0, 0), Point(2 * r, 2 * r))

        self.center = Point(self.rect.A.x + r/2, self.rect.A.y + r/2)

        self.pixels = [[0] * self.rect.B.x for i in range(self.rect.B.y)]
        self.pixels = [[Pixel(i, j, Color(0, 0, 0, 0)) for j in range(self.rect.B.x)] for i in range(self.rect.B.y)]

        # TODO: explore better ways to do this: e.g. Midpoint Circle Algorithm
        for i in range(self.rect.B.x):
            for j in range(self.rect.B.y):
                distance_from_center = math.sqrt((r - i)**2 + (r - j)**2)
                if distance_from_center < r:
                    self.pixels[i][j] = Pixel(i, j, Color(25, 25, 225))  # TODO: take color from somewhere
                else:
                    self.pixels[i][j] = 0
                    #self.pixels[i][j] = Pixel(i, j, Color(255, 255, 255, 0))
                    #print(self.pixels[i][j].color.a)

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.j >= self.rect.B.y:
            raise StopIteration

        pixel = self.pixels[self.i][self.j]
        self.i += 1
        if self.i >= self.rect.B.x:
            self.i = 0
            self.j += 1

        if pixel == 0:
            return self.__next__()
        else:
            return pixel



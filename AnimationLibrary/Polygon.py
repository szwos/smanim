import math

from .Pixel import Pixel
from .Point import Point
from .Color import Color
from .Rect import Rect
from .Line import Line

class Polygon():

    def __init__(self, vertices: list[Point], position: Point = Point(0, 0), color: Color = Color(0, 0, 0, 255)) -> None:

        self.vertices = vertices
        # position is ALWAYS top left of rect describing the shape
        self.position = position
        self.color = color


        r_A_x = min([p.x for p in vertices])
        r_A_y = min([p.y for p in vertices])
        r_B_x = max([p.x for p in vertices])
        r_B_y = max([p.y for p in vertices])

        r_B_x = r_B_x - r_A_x
        r_B_y = r_B_y - r_A_y
        r_A_x = r_A_x - r_A_x
        r_A_y = r_A_y - r_A_y


        self.rect = Rect(Point(r_A_x, r_A_y), Point(r_B_x, r_B_y))

        self.pixels = [[0] * self.rect.B.x for i in range(self.rect.B.y)]
        self.pixels = \
            [[Pixel(i, j, Color(0, 0, 0, 0)) for j in range(self.rect.B.x)] for i in range(self.rect.B.y)]

        # TODO: explore better ways to do this: e.g. Midpoint Circle Algorithm
        for i in range(self.rect.B.x):
            for j in range(self.rect.B.y):

                if True:
                    self.pixels[i][j] = Pixel(i, j, color)
                else:
                    self.pixels[i][j] = 0

    def rasterize(self):

        #TODO : if len(self.vertices == 1: raise exception or smth, idk handle this case it should not be

        sides = []
        for i in range(len(self.vertices) - 1):
            sides.append(Line(self.vertices[i], self.vertices[i + 1]))

        sides.append(Line(self.vertices[len(self.vertices) - 1], self.vertices[0]))

        for i in range(self.rect.B.x):
            for j in range(self.rect.B.y):

                if True:
                    self.pixels[i][j] = Pixel(i, j, color)
                else:
                    self.pixels[i][j] = 0




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



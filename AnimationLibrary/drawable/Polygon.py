from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.drawable.Rect import Rect
from AnimationLibrary.drawable.Line import Line
from AnimationLibrary.Animation import Animation
from typing import Callable
from AnimationLibrary.drawable.DrawableObject import DrawableObject
class Polygon(DrawableObject):

    def __init__(self, vertices: list[Point], animation: Animation, position: Point = Point(0, 0),
                 color: Color = Color(0, 0, 0, 255), path: Callable[[float], float] = None, parent: DrawableObject = None):

        super().__init__(animation, position, color, path, parent)

        self.vertices = vertices
        # position is ALWAYS top left of rect describing the shape
        self.position = position
        self.color = color

        #animation ref is kept for use in Line constructor
        self.animation = animation


        r_A_x = min([p.x for p in vertices])
        r_A_y = min([p.y for p in vertices])
        r_B_x = max([p.x for p in vertices])
        r_B_y = max([p.y for p in vertices])

        r_B_x = r_B_x - r_A_x
        r_B_y = r_B_y - r_A_y
        r_A_x = r_A_x - r_A_x
        r_A_y = r_A_y - r_A_y


        self.dimensions = Rect(Point(r_A_x, r_A_y), Point(r_B_x, r_B_y))

    def rasterize(self):

        #TODO : if len(self.vertices == 1: raise exception or smth

        sides = []
        pixels = []
        for i in range(len(self.vertices) - 1):
            sides.append(Line(self.vertices[i], self.vertices[i + 1], animation=self.animation, parent=self))

        for side in sides:
            for pixel in side.rasterize():
                pixels.append(pixel + side.position)

        return pixels


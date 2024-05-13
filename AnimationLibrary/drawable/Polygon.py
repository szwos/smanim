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
                 color: Color = Color(0, 0, 0, 255), path: Callable[[int], Point] = None, parent: DrawableObject = None):

        super().__init__(animation, position, color, path, parent)

        self.vertices = vertices
        # position is ALWAYS top left of rect describing the shape
        self.position = position
        self.color = color

        #animation ref is kept for use in Line constructor
        self.animation = animation

        self.sides = []

        displacement_x = min([v.x for v in vertices])
        displacement_y = min([v.y for v in vertices])

        self.displacement = Point(displacement_x, displacement_y)

        for i in range(len(self.vertices) - 1):
            line = Line(vertices[i+1] - vertices[i], animation=animation, parent=self, position=vertices[i] - self.displacement, path=self.path)
            self.sides.append(line)

        last_line = Line(vertices[0] - vertices[len(self.vertices) - 1], animation=animation, parent=self, position=vertices[len(self.vertices) - 1] - self.displacement)
        self.sides.append(last_line)

        pass

    def rasterize(self):
        # do nothing (sides rasterize themselves, bcs they are placed on tree)
        return []

        # #TODO : if len(self.vertices == 1: raise exception or smth
        # pixels = []
        #
        # for n, side in enumerate(self.sides):
        #     for pixel in side.rasterize():
        #         #print(f"side: {n}, pixel: {pixel}, position: {side.position}")
        #         pixels.append(pixel + self.position)
        #
        #
        # return pixels


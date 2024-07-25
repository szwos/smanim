
#TODO: Qol overrides (e.g. taking tuples, tables instead of other objects for construction)

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.Animation import Animation
from typing import Callable
from AnimationLibrary.drawable.DrawableObject import DrawableObject

class Rect(DrawableObject):
    """
    @args:
    A - top left corner of the rectangle
    B - bottom right corner of the rectangle
    """
    #TODO: in current implementation A Point is useless, because rectangle is always describing it's internal coordinates, hence we can cope with width height described in B Point
    #TODO: default position
    #TODO: get rid of A point
    def __init__(self, B: Point, animation: Animation = None, position: Point = Point(0, 0),
                 color: Color = Color(0, 0, 0, 255), path: Callable[[float], float] = None, parent: 'DrawableObject' = None):
        super().__init__(animation, position, color, path, parent)

        self.B = B

        self.position = position

        self.color = color

    def rasterize(self):

        pixels = []

        for i in range(self.B.x):
            for j in range(self.B.y):
                pixels.append(Pixel(i, j, self.color))

        return pixels


import math

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
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
                path: Callable[[int], Point] = None, position: Point = Point(0, 0), parent: DrawableObject = None, name: str = ""):

        self.name = name

        super().__init__(animation, position, color, path, parent)
        self.radius = r

        #position is ALWAYS top left of rect describing the shape
        self.position = position

        self.color = color

        self.dimensions = Point(2 * r, 2 * r)

        self.center = Point(r/2, r/2)



    def rasterize(self):

        pixels = []

        # TODO: explore better ways to do this: e.g. Midpoint Circle Algorithm
        for i in range(self.dimensions.x):
            for j in range(self.dimensions.y):
                distance_from_center = math.sqrt((self.radius - i) ** 2 + (self.radius - j) ** 2)
                if distance_from_center < self.radius:
                    pixels.append(Pixel(i, j, self.color))

        return pixels

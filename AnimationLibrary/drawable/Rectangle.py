from AnimationLibrary.drawable.Polygon import Polygon
from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.Animation import Animation
from typing import Callable

class Rectangle(Polygon):

    def __init__(self, B: Point, animation: Animation = None, position: Point = Point(0, 0),
                 color: Color = Color(30, 30, 230, 255), path: Callable[[float], float] = None,
                 parent: 'DrawableObject' = None):

        vertices = [Point(0, 0), Point(B.x, 0), Point(B.x, B.y), Point(0, B.y)]
        super().__init__(vertices, animation, position, color, path, parent)

        self.width = B.x
        self.height = B.y

        self.fill_seed = Pixel(int(self.width / 2), int(self.height / 2), color=color)



    # def transform(self, t: int):
    #     return Point(0, 0)
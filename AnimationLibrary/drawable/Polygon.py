from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.drawable.Rect import Rect
from AnimationLibrary.drawable.Line import Line
from AnimationLibrary.Animation import Animation
from typing import Callable
from AnimationLibrary.drawable.DrawableObject import DrawableObject
from AnimationLibrary.algorithms.FloodFill import FloodFill
import math

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
            line = Line(vertices[i+1] - vertices[i], animation=None, parent=self, position=vertices[i] - self.displacement)
            self.sides.append(line)

        last_line = Line(vertices[0] - vertices[len(self.vertices) - 1], animation=None, parent=self, position=vertices[len(self.vertices) - 1] - self.displacement)
        self.sides.append(last_line)

        pass

    def rasterize(self):
        pixels = []

        for side in self.sides:
            for pixel in side.rasterize():
                pixels.append(pixel + side.position)

        width = int(max([math.fabs(v.x) + math.fabs(self.displacement.x) for v in self.vertices]))
        height = int(max([math.fabs(v.y) + math.fabs(self.displacement.y) for v in self.vertices]))

        frame = [[None for _ in range(height + 1)] for _ in range(width + 1)]

        for p in pixels:
            frame[p.x][p.y] = p.color

        fill_seed = Point(int(width / 2), int(height / 2))

        frame = FloodFill.fill(frame, width, height, fill_seed, self.color)

        # TODO: this could propably be optimised to avoid copying pixels
        colored_pixels = []
        for x in range(width):
            for y in range(height):
                if frame[x][y] is not None:
                    colored_pixels.append(Pixel(x, y, frame[x][y]))

        return colored_pixels

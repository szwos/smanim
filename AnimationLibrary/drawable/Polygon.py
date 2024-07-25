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
from AnimationLibrary.Serializer import Serializer
class Polygon(DrawableObject):

    def __init__(self, vertices: list[Point], animation: Animation, position: Point = Point(0, 0),
                 color: Color = Color(0, 0, 0, 255), path: Callable[[int], Point] = None,
                 parent: DrawableObject = None, fill_seed: Point = None, scale: Callable[[int], float] = lambda t: 1,
                 rotation_angle: Callable[[int], float] = lambda t: 0, rotation_pivot: Point = Point(0, 0)):

        super().__init__(animation, position, color, path, parent)

        self.vertices = vertices
        # position is ALWAYS top left of rect describing the shape
        self.position = position
        self.color = color
        self.fill_seed = fill_seed
        self.scale = scale # todo: scale time function instead
        self.rotation_angle = rotation_angle
        self.rotation_pivot = rotation_pivot

        #animation ref is kept for use in Line constructor
        self.animation = animation

    def rasterize(self):
        pixels = []

        for side in self.sides:
            for pixel in side.rasterize():
                pixels.append(pixel + side.position)

        width = int(max([v.x - self.displacement.x for v in self.vertices])) + 1
        height = int(max([v.y - self.displacement.y for v in self.vertices])) + 1

        frame = [[None for _ in range(height)] for _ in range(width)]

        for p in pixels:
            frame[p.x][p.y] = p.color

        if self.fill_seed is None:
            self.fill_seed = Point(int(width / 2), int(height / 2))

        frame = FloodFill.fill(frame, width, height, self.fill_seed, self.color)

        # TODO: this could propably be optimised to avoid copying pixels
        colored_pixels = []
        for x in range(width):
            for y in range(height):
                if frame[x][y] is not None:
                    colored_pixels.append(Pixel(x, y, frame[x][y]))

        return colored_pixels

    def rasterize(self, t: int):

        scale = self.scale
        rotation_angle = self.rotation_angle
        transform = self.transform(t)

        for obj in self.ancestors_to_root():
            transform = transform + obj.transform(t)

        sides = []
        vertices = []

        for v in self.vertices:
            vertices.append(Point(v.x, v.y))


        # # apply displacement (NOT TRANSFORM)
        # for v in vertices:
        #     v.x = v.x - displacement_x # "-" ??
        #     v.y = v.y - displacement_y
        #     v.x = int(v.x)
        #     v.y = int(v.y)

        # apply scale
        for v in vertices:
            v.x = v.x * scale(t)
            v.y = v.y * scale(t)
            v.x = int(v.x)
            v.y = int(v.y)

        # apply rotation:
        for v in vertices:
            x_rotated = ((v.x + self.rotation_pivot.x) * math.cos(rotation_angle(t) * 0.0174532925)
                         + (v.y + self.rotation_pivot.y) * math.sin(rotation_angle(t) * 0.0174532925))
            y_rotated = ((v.y + self.rotation_pivot.y) * math.cos(rotation_angle(t) * 0.0174532925)
                         - (v.x + self.rotation_pivot.x) * math.sin(rotation_angle(t) * 0.0174532925))
            v.x = int(x_rotated)
            v.y = int(y_rotated)


        displacement_x = min([v.x for v in vertices])
        displacement_y = min([v.y for v in vertices])

        # create sides
        for i in range(len(vertices) - 1):
            line = Line(vertices[i+1] - vertices[i], animation=None, parent=self, position=vertices[i])
            sides.append(line)

        last_line = Line(vertices[0] - vertices[len(vertices) - 1], animation=None, parent=self, position=vertices[len(vertices) - 1])
        sides.append(last_line)

        #sides_debug = [(side.position, side.B) for side in sides]

        # rasterize
        pixels = []

        for k, side in enumerate(sides):
            for pixel in side.rasterize():
                #pixels.append(pixel - Point(displacement_x, displacement_y) + side.position)
                pixels.append(pixel + side.position)

        # bring pixels to positive quadrant, then move back by pivot
        min_x = min([v.x for v in vertices])
        min_y = min([v.y for v in vertices])

        for p in pixels:
            p.x = p.x - min_x
            p.y = p.y - min_y

        transform = transform + Point(min_x, min_y)

        # apply pivot to transform
        transform = transform + self.rotation_pivot

        # TODO: sprawdz czy pivot dziala dobrze

        Serializer.save_pixels("test/imgs/polaczone", pixels)

        #width = int(max([v.x - displacement_x for v in vertices])) + 1
        #height = int(max([v.y - displacement_y for v in vertices])) + 1
        width = max([p.x for p in pixels]) + 1
        height = max(p.y for p in pixels) + 1

        frame = [[None for _ in range(height)] for _ in range(width)]

        pass
        for p in pixels:
            frame[p.x][p.y] = p.color

        Serializer.save_frame("test/imgs/przepisane", frame)

        #TODO: this NEEDS to be upgraded # take first pixel, that is inside the shape
        if self.fill_seed is None:
            fill_seed = Point(int(width / 2), int(height / 2))
        else:
            fill_seed = self.fill_seed

        frame = FloodFill.fill(frame, width, height, fill_seed, self.color)

        Serializer.save_frame("test/imgs/colored", frame)


        # transform
        colored_and_displaced_pixels = []
        for x in range(width):
            for y in range(height):
                if frame[x][y] is not None:
                    colored_and_displaced_pixels.append(Pixel(x + transform.x, y + transform.y, frame[x][y]))

        return colored_and_displaced_pixels

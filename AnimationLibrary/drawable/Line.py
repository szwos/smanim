import math

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from AnimationLibrary.drawable.DrawableObject import DrawableObject
from AnimationLibrary.Animation import Animation
from typing import Callable

#TODO: consider moving file scope methods from this file to some other context

def bresenham(B: Point):
    points = []

    dx = abs(B.x)
    dy = abs(B.y)

    P = 2 * dy - dx

    x_step = 1 if B.x >= 0 else -1
    y_step = 1 if B.y >= 0 else -1

    x, y = 0, 0
    points.append(Point(x, y))

    while x < dx:
        x += 1
        if P < 0:
            P += 2 * dy
        else:
            y += 1
            P += 2 * dy - 2 * dx
        points.append(Point(x * x_step, y * y_step))

    return points

def swapXWithY(P: Point):
    return Point(P.y, P.x)

def negate_x(B: Point):
    B_x = -B.x
    B_y = B.y

    return Point(B_x, B_y)

def negate_y(B: Point):
    B_x = B.x
    B_y = -B.y

    return Point(B_x, B_y)

def swap_x_with_y(B: Point):
    B_x = B.y
    B_y = B.x

    return Point(B_x, B_y)

def points_swap_x_with_y(points):
    reversed_points = []
    for p in points:
        reversed_points.append(Point(p.y, p.x))
    return reversed_points

# this negates x's WHICH MEANS IT NEGATES AROUND Y AXIS, not X axis!!!
def points_negate_x(points):
    negated_points = []
    for p in points:
        negated_points.append(Point(-p.x, p.y))
    return negated_points

def points_negate_y(points):
    negated_points = []
    for p in points:
        negated_points.append(Point(p.x, -p.y))
    return negated_points

def determine_octant(B: Point) -> int:

    if B.x >= 0:
        if B.y >= 0:
            if abs(B.x) >= abs(B.y):
                return 1
            else:
                return 2
        else:
            if abs(B.x) >= abs(B.y):
                return 8
            else:
                return 7
    else:
        if B.y >= 0:
            if abs(B.x) >= abs(B.y):
                return 4
            else:
                return 3
        else:
            if abs(B.x) >= abs(B.y):
                return 5
            else:
                return 6

def transform_to_1st_octant(B: Point):

    octant = determine_octant(B)

    match octant:
        case 1:
            return B
        case 2:
            new_B = swap_x_with_y(B)
            return new_B
        case 3:
            new_B = negate_x(B)
            new_B = swap_x_with_y(new_B)
            return new_B
        case 4:
            new_B = negate_x(B)
            return new_B
        case 5:
            new_B = negate_y(B)
            new_B = negate_x(new_B)
            return new_B
        case 6:
            new_B = negate_y(B)
            new_B = negate_x(new_B)
            new_B = swap_x_with_y(new_B)
            return new_B
        case 7:
            new_B = negate_y(B)
            new_B = swap_x_with_y(new_B)
            return new_B
        case 8:
            new_B = negate_y(B)
            return new_B
def transform_from_1st_to_octant(points, octant: int):

    match octant:
        case 1:
            return points
        case 2:
            return points_swap_x_with_y(points)
        case 3:
            return points_negate_x(points_swap_x_with_y(points))
        case 4:
            return points_negate_x(points)
        case 5:
            return points_negate_y(points_negate_x(points))
        case 6:
            return points_swap_x_with_y(points_negate_y(points_negate_x(points)))
        case 7:
            return points_negate_y(points_swap_x_with_y(points))
        case 8:
            return points_negate_y(points)

class Line(DrawableObject):
    """
        @args
        A - starting point of the line
        B - end point of the line
        position - offset of shape's rect top left point from Point(0, 0), default is Point(0, 0)
    """

    # TODO: rename B
    def __init__(self, B: Point, animation: Animation, position: Point = Point(0, 0),
                 color: Color = Color(0, 0, 0, 255), path: Callable[[float], float] = None, parent: 'DrawableObject' = None):

        super().__init__(animation, position, color, path, parent)
        self.B = B

        self.color = color
        self.position = position

    def rasterize(self):

        # część 1 - przerobienie linii do takiej żeby działało (do 1 oktetu, z punktem poczatkowym w lewym górnym)
        B = transform_to_1st_octant(self.B)

        # cześć 2 - puszczenie algorytmu, on wypluwa array pixeli
        points = bresenham(B)

        #część 3 - przetransformowanie tego arraya pixeli, tą samą tranformacją, co wczesniej została przetransformowana linia
        octant = determine_octant(self.B)
        points = transform_from_1st_to_octant(points, octant)

        # część 4 - nadanie otrzymanym punktom koloru (zamienienie je w Pixele) oraz uwzglednienie pozycji
        pixels = []
        for point in points:
            pixels.append(Pixel(point.x, point.y, self.color))

        return pixels


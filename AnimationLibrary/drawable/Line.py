import math

from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color

#TODO: consider moving file scope methods from this file to some other context

def bresenham(A: Point, B: Point):
    x = A.x
    y = A.y

    dx = B.x - A.x
    dy = B.y - A.y

    P = 2 * dx - dy

    points = []
    while x <= B.x:
        points.append(Point(x, y))
        x += 1

        if P < 0:
            P = P + dy
        else:
            P = P + 2 * dy - 2 * dx
            y += 1

    return points

def swapXWithY(P: Point):
    return Point(P.y, P.x)

def negate_x(A: Point, B: Point):
    A_x = -A.x
    A_y = A.y

    B_x = -B.x
    B_y = B.y

    return Point(A_x, A_y), Point(B_x, B_y)

def negate_y(A: Point, B: Point):
    A_x = A.x
    A_y = -A.y

    B_x = B.x
    B_y = -B.y

    return Point(A_x, A_y), Point(B_x, B_y)

def swap_x_with_y(A: Point, B: Point):
    A_x = A.y
    A_y = A.x

    B_x = B.y
    B_y = B.x

    return Point(A_x, A_y), Point(B_x, B_y)

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

def determine_octant(A: Point, B: Point) -> int:

    dx = B.x - A.x
    dy = B.y - A.y

    if dx >= 0:
        if dy >= 0:
            if abs(dx) >= abs(dy):
                return 1
            else:
                return 2
        else:
            if abs(dx) >= abs(dy):
                return 8
            else:
                return 7
    else:
        if dy >= 0:
            if abs(dx) >= abs(dy):
                return 4
            else:
                return 3
        else:
            if abs(dx) >= abs(dy):
                return 5
            else:
                return 6

def transform_to_1st_octant(A: Point, B: Point):

    octant = determine_octant(A, B)

    match octant:
        case 1:
            return A, B
        case 2:
            new_A, new_B = swap_x_with_y(A, B)
            return  new_A, new_B
        case 3:
            new_A, new_B = negate_x(A, B)
            new_A, new_B = swap_x_with_y(new_A, new_B)
            return new_A, new_B
        case 4:
            new_A, new_B = negate_x(A, B)
            return new_A, new_B
        case 5:
            new_A, new_B = negate_y(A, B)
            new_A, new_B = negate_x(new_A, new_B)
            return new_A, new_B
        case 6:
            new_A, new_B = negate_y(A, B)
            new_A, new_B = negate_x(new_A, new_B)
            new_A, new_B = swap_x_with_y(new_A, new_B)
            return new_A, new_B
        case 7:
            new_A, new_B = negate_y(A, B)
            new_A, new_B = swap_x_with_y(new_A, new_B)
            return new_A, new_B
        case 8:
            new_A, new_B = negate_y(A, B)
            return new_A, new_B
def transform_from_1st_to_octant(points, octant: int):

    match octant:
        case 1:
            return points
        case 2:
            return points_swap_x_with_y(points)
        case 3:
            return points_swap_x_with_y(points_negate_x(points))
        case 4:
            return points_negate_x(points)
        case 5:
            return points_negate_y(points_negate_x(points))
        case 6:
            return points_swap_x_with_y(points_negate_y(points_negate_x(points)))
        case 7:
            return points_swap_x_with_y(points_negate_y(points))
        case 8:
            return points_negate_y(points)

class Line:
    """
        @args
        A - starting point of the line
        B - end point of the line
        position - offset of shape's rect top left point from Point(0, 0), default is Point(0, 0)
    """

    def __init__(self, A: Point, B: Point, position: Point = Point(0, 0), color: Color = Color(0, 0, 0, 255)):

        # TODO: self.A, self.B assignments were removed here, as they would be missleading because they are different from self.rect.A, self.rect.B, do this for other classes too
        # TODO: now i am bringing them back and removing self.rect
        self.A = A
        self.B = B

        self.color = color
        self.position = position

        pass

    def rasterize(self):

        # część 1 - przerobienie linii do takiej żeby działało (do 1 oktetu, z punktem poczatkowym w lewym górnym)

        A, B = transform_to_1st_octant(self.A, self.B)

        # cześć 2 - puszczenie algorytmu, on wypluwa array pixeli

        points = bresenham(A, B)

        #część 3 - przetransformowanie tego arraya pixeli, tą samą tranformacją, co wczesniej została przetransformowana linia

        octant = determine_octant(self.A, self.B)

        points = transform_from_1st_to_octant(points, octant)

        # część 4 - nadanie otrzymanym punktom koloru (zamienienie je w Pixele) oraz uwzglednienie pozycji

        pixels = []
        for point in points:
            pixels.append(Pixel(self.position.x + point.x, self.position.y + point.y, self.color))


        return pixels

    #TODO: __next__ and __iter__ will be reused

    # def __iter__(self):
    #     self.i = 0
    #     self.j = 0
    #     return self
    #
    # def __next__(self):
    #     if self.j >= self.rect.B.y:
    #         raise StopIteration
    #
    #     pixel = self.pixels[self.j][self.i]
    #     self.i += 1
    #     if self.i >= self.rect.B.x:
    #         self.i = 0
    #         self.j += 1
    #
    #     if pixel == 0:
    #         return self.__next__()
    #     else:
    #         return pixel

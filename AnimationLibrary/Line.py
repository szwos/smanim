import math

from .Pixel import Pixel
from .Point import Point
from .Color import Color
from .Rect import Rect


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

#after negating, points need to be moved back to 1'st quadrant (as everything is being calculated and displayed in 1'st quadrant), hence width variable
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



class Line():
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
        self.position = position #TODO: i think postion "could" be updated with

        # # TODO: remember that user might use A and B in a way, where A is in bottom right
        # # and B is top left (default should be A top left, B bottom right), handle this case smooothly
        #
        # r_A_x = min(A.x, B.x)
        # r_A_y = min(A.y, B.y)
        # r_B_x = max(A.x, B.x)
        # r_B_y = max(A.y, B.y)
        #
        # #translate A to 0, as is with other shapes
        # r_B_x = r_B_x - r_A_x
        # r_B_y = r_B_y - r_A_y
        #
        # self.rect = Rect(Point(0, 0), Point(r_B_x, r_B_y))
        #
        # self.rect = Rect(A, B)

        #TODO: something is wrong here, decide on how should this table be initiated correctly, debug, check and continue
        #self.pixels = [[0] * (self.rect.B.x + 1) for i in range(self.rect.B.y + 1)]

        #m = r_B_y / r_B_x

        # points = self.rasterize()
        #
        # for p in points:
        #     self.pixels[p.y][p.x] = Pixel(p.x + position.x, p.y + position.y, self.color)

        # for x in range(self.rect.B.x + 1):
        #     for y in range(self.rect.B.y + 1):
        #         #print(x, y)
        #         #if y == int(m * x):
        #             self.pixels[y][x] = Pixel(x, y, Color(255, 255, 50))
        #         else:
        #             self.pixels[y][x] = 0

        pass

    def determine_octant(self, A: Point, B: Point) -> int:

        dx = B.x - A.x
        dy = B.y - A.y

        # TODO: i'm 90% positive, this is wrong and messes up octants sometimes
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
    def transform_to_1st_octant(self, A: Point, B: Point): # TODO: static class or smth, there is no point in adding boilerplate by calling this function self.function() instead of jsut function()

        octant = self.determine_octant(A, B)

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

        return#???

        # if dx >= 0:
        #     if dy >= 0:
        #         if abs(dx) >= abs(dy):
        #             # 1st octant
        #             octant = 1
        #             return A, B, 1
        #         else:
        #             # 2nd octant
        #             octant = 2
        #             A = swapXWithY(A)
        #             B = swapXWithY(B)
        #
        #             return A, B, 2
        #
        #     else:
        #         if abs(dx) >= abs(dy):
        #             return 8
        #         else:
        #             return 7
        # else:
        #     if dy >= 0:
        #         if abs(dx) >= abs(dy):
        #             return 4
        #         else:
        #             # 3rd octant
        #             octant = 3
        #             A = Point(-A.y, A.x)    # TODO: when line is in this quadrant, either rasterization will break
        #             B = Point(-B.y, B.x)    # TODO: (bcs it's out of (0, +)(0, +) rect), or bresnham will break (not detect 3rd quadrant)
        #                                     # TODO: something must get changed, for now i'd shoot for changing rasterization, so that it manages
        #                                     # TODO: such a line, and leave lines 49, 63 commented out as it is now
        #             return A, B, 3
        #     else:
        #         if abs(dx) >= abs(dy):
        #             return 5
        #         else:
        #             return 6




    def rasterize(self):

        # część 1 - przerobienie linii do takiej żeby działało (do 1 oktetu, z punktem poczatkowym w lewym górnym)

        #A, B, octant = self.transform_to_1st_octant(self.A, self.B)
        A, B = self.transform_to_1st_octant(self.A, self.B)

        # cześć 2 - puszczenie algorytmu, on wypluwa array pixeli

        points = bresenham(A, B)

        #część 3 - przetransformowanie tego arraya pixeli, tą samą tranformacją, co wczesniej została przetransformowana linia

        octant = self.determine_octant(self.A, self.B)

        match octant:
            case 1:
                pass
            case 2:
                points = points_swap_x_with_y(points)
            case 3:
                points = points_swap_x_with_y(points_negate_x(points))
            case 4:
                points = points_negate_x(points)
            case 5:
                points = points_negate_y(points_negate_x(points))
            case 6:
                points = points_swap_x_with_y(points_negate_y(points_negate_x(points)))
            case 7:
                points = points_swap_x_with_y(points_negate_y(points))
            case 8:
                points = points_negate_y(points)

        # część 4 - nadanie otrzymanym punktom koloru (zamienienie je w Pixele) oraz uwzglednienie pozycji


        pixels = []
        for point in points:
            pixels.append(Pixel(self.position.x + point.x, self.position.y + point.y, self.color))


        return pixels

    def rasterized(self): # TODO: decide on a name, rasaterize or rasterized
        return self.rasterize()

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

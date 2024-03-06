import math

from .Pixel import Pixel
from .Point import Point
from .Color import Color
from .Rect  import Rect


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


class Line():
    """
        @args
        A - starting point of the line
        B - end point of the line
        position - offset of shape's rect top left point from Point(0, 0), default is Point(0, 0)
    """

    def __init__(self, A: Point, B: Point, position: Point = Point(0, 0), color: Color = Color(0, 0, 0, 255)):

        # TODO: self.A, self.B assignments were removed here, as they would be missleading because they are different from self.rect.A, self.rect.B, do this for other classes too
        self.color = color
        self.position = position #TODO: i think postion "could" be updated with initial value of A, as it's being

        # TODO: remember that user might use A and B in a way, where A is in bottom right
        # and B is top left (default should be A top left, B bottom right), handle this case smooothly

        r_A_x = min(A.x, B.x)
        r_A_y = min(A.y, B.y)
        r_B_x = max(A.x, B.x)
        r_B_y = max(A.y, B.y)

        #translate A to 0, as is with other shapes
        r_B_x = r_B_x - r_A_x
        r_B_y = r_B_y - r_A_y

        self.rect = Rect(Point(0, 0), Point(r_B_x, r_B_y))

        #TODO: something is wrong here, decide on how should this table be initiated correctly, debug, check and continue
        self.pixels = [[0] * (self.rect.B.x + 1) for i in range(self.rect.B.y + 1)]

        m = r_B_y / r_B_x

        points = self.rasterize()

        for p in points:
            self.pixels[p.y][p.x] = Pixel(p.x, p.y, self.color)

        # for x in range(self.rect.B.x + 1):
        #     for y in range(self.rect.B.y + 1):
        #         #print(x, y)
        #         #if y == int(m * x):
        #             self.pixels[y][x] = Pixel(x, y, Color(255, 255, 50))
        #         else:
        #             self.pixels[y][x] = 0

        pass



    def rasterize(self):

        # część 1 - przerobienie linii do takiej żeby działało (do 1 oktetu, z punktem poczatkowym w lewym górnym)

        A = Point(self.rect.A.x, self.rect.A.y)
        B = Point(self.rect.B.x, self.rect.B.y)

        dx = B.x - A.x
        dy = B.y - A.y

        if dx >= 0:
            if dy >= 0:
                if abs(dx) >= abs(dy):
                    # 1st octant
                    # TODO: do nothing
                    pass
                else:
                    # 2nd octant
                    A = swapXWithY(A)
                    B = swapXWithY(B)

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



        # cześć 2 - puszczenie algorytmu, on wypluwa array pixeli


        points = bresenham(A, B)
        #część 3 - przetransformowanie tego arraya pixeli, tą samą tranformacją, co wczesniej została przetransformowana linia



        # TODO : now do this, bcs line 71 is crashing


    def __iter__(self):
        self.i = 0
        self.j = 0
        return self

    def __next__(self):
        if self.j >= self.rect.B.y:
            raise StopIteration

        pixel = self.pixels[self.j][self.i]
        self.i += 1
        if self.i >= self.rect.B.x:
            self.i = 0
            self.j += 1

        if pixel == 0:
            return self.__next__()
        else:
            return pixel

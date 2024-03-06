from .Point import Point
import math
class Path():

    def __init__(self, timePeriod):
        self.points = []
        self.timePeriod = timePeriod #total number of all frames, the path will be divided into

    def add(self, point: Point):
        self.points.append(point)

    #time - t here is a step of interpolation / frame of animation
    def asTimeFunction(self, t):
        a = self.points[0]
        b = self.points[1]

        distance = (math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2))

        dt = t * distance / self.timePeriod

        x = (1 - dt) * a.x + dt * b.x
        y = (1 - dt) * a.y + dt * b.y

        return Point(x, y)



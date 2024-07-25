from AnimationLibrary.Point import Point
import math

class LinearMotion:
    def __init__(self, x0, y0, vx0, vy0, ax, ay):
        self.x0 = x0
        self.y0 = y0
        self.vx0 = vx0
        self.vy0 = vy0
        self.ax = ax
        self.ay = ay

    def function(self, t):
        return Point(self.x0 + self.vx0 * t + (self.ax * t * t) / 2, self.y0 + self.vy0 * t + (self.ay * t * t) / 2)


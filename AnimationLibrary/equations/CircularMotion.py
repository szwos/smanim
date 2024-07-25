from AnimationLibrary.Point import Point
import math

# TODO: some docs to let user see what exact equation is used
class CircularMotion:
    def __init__(self, radius: float, x0: float = 0, y0: float = 0, omega: float = 1, alpha: float = 0):
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.omega = omega
        self.alpha = alpha

    def function(self, t):
        return Point(self.x0 + self.radius * (math.cos(self.omega * t + self.alpha)),
                     self.y0 + self.radius * (math.sin(self.omega * t + self.alpha)))

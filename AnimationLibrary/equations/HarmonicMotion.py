from AnimationLibrary.Point import Point
import math

class HarmonicMotion:
    def __init__(self, x0: float, y0: float, omega: float = 1, phi: float = 0):
        self.x0 = x0
        self.y0 = y0
        self.omega = omega
        self.phi = phi


    def function(self, t):
        return Point(self.x0 * math.sin(self.omega * t + self.phi), self.y0 * math.sin(self.omega * t + self.phi))


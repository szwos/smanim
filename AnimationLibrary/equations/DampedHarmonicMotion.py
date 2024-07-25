from AnimationLibrary.Point import Point
import math

class DampedHarmonicMotion:
    def __init__(self, x0: float, y0: float, damping_factor_x: float, damping_factor_y: float, omega: float = 1, phi: float = 0):
        self.x0 = x0
        self.y0 = y0
        self.omega = omega
        self.phi = phi
        self.damping_factor_x = damping_factor_x
        self.damping_factor_y = damping_factor_y


    def function(self, t):
        return Point(self.x0 * math.e**(-self.damping_factor_x * t) * math.sin(self.omega * t + self.phi),
                     self.y0 * math.e**(-self.damping_factor_y * t) * math.sin(self.omega * t + self.phi))


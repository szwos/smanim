import math

from AnimationLibrary import *

anim = Animation(360, Canvas(200, 200))

def scale_function(t: int):
    return 1 + float(t) / 10

def rotation_function(t: int):
    return ((math.pi / 8) * 8.1) * t


#vertices = [Point(0, 0), Point(10, 10), Point(10, 20), Point(0, 30), Point(-10, 20), Point(-10, 10)]
#polygon = Polygon(vertices, anim, Point(50, 50), Color(255, 69, 0), scale=-1, rotation_angle=(math.pi / 8) * 8.1, path=HarmonicMotion(20, 10, 1, 0).function)
#polygon = Polygon(vertices, anim, Point(50, 50), Color(255, 69, 0), scale=scale_function, rotation_angle=rotation_function, path=HarmonicMotion(20, 10, 1, 0).function)

vertices2 = [Point(0, 0), Point(10, 0), Point(10, 20)]
polygon2 = Polygon(vertices2, anim, Point(100, 100), rotation_angle=rotation_function)

Serializer.save("test/scale_testing.gif", anim)
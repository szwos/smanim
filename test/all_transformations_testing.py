from AnimationLibrary import *
import math

def rotation_function(t: int):
    return ((math.pi / 8) * 8.1) * t

def scale_function(t: int):
    return 1 + float(t) / 5


animation = Animation(60, Canvas(500, 500))

vertices2 = [Point(0, 0), Point(10, 0), Point(10, 20)]
polygon2 = Polygon(vertices2, animation, Point(50, 50), rotation_angle=rotation_function, scale = scale_function, path=LinearMotion(0, 0, 0, 1, 1, 1).function, color=Color(25, 255, 25))


Serializer.save("test/all_transformations_testing.gif", animation)


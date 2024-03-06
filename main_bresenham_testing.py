import math

from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

canvas = Canvas(300, 300)

objects = []


# pointA = Point(0, 0)
# pointB = Point(10, 100)
# line = Line(pointA, pointB)
# objects.append(line)
#
#
# # 1st octant
# pointA = Point(0, 0)
# pointB = Point(100, 10)
# line = Line(pointA, pointB, Point(150, 150))
# objects.append(line)
#
# # 2nd octant
# pointA = Point(0, 0)
# pointB = Point(10, 100)
# line = Line(pointA, pointB, Point(150, 150))
# objects.append(line)

# 3rd octant
pointA = Point(0, 0)
pointB = Point(-10, 100)
line = Line(pointA, pointB, Point(150, 150))
objects.append(line)







# tworzenie obiektu animacji
animation = Animation(100, canvas, Color(25, 25, 100))

for o in objects:
    animation.add(copy.copy(o))

Serializer.save("test_bresenham.gif", animation)


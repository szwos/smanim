import math

from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

canvas = Canvas(300, 300)

# tworzenie obiektu animacji
animation = Animation(10, canvas, Color(25, 25, 100))

# pointA = Point(0, 0)
# pointB = Point(10, 100)
# line = Line(pointA, pointB)
# objects.append(line)


# # 1st octant
# pointB1 = Point(100, 50)
# line1 = Line(pointB1, position=Point(150, 150), animation=animation)
#
# # 2nd octant
# pointB2 = Point(50, 100)
# line2 = Line(pointB2, position=Point(150, 150), animation=animation)
#
# # 3rd octant
# pointB3 = Point(-50, 100)
# line3 = Line(pointB3, position=Point(150, 150), animation=animation)
#
# # 4th octant
# pointB4 = Point(-100, 50)
# line4 = Line(pointB4, position=Point(150, 150), animation=animation)
#
# # 5th octant
# pointB5 = Point(-100, -50)
# line5 = Line(pointB5, position=Point(150, 150), animation=animation)

# 6th octant
pointB6 = Point(-50, -100)
line6 = Line(pointB6, position=Point(150, 150), animation=animation)

# # 7th octant
# pointB7 = Point(50, -100)
# line7 = Line(pointB7, position=Point(150, 150), animation=animation)
#
# # 8th octant
# pointB8 = Point(100, -50)
# line8 = Line(pointB8, position=Point(150, 150), animation=animation)

Serializer.save("test/test_bresenham.gif", animation)


import math

from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

canvas = Canvas(300, 300)

pointA = Point(0, 0)
pointB = Point(10, 100)

line = Line(pointA, pointB)


# tworzenie obiektu animacji
animation = Animation(100, canvas, Color(25, 25, 100))

animation.add(copy.copy(line))

Serializer.save("test_bresenham.gif", animation)


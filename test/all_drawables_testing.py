import math

from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

canvas = Canvas(300, 300)

objects = []

# # 1st octant
pointA = Point(0, 0)
pointB = Point(100, 50)
line = Line(pointA, pointB, Point(150, 150))
objects.append(line)

circle = Circle(25, position=Point(100, 200))
objects.append(circle)

rect = Rect(Point(0, 0), Point(20, 10), position=Point(200, 260))
objects.append(rect)


# tworzenie obiektu animacji
animation = Animation(10, canvas, Color(25, 25, 100))
for o in objects:
    animation.add(copy.copy(o), path=lambda t: Point(t, t))

Serializer.save("test_all.gif", animation)


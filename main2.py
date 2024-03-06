import math

from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

# tworzenie "canvas"
canvas = Canvas(300, 300)

# tworzenie obiektu
#rect_a = Point(0, 0)
#rect_b = Point(30, 30)
#rect = Rect(rect_a, rect_b)

circle = Circle(20)
circle2 = Circle(30)

#TODO: ensure those 2 work also
#pointA = Point(10, 100)
#pointB = Point(50, 200)

pointA = Point(1, 10)
pointB = Point(5, 20)

line = Line(pointA, pointB)

#bg_rect = Rect(Point(150, 150), Point(300, 300))


# tworzenie sciezki dla obiektu
def f(t):
    radius = 20
    return Point(math.sin(t * 0.1) * radius + 130, math.cos(t * 0.1) * radius + 130)

def f2(t):
    t = t + 30
    radius = 30
    return Point(math.sin(t * 0.1) * radius + 80, math.cos(t * 0.1) * radius + 130)


# tworzenie obiektu animacji
animation = Animation(200, canvas, Color(25, 25, 100))

#animation.add(copy.copy(rect), f)
animation.add(copy.copy(circle), f)
animation.add(copy.copy(circle2), f2)
animation.add(copy.copy(line))

Serializer.save("test.gif", animation)


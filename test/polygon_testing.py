from AnimationLibrary.drawable.Circle import Circle
from AnimationLibrary import Animation
from AnimationLibrary.Canvas import Canvas
from AnimationLibrary.Color import Color
from AnimationLibrary.Point import Point
from AnimationLibrary.Serializer import Serializer
from AnimationLibrary.drawable.Polygon import Polygon
from AnimationLibrary.drawable.Line import Line
from AnimationLibrary.drawable.Rect import Rect

def f(x):
    return Point(x, x)


canvas = Canvas(300, 300)
animation = Animation(5, canvas, bgColor=Color(10, 10, 125, 255))


pos = Point(150, 150)
vertices = [Point(0, 0), Point(10, 10), Point(10, 20), Point(0, 30), Point(-10, 20), Point(-10, 10)]
polygon = Polygon(vertices, animation, Point(100, 100), color=Color(255, 123, 0, 255), path=f)

# vertices2 = [Point(0, 0), Point(100, 100), Point(100, 200), Point(0, 300), Point(-100, 200), Point(-100, 100)]
# polygon2 = Polygon(vertices2, animation=animation, position=Point(10, 10))

# l0 = Line(Point(10, 10), animation=animation, position=vertices[0] + pos)
# l1 = Line(Point(0, 10), animation=animation, position=vertices[1] + pos)
# l2 = Line(Point(-10, 10), animation=animation, position=vertices[2] + pos)
# l3 = Line(Point(-10, -10), animation=animation, position=vertices[3] + pos)
# l4 = Line(Point(0, -10), animation=animation, position=vertices[4] + pos)
# l5 = Line(Point(10, -10), animation=animation, position=vertices[5] + pos)






Serializer.save("test/polygon_testing_2.gif", animation)
# TODO: sprawdz czy iteruje sie po sidesach polygonu
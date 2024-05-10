from AnimationLibrary import *
import math


canvas = Canvas(250,250)
animation = Animation(155, canvas, Color(60, 60, 250))

def circle_movement_1(t: int):
    return Point(100 * math.cos(t / 25), 100 * math.sin(t / 25))

def circle_movement_2(t: int):
    return Point(30 * math.cos(t / 5), 30 * math.sin(t / 5))


circle1 = Circle(50, animation=animation, position=Point(75, 75), name="circle1")
circle2 = Circle(r=20, animation=animation, position=Point(25, 25), parent=circle1, path=circle_movement_1, color=Color(230, 50, 50, 255), name="circle2")
circle3 = Circle(r=10, animation=animation, position=Point(5, 5), parent=circle2, path=circle_movement_2, color=Color(50, 230, 50, 255), name="circle3")


Serializer.save("test/tree_association_testing.gif", animation)

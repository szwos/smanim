from AnimationLibrary.drawable.Circle import Circle
from AnimationLibrary import Animation
from AnimationLibrary.Canvas import Canvas
from AnimationLibrary.Color import Color
from AnimationLibrary.Point import Point
from AnimationLibrary.Serializer import Serializer

def f(x):
    return Point(x, x)


canvas = Canvas(300, 300)
animation = Animation(5, canvas, bgColor=Color(10, 10, 125, 255))

circle = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(100, 50))

Serializer.save("test/tree_testing_2.gif", animation)













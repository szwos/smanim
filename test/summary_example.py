from AnimationLibrary.Animation import Animation
from AnimationLibrary.Canvas import Canvas
from AnimationLibrary.Color import Color
from AnimationLibrary.drawable.Rect import Rect
from AnimationLibrary.Point import Point
from AnimationLibrary.drawable.Circle import Circle
from AnimationLibrary.Serializer import Serializer
from AnimationLibrary.drawable.Line import Line
import math
from AnimationLibrary.Path import Path

canvas = Canvas(500, 500)
anim = Animation(30, canvas=canvas, bgColor=Color(50, 10, 125, 255))


xpos = 0
def circle_movement(t: float):

    move = False
    if t % 20 == 0:
        move = not move

    global xpos

    if move:
        xpos = xpos + 20

    return Point(xpos, 0)


def rownanie_ruchu(t):
    return Point(t, t)


#circle = Circle(r=75, animation=anim, position=Point(25, 25), path=circle_movement)

line1 = Line(Point(100, 100), animation=anim, position=Point(50, 250))
line2 = Line(Point(100, -100), animation=anim, position=Point(150, 350))
line3 = Line(Point(127, 80), animation=anim, position=Point(250, 250))


rect1 = Rect(Point(80, 80), animation=anim, position=Point(50, 400), color=Color(200, 10, 10, 255))
rect2 = Rect(Point(230, 80), animation=anim, position=Point(200, 400), color=Color(200, 10, 10, 255), path= lambda x: Point(x * 2, 0))

circe_nowy = Circle(r=50, animation=anim, position=Point(250, 250), path=rownanie_ruchu)


#rect3 = Rect(Point(50, 50), animation=anim, position=Point(350, 350), parent=rect2) nie działa


Serializer.save("test/summary_example.gif", animation=anim)



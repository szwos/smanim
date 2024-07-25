from AnimationLibrary import *


canvas = Canvas(300, 300)
animation = Animation(30, canvas, Color(30, 30, 230, 255))

rect = Rectangle(Point(80, 80), animation, position=Point(10, 10), color=Color(255, 69, 0))

rect2 = Rectangle(Point(80, 80), animation, position=Point(150, 150), color=Color(10, 230, 10), path=CircularMotion(50, 0, 0, 0.1, 0).function)

rect3 = Rectangle(Point(80, 80), animation, position=Point(10, 200), color=Color(10, 230, 230), path=LinearMotion(0, 0, 2, 0, 1, 0).function)


vertices = [Point(0, 0), Point(30, 30), Point(30, 60), Point(0, 90), Point(-30, 60), Point(-30, 30)]
polygon = Polygon(vertices, animation, position=Point(150, 10), color=Color(69, 255, 0), path=HarmonicMotion(x0 = 0, y0 = 50).function)

control_line = Line(Point(0, 300), animation, position=Point(150, 0), color=Color(255, 0, 0))
Serializer.save("test/fill_testing.gif", animation)
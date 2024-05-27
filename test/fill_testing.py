from AnimationLibrary import *


canvas = Canvas(300, 300)
animation = Animation(30, canvas, Color(30, 30, 230, 255))

rect = Rectangle(Point(80, 80), animation, position=Point(10, 10), color=Color(255, 69, 0))

rect2 = Rectangle(Point(80, 80), animation, position=Point(150, 150), color=Color(10, 230, 10), path=CircularMotion(50, 0, 0, 0.1, 0).function)

rect3 = Rectangle(Point(80, 80), animation, position=Point(10, 200), color=Color(10, 230, 230), path=LinearMotion(0, 0, 2, 0, 1, 0).function)


Serializer.save("test/fill_testing.gif", animation)
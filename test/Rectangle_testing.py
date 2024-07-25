from AnimationLibrary import *

canvas = Canvas(250, 250)
animation = Animation(60, canvas, Color(20, 20, 230, 255))

#rect = Rect(Point(80, 80), animation, position=Point(10, 10))
rectangle = Rectangle(Point(80, 80), animation, position=Point(10, 10), color=Color(255, 0, 0, 255))


vertices = [Point(0, 0), Point(30, 30), Point(30, 60), Point(0, 90), Point(-30, 60), Point(-30, 30)]
polygon = Polygon(vertices, animation, position=Point(10, 10))


Serializer.save("test/rectangle_testing.gif", animation)

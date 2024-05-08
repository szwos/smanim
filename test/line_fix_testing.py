from AnimationLibrary import *


canvas = Canvas(80, 20)
animation = Animation(10, canvas, bgColor=Color(215, 215, 215))


line = Line(B=Point(80, 20), animation=animation, position=Point(0, 0))


Serializer.save(animation=animation, filename="test/line_fix_testing.gif")


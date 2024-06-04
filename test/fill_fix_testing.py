from AnimationLibrary import *


anim = Animation(1, Canvas(100, 100))


pol = Polygon([Point(10, 10), Point(14, 6), Point(18, 10), Point(18, 18), Point(10, 18)], anim, position=Point(50, 50), color=Color(69, 255, 69))


Serializer.save("test/fill_fix_testing.gif", animation=anim)

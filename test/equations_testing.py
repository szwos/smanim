from AnimationLibrary import *


canvas = Canvas(500, 500)
animation = Animation(60, canvas, Color(50, 50, 230, 255))

circular_motion = CircularMotion(50, omega=1/4)
circle = Circle(25, animation, Color(50, 230, 50, 255), position=Point(50, 100), path=circular_motion.function)

linear_motion = LinearMotion(0, 0, 1.5, 0, 2.5, 0.5)
rect = Rect(Point(50, 50), color=Color(235, 180, 50, 255), animation=animation, position=Point(50, 200), path=linear_motion.function)

harmonic_motion = HarmonicMotion(100, 0, 1, 0)
rect2 = Rect(Point(50, 50), color=Color(250, 50, 50, 255), animation=animation, position=Point(100, 300), path=harmonic_motion.function)

damped_harmonic_motion = DampedHarmonicMotion(200, 0, 0.05, 0, 1, 0)
rect3 = Rect(Point(50, 50), color=Color(200, 50, 230, 255), animation=animation, position=Point(100, 400), path=damped_harmonic_motion.function)


Serializer.save("test/equations_testing.gif", animation)

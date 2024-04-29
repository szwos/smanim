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

circle_A = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(100, 50), name="circle_A")
circle_B = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(150, 50), parent=circle_A, name="circle_B")
circle_C = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(100, 100), parent=circle_B, name="circle_C")
circle_D = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(200, 50), parent=circle_B, name="circle_D")
circle_E = Circle(10, animation=animation, color=Color(255, 123, 0, 255), path=f, position=Point(250, 50), parent=circle_A, name="circle_E")

for obj_uuid in animation.objects_tree._tree.nodes:
    obj = animation.objects_tree._tree[obj_uuid]
    print(obj.name)

print("\n\n")

for obj_uuid in animation.objects_tree._tree.traverse(circle_A):
    obj = animation.objects_tree._tree[obj_uuid]
    print(obj.name)


#Serializer.save("test/tree_traversal_testing.gif", animation)













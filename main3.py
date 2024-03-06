from AnimationLibrary import Canvas, Point, Rect, Animation, Color, Serializer, Path, Circle, Line
import copy

# tworzenie "canvas"
canvas = Canvas(300, 300)

# tworzenie obiektu
rect = Rect(Point(0, 0), Point(10, 10))

# tworzenie sciezki dla obiektu
time = 60

position = [Point(0, 0)]
for i in range(1, time):
    x = position[i-1].x + 1
    position.append(Point(x, 0))

def f(t):
    return position[t]


# tworzenie obiektu animacji
animation = Animation(time, canvas, Color(128, 0, 12))

animation.add(copy.copy(rect), f)

Serializer.save("test.gif", animation)


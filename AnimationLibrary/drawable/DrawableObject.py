from AnimationLibrary.tree.Node import Node
from AnimationLibrary import Animation
from AnimationLibrary.Point import Point
from AnimationLibrary.Color import Color
from typing import Callable

# TODO: Node's methods should be hidden from user, research private inheritance or smth idk

class DrawableObject(Node):

    def __init__(self, animation: Animation = None, position: Point = Point(0, 0), color: Color = Color(0, 0, 0, 255), path: Callable[[float], float] = None, parent: 'DrawableObject' = None):
        super().__init__()
        self.position = position
        self.color = color
        self.parent = parent
        self.path = path

        # if animation is None:
        #     raise ValueError("Missing animation: A DrawableObject requires Animation to be registered on it's DrawableTree")

        if animation is not None:
            animation.add(self, parent)

    def transform(self, t: int):
        if self.path is None:
            return self.position
        else:
            return self.position + self.path(t)

    def ancestors_to_root(self):
        if self.parent is None:
            return []

        return [self] + self.parent.ancestors_to_root()


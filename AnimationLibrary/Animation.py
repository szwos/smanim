from .Frame import Frame
from .Point import Point
from AnimationLibrary.tree.DrawableTree import DrawableTree
from AnimationLibrary.drawable.DrawableObject import DrawableObject

# Idea: to allow user control of time. Animation class could have tick(n) method, which would render (or like queue to render idk - it should not affect algorithm's time) given amount of ticks
# this would be easy to use in a scenario, where user runs algorithm and wants every step of algorithm (state of Animation) to last given amount of frames

class Animation:

# TODO: maybe place canvas as root node?
# TODO: move bgColor as this "root canvas" property
# TODO: typehint
    def __init__(self, frameCount, canvas, bgColor):
        self.objects_tree = DrawableTree(canvas)
        self.frameCount = frameCount
        self.canvas = canvas
        self.bgColor = bgColor

    def add(self, obj: DrawableObject, parent: DrawableObject = None):
        self.objects_tree.add(obj, parent)

    # TODO: this needs to be rewritten
    def getFrames(self):

        frames = []

        for t in range(self.frameCount):
            print(f"frame: {t}")
            frame = Frame(self.canvas, self.bgColor)
            #for obj_uuid in self.objects_tree._tree.nodes:

             # TODO: handle when nothing is added to animation

            for obj_uuid in self.objects_tree._tree.traverse(): # TODO traverse method in DrawableTree
                obj = self.objects_tree._tree[obj_uuid]

                if obj.path is None:
                    path_displacement = Point(0, 0)
                else:
                    path_displacement = obj.path(t)

                displaced_pixels = [] # after applying path displacement
                for p in obj.rasterize():
                    displaced_pixels.append(p + path_displacement)

                frame.draw(displaced_pixels)

            frames.append(frame)

        return frames

    # TODO: remove
    # TODO: __str__()

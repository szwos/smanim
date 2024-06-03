from .Frame import Frame
from .Point import Point
from AnimationLibrary.tree.DrawableTree import DrawableTree
from AnimationLibrary.drawable.DrawableObject import DrawableObject
from AnimationLibrary.algorithms.FloodFill import FloodFill
from AnimationLibrary.Color import Color

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

    def getFrames(self):

        frames = []

        for t in range(self.frameCount):
            print(f"frame: {t}")
            frame = Frame(self.canvas, self.bgColor)
            #for obj_uuid in self.objects_tree._tree.nodes:

             # TODO: handle when nothing is added to animation


            for obj in self.objects_tree.traverse():

                transform = Point(0, 0)
                for ancestor in self.objects_tree.ancestors_to_root(obj):
                    transform = transform + ancestor.transform(t)

                displaced_pixels = [] # after applying path displacement
                for p in obj.rasterize():
                    displaced_pixels.append(p + transform)

                frame.draw(displaced_pixels)

            # for obj in self.objects_tree.traverse():
            #
            #     if hasattr(obj, 'fill_seed'):
            #
            #         fill_color = obj.fill_seed.color
            #
            #         transform = Point(0, 0)
            #         for ancestor in self.objects_tree.ancestors_to_root(obj):
            #             transform = transform + ancestor.transform(t)
            #
            #         fill_x = int(obj.fill_seed.x + transform.x)
            #         fill_y = int(obj.fill_seed.y + transform.y)
            #
            #         if fill_x >= 0 and fill_x < self.canvas.width and fill_y >= 0 and fill_y < self.canvas.height:
            #             frame.pixels = FloodFill.fill(frame.pixels, frame.canvas.width, frame.canvas.height, Point(fill_x, fill_y), fill_color)

            frames.append(frame)

        return frames

    # TODO: remove
    # TODO: __str__()

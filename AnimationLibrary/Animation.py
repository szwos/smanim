from .Frame import Frame
from .Point import Point

# Idea: to allow user control of time. Animation class could have tick(n) method, which would render (or like queue to render idk - it should not affect algorithm's time) given amount of ticks
# this would be easy to use in a scenario, where user runs algorithm and wants every step of algorithm (state of Animation) to last given amount of frames

class Animation:

    def __init__(self, frameCount, canvas, bgColor):
        self.objects = {}
        self.frameCount = frameCount
        self.canvas = canvas
        self.bgColor = bgColor

    def add(self, obj, path=None):

        if obj not in self.objects:
            self.objects[obj] = path
        else:
            raise ValueError("object" + str(obj) + "is already present in animation" + str(self))


    def getFrames(self):

        frames = []

        for t in range(self.frameCount):
            print(f"frame: {t}")
            frame = Frame(self.canvas, self.bgColor)
            for obj in self.objects:

                if self.objects[obj] is None:
                    path_displacement = Point(0, 0)
                else:
                    path_displacement = self.objects[obj](t)

                frame.draw(obj.rasterize(), path_displacement)

            frames.append(frame)

        return frames

    # TODO: remove
    # TODO: __str__()

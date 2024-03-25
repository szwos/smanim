from .Frame import Frame
from .Point import Point

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

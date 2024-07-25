from PIL import Image
from .Animation import Animation
from AnimationLibrary.Canvas import Canvas
from AnimationLibrary.Frame import Frame
from AnimationLibrary.Color import Color
from AnimationLibrary.Pixel import Pixel

# TODO: this class needs a better name
class Serializer:

    # TODO: output file format, for now it's only GIF
    @staticmethod
    def save(filename: str, animation: Animation):

        imgs = [frame.getImg() for frame in animation.getFrames()]

        # TODO: add time parameter to animation, and calculate duration value (it's actually mspf)
        # animation.

        imgs[0].save(filename, save_all=True, format="GIF", append_images=imgs[1:], duration=50, loop=0, disposal=2)

    @staticmethod
    def save_pixels(filename: str, pixels):

        max_x = max([p.x for p in pixels])
        min_x = min([p.x for p in pixels])
        max_y = max([p.y for p in pixels])
        min_y = min([p.y for p in pixels])

        canvas = Canvas(max_x - min_x + 1, max_y - min_y + 1)

        frame = Frame(canvas, Color(255, 255, 255))

        for p in pixels:
            frame.pixels[p.x - min_x][p.y - min_y] = p.color

        img = frame.getImg()
        img.save(filename + ".png", "PNG")

    @staticmethod
    def save_frame(filename: str, frame): # TODO: typehint

        width = len(frame)
        height = len(frame[0])

        canvas = Canvas(width, height)

        frame_obj = Frame(canvas, Color(255, 255, 255))

        for x, row in enumerate(frame):
            for y, p in enumerate(frame[x]):
                if frame[x][y] is not None:
                 frame_obj.pixels[x][y] = frame[x][y]
                else:
                    frame_obj.pixels[x][y] = Color(255, 255, 255)

        img = frame_obj.getImg()
        img.save(filename + ".png", "PNG")

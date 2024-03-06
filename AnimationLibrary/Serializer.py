from PIL import Image
from .Animation import Animation


# TODO: this class needs a better name
class Serializer:

    # TODO: output file format, for now it's only GIF
    @staticmethod
    def save(filename: str, animation: Animation):

        imgs = [frame.getImg() for frame in animation.getFrames()]

        # TODO: add time parameter to animation, and calculate duration value (it's actually mspf)
        # animation.

        imgs[0].save(filename, save_all=True, format="GIF", append_images=imgs[1:], duration=50, loop=0, disposal=2)

from PIL import Image, ImageDraw
from .Point import Point

class Frame:
    def __init__(self, canvas, bgColor):
        self.canvas = canvas
        self.bgColor = bgColor
        self._img = Image.new("RGBA", canvas.getDims(), bgColor.asTuple())

        self.pixels = [[self.bgColor for _ in range(self.canvas.height)] for _ in range(self.canvas.width)]

        pass

    def getImg(self):
        draw = ImageDraw.Draw(self._img)

        for x, row in enumerate(self.pixels):
            for y, pixel in enumerate(row):
                draw.point((x, y), fill=pixel.asTuple())

        return self._img

    def draw(self, obj_pixels):

        for pixel in obj_pixels:

            if pixel.x < self.canvas.width and pixel.y < self.canvas.height and \
                pixel.x >= 0 and pixel.y >= 0:

                if pixel.color.a == 0:
                    pass # skip, drawn color is invisible
                elif pixel.color.a != 255:
                    raise NotImplementedError(
                        "alpha blending is not implemented yet, any colors with opacity other than 0 or 255 are not supported")
                else:
                    self.pixels[int(pixel.x)][int(pixel.y)] = pixel.color

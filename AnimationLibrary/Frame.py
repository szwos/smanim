from PIL import Image, ImageDraw
from .Point import Point
from .Canvas import Canvas

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


    #object jest IShapem, ktory za pomoca enumeratora zwraca Pixel
    # Pixel zawieraja pola x, y, (relatywna pozycja wewnątrz obiektu) oraz color, będący kolorem na danej pozycji
    #path jest funkcją (lambdą) zwracającą Transform utworzony zaleznie od jakiejstam funckji
    #Transform posiada pola x, y (na obecna chwile to po prostu punkt)
    def add(self, obj, path, t):

        if path is None:
            path = lambda _: Point(0, 0)

        for pixel in obj:

            if pixel.color.a == 0:
                pass #skip, drawn color is invisible
            elif pixel.color.a != 255: #if it's not fully opaque
                raise NotImplementedError("alpha blending is not implemented yet, any colors with opacity other than 0 or 255 are not supported")
                #old_pixel =
                #combined_alpha =

                #TODO: combine colors accounting for alpha factor
                #TODO: combine alphas
                #blended_color
            else:
                x = pixel.x + int(path(t).x)
                y = pixel.y + int(path(t).y)
                self.pixels[x][y] = pixel.color

    def draw(self, obj, displacement):

        for pixel in obj:
            for x in range(self.canvas.width):
                for y in range(self.canvas.height):

                    if pixel.x == x and pixel.y == y:
                        if pixel.color.a == 0:
                            pass # skip, drawn color is invisible
                        elif pixel.color.a != 255: # not fully opaque
                            raise NotImplementedError("alpha blending is not implemented yet, any colors with opacity other than 0 or 255 are not supported")
                        else:
                            x = pixel.x + displacement.x
                            y = pixel.y + displacement.y
                            self.pixels[x][y] = pixel.color

from typing import List
from AnimationLibrary.Pixel import Pixel
from AnimationLibrary.Color import Color
from AnimationLibrary.Point import Point


def _isValid(pixels, width: int, height: int, x: int, y: int, previous_color: Color, new_color: Color):
    try:
        if x < 0 or x > width or y < 0 or y > height or pixels[x][y] != previous_color or pixels[x][y] == new_color:
            return False
        else:
            return True
    except IndexError:
        return False

class FloodFill():
    def __init__(self):
        pass


    @staticmethod
    def fill(pixels: List[List[Color]], width: int, height: int, fill_seed: Point, color: Color, prevColor: Color = None):

        try:
            if prevColor == None:
                prevColor = pixels[fill_seed.x][fill_seed.y]
        except:
            print(fill_seed.x, fill_seed.y)

        queue = []
        queue.append([fill_seed.x, fill_seed.y])

        pixels[fill_seed.x][fill_seed.y] = color

        while queue:
            current_pixel = queue.pop()

            pos_x = current_pixel[0]
            pos_y = current_pixel[1]

            if _isValid(pixels, width, height, pos_x + 1, pos_y, prevColor, color):
                pixels[pos_x + 1][pos_y] = color
                queue.append([pos_x + 1, pos_y])

            if _isValid(pixels, width, height, pos_x - 1, pos_y, prevColor, color):
                pixels[pos_x - 1][pos_y] = color
                queue.append([pos_x - 1, pos_y])

            if _isValid(pixels, width, height, pos_x, pos_y + 1, prevColor, color):
                pixels[pos_x][pos_y + 1] = color
                queue.append([pos_x, pos_y + 1])

            if _isValid(pixels, width, height, pos_x, pos_y - 1, prevColor, color):
                pixels[pos_x][pos_y - 1] = color
                queue.append([pos_x, pos_y - 1])

        return pixels

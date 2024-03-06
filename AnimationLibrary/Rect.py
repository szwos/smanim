#TODO: make all those classes implement some interface that will implement 
#   getPosition() - top left corner of a shape 
#   getPixels() - returns some kind of array of Pixels with colors, that will be easy to be put on PiL texture
#   Update() - can be not implemented by derived classes (can basically do nothing)

#TODO: Qol overrides (e.g. taking tuples, tables instead of other objects for construction)

from .Pixel import Pixel
from .Point import Point
from .Color import Color

class Rect():
    """
    @args:
    A - top left corner of the rectangle
    B - bottom right corner of the rectangle
    """
    #TODO: in current implementation A Point is useless, because rectangle is always describing it's internal coordinates, hence we can cope with width height described in B Point
    #TODO: default position
    def __init__(self, A: Point, B: Point, color: Color = Color(0, 0, 0, 255)) -> None:
        #this should be handled by base class (super() ??)
        self.A = A
        self.B = B
        self.pixels = [[0] * self.B.x for _ in range(self.B.y)]


        #this should be handled by derived class
        for i in range(self.B.y): #TODO: i don't like swapping y with x here, but i was getting index out of range, like it should be swapped idk
            for j in range(self.B.x):
                #print(i, j)
                self.pixels[i][j] = Pixel(i, j, Color(25, 25, 225)) #TODO: take color from somewhere

    def __iter__(self):
        self.i = 0
        self.j = 0
        return self
    
    def __next__(self):
        if self.j >= self.B.y:
            raise StopIteration
        
        pixel = self.pixels[self.i][self.j]
        self.i += 1
        if self.i >= self.B.x:
            self.i = 0
            self.j += 1
        return pixel



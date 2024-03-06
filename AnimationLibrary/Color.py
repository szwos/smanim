class Color():
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    #multiplication by scalar value
    def __imul__(self, other): 
        self.r *= other
        self.g *= other
        self.b *= other
        return self
    
    def __itruediv__(self, other): 
        self.r /= other
        self.g /= other
        self.b /= other
        return self

    #addition of vector
    def __iadd__(self, other):
        self.r += other.r
        self.g += other.g
        self.b += other.b
        return self

    #addition of vector
    def __add__(self, other):
        return Color((self.r + other.r, self.g + other.g, self.b + other.b))

    def __str__(self):
        return "({0},{1},{2},{3})".format(self.r,self.g,self.b, self.a)

    #returns value of percieved luminance of color
    def getLuminance(self):
        return (0.299 * self.r + 0.587 * self.g + 0.114 * self.b)

    #returns tuple of INT's
    def asTuple(self):
        #TODO: why is int() there?
        return (int(self.r), int(self.g), int(self.b), int(self.a))

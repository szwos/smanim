# alternate scenario for this is allowing both position and Grid, and considering position as position inside of cell of a grid
# instead of position on screen
# but that seems like pain in the ass to implement (this logic would need to be taken care of in rendering, also
# space of cell is confined, hence objects that are e.g. larger than single cell would need to be handled somehow
# using masking or just allowing objects to go out of cell (then overlaying with other cells would create some problems) )
# This scenario also has it's problems:
# When putting in a Rectangle it would be handy to make it fill the whole cell, to create e.g. checker board
# But a rectangle has it's own dimensions, so stretching it makes those dimensions pointless
# it gets even more complicated, when a polygon would be put in a cell, to stretch it somehow (and i really dont know
# how, but it smells like some funky maths if we're talking about vectors...) a describing rectangle would be needed

# note on stretching:
# if stretching of any kind is considered, it would be handy to make it something possible in any context by
# just stretching object to it's canvas (canvas it was placed on, this sound like it will need parent ref)
# Then stretching to a cell would be as trivial as setting canvas of such object to dimensions of given cell

#canvas seem from now on more like a frame


from AnimationLibrary import Point
class Grid:
    def __init__(self, ncols, nrows):
        self.columns = ncols
        self.rows = nrows

    def setpos(self, x, y):
        pass

class Circle:
    def __init__(self, radius, position_placement):
        self.radius = radius

        # TODO: access method (like grid() for position)

        if type(position_placement) == type(Grid(0, 0)): # disgusting way of type comparision...
            self._grid = position_placement
        else:
            self.position = position_placement

    def grid(self, x, y):
        if self._grid is None:
            raise Exception("accesed grid when position was passe in ctor")
        self._grid.setpos(x, y)


circle1 = Circle(2, Point(1, 2))
circle1.position = Point(3, 3)

circle2 = Circle(2, Grid(2, 2))
circle2.grid(0, 0)
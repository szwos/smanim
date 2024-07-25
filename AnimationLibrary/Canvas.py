from AnimationLibrary.tree.Node import Node

class Canvas(Node):
    def __init__(self, width: int, height: int) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def get_height(self) -> int:
        return self.height
    
    def get_width(self) -> int:
        return self.width
    
    def getDims(self) -> tuple:
        return self.width, self.height

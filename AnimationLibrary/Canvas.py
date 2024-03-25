
class Canvas():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_height(self) -> int:
        return self.height
    
    def get_width(self) -> int:
        return self.width
    
    def getDims(self) -> tuple:
        return self.width, self.height

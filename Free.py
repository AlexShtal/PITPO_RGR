from Position import *
class Free:
    name = "Free"
    position: Position
    def __init__(self, x, y):
        self.position = Position(x, y)

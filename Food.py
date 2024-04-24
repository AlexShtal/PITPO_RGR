from Position import *


class Food:
    position: Position
    value: int
    name = "Food"

    def __init__(self, x, y):
        self.position = Position(x, y)
        self.value = 3

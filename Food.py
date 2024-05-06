from Position import Position

from consts import *


class Food:
    position: Position
    value = GRASS_VALUE
    name = "Food"

    def __init__(self, x, y):
        self.position = Position(x, y)

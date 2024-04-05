import random as rd

VALID_DIRECTIONS = ["left", "Up", "Right", "Down"]


class Cell:
    def __init__(self):
        self.name = "Cell"


class Bug:
    def __init__(self, position: dict, speed: int = 1, hunger: int = 1,
                 direction: str = rd.choice(VALID_DIRECTIONS)):
        self.position: dict = position
        self.name = "Bug"
        self.speed = speed
        self.hunger = hunger
        self.direction = direction

    def turn(self, direction: str):
        if direction in VALID_DIRECTIONS:
            self.direction = direction
        else:
            raise Exception('Invalid direction name.')

    def step(self, entity_matrix: list):

        match self.direction:
            case "Left":
                if entity_matrix[self.position["x"] - 1][self.position["y"]].name != "Bug":
                    self.position["x"] -= 1
            case "Up":
                if entity_matrix[self.position["x"]][self.position["y"] + 1].name != "Bug":
                    self.position["y"] += 1
            case "Right":
                if entity_matrix[self.position["x"] + 1][self.position["y"]].name != "Bug":
                    self.position["x"] += 1
            case "Down":
                if entity_matrix[self.position["x"]][self.position["y"] - 1].name != "Bug":
                    self.position["y"] -= 1


class Food:
    def __init__(self, value: int = 1):
        self.value = value
        self.name = "Food"

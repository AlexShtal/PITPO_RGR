import random as rd
import time
from entitys import Cell, Bug, Food

SCREEN_SIZE_X: int = 3
SCREEN_SIZE_Y: int = 3
RENDER_SPEED: int = 1
BUG_VISION_DISTANCE: int = 5
VALID_DIRECTIONS = ["left", "Up", "Right", "Down"]


class Petri:

    def __init__(self, path: str = None):
        if path:
            entity_matrix: list = []
            with open(path) as file:
                index_y = 0

                for row in file:
                    entity_matrix.append([])
                    for item in row.strip().split(" "):
                        entity_matrix[index_y].append(item)
                    index_y += 1

            for index_y in range(SCREEN_SIZE_Y):
                for index_x in range(SCREEN_SIZE_X):
                    match entity_matrix[index_x][index_y]:
                        case "Bug":
                            entity_matrix[index_x][index_y] = Bug({"x": index_x, "y": index_y})
                        case "Food":
                            entity_matrix[index_x][index_y] = Food()
                        case "Empty":
                            entity_matrix[index_x][index_y] = Cell()
                        case _:
                            raise Exception("Invalid cell type from file.")

            self.entity_matrix = entity_matrix
        else:
            raise Exception("No path to file.")

    def __repr__(self):
        string: str = ""
        for row in self.entity_matrix:
            string = string + " ".join([instance.name for instance in row]) + "\n"
        return string

    def run(self):
        while True:
            print(petr)
            self.render()
            time.sleep(RENDER_SPEED)

    def render(self):
        for row in self.entity_matrix:
            for item in row:
                if item.name == "Bug":
                    action = rd.choice(["Turn", "Step"])

                    match action:
                        case "Turn":
                            item.turn(rd.choice(VALID_DIRECTIONS))
                        case "Step":
                            item.step(self.entity_matrix)


petr = Petri("matrix.txt")
petr.run()


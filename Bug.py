from sklearn.neural_network import MLPClassifier
import numpy as np

from Position import Position

from DefaultBehavior import DefaultBehavior




class Bug:
    position: Position
    hunger = 10
    pregnant = False
    acted = False

    behavior_model: MLPClassifier

    def __init__(self, x, y, parent_model: MLPClassifier = None):
        self.position = Position(x, y)
        self.hunger = 5

        model = DefaultBehavior.GetModel()

        if parent_model:
            parent_coefs = parent_model.coefs_
            model.coefs_ = [array * np.random.normal(1, .2, size=array.shape) for array in parent_coefs]

        self.behavior_model = model

    # Returns possible steps for bug
    def getPossibleSteps(self, items_map: []):
        x_list = [self.position.x]
        y_list = [self.position.y]

        if self.position.x == 0:
            x_list.append(self.position.x + 1)
        elif self.position.x == len(items_map[0]) - 1:
            x_list.append(self.position.x - 1)
        else:
            x_list.append(self.position.x + 1)
            x_list.append(self.position.x - 1)

        if self.position.y == 0:
            y_list.append(self.position.y + 1)
        elif self.position.y == len(items_map) - 1:
            y_list.append(self.position.y - 1)
        else:
            y_list.append(self.position.y + 1)
            y_list.append(self.position.y - 1)

        return x_list, y_list

    # Returns elements that bug can see
    def get_surrounding_elements(self, items_map: []):
        rows = len(items_map)
        cols = len(items_map[0]) if rows > 0 else 0
        row = self.position.y
        col = self.position.x
        surrounding_elements = []

        # Check items around bug
        for i in range(row - 2, row + 3):
            for j in range(col - 2, col + 3):
                # Check items to be inside matrix
                if 0 <= i < rows and 0 <= j < cols:
                    # Reject self position
                    if (i, j) != (row, col):
                        neighbour = items_map[i][j]
                        match neighbour.name:
                            case "Free":
                                surrounding_elements.append(1)
                            case "GrassBug":
                                surrounding_elements.append(2)
                            case "MeatBug":
                                surrounding_elements.append(3)
                            case "Food":
                                surrounding_elements.append(4)
                else:
                    surrounding_elements.append(0)
        return surrounding_elements


    def findNearestFreeSpace(self, items_map: []):
        nearest_free_position = []

        x_list, y_list = self.getPossibleSteps(items_map)

        for x in x_list:
            for y in y_list:
                if items_map[y][x].name == "Free":
                    nearest_free_position.append(Position(x, y))
        return nearest_free_position

    def goToPosition(self, new_position: Position):
        self.position = new_position

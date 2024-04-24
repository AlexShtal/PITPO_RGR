from Position import *
from Free import *


class Bug:
    position: Position
    hunger = 5
    name = "Bug"
    acted = False

    def __init__(self, x, y):
        self.position = Position(x, y)
        self.hunger = 5

    def getSteps(self, items_map: []):
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

    def findNearestFood(self, items_map: []):
        nearest_food_position: Position

        x_list, y_list = self.getSteps(items_map)

        for x in x_list:
            for y in y_list:
                if items_map[y][x].name == "Food":
                    nearest_food_position = Position(x, y)
                    return nearest_food_position
        return 0

    def findNearestFreeSpace(self, items_map: []):
        nearest_free_position: Position

        x_list, y_list = self.getSteps(items_map)

        for x in x_list:
            for y in y_list:
                if items_map[y][x].name == "Free":
                    nearest_free_position = Position(x, y)
                    return nearest_free_position
        return 0

    def goToPosition(self, new_position: Position):
        self.position = new_position

    def act(self, items_map: []):
        nearest_food_position = self.findNearestFood(items_map)
        nearest_free_position = self.findNearestFreeSpace(items_map)

        if (nearest_food_position):
            items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
            self.hunger = self.hunger + items_map[nearest_food_position.y][nearest_food_position.x].value % 5
            self.goToPosition(nearest_food_position)
            items_map[self.position.y][self.position.x] = self
            self.acted = True
        elif (nearest_free_position):
            items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
            self.goToPosition(nearest_free_position)
            items_map[self.position.y][self.position.x] = self
            self.acted = True
        return items_map

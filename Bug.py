from Free import Free
from Position import Position
from random import choice


class Bug:
    position: Position
    hunger = 10
    pregnant = False
    name = "Bug"
    acted = False

    def __init__(self, x, y):
        self.position = Position(x, y)
        self.hunger = 5

    # Processing possible steps according to bug position
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

    def findNearestFood(self, items_map: []):
        nearest_food_position = []

        x_list, y_list = self.getPossibleSteps(items_map)

        for x in x_list:
            for y in y_list:
                if items_map[y][x].name == "Food":
                    nearest_food_position.append(Position(x, y))
        return nearest_food_position

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

    def act(self, items_map: []):
        nearest_food_positions = self.findNearestFood(items_map)
        nearest_free_positions = self.findNearestFreeSpace(items_map)

        # If food found nearby
        if nearest_food_positions:
            target = choice(nearest_food_positions)
            items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
            self.hunger = self.hunger + items_map[target.y][target.x].value % 10
            self.goToPosition(target)
            items_map[self.position.y][self.position.x] = self
            self.acted = True
        # If there is no food, step to free space
        elif nearest_free_positions:
            target = choice(nearest_free_positions)
            items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
            self.goToPosition(target)
            items_map[self.position.y][self.position.x] = self
            self.acted = True

        # Birth new bug
        if self.hunger >= 10 or self.pregnant:
            nearest_free_positions = self.findNearestFreeSpace(items_map)
            if nearest_free_positions:
                target = choice(nearest_free_positions)
                items_map[target.y][target.x] = Bug(target.x, target.y)
                self.hunger = self.hunger - 5
                self.pregnant = False
            else:
                self.pregnant = True

        return items_map

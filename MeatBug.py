from random import choice
import numpy as np

from Bug import Bug
from Free import Free

from Actions import Actions


class MeatBug(Bug):
    name = "MeatBug"

    # Processing possible steps according to bug position and food type
    def getPossibleActions(self, items_map: []):
        actions = []
        possible_targets = ["GrassBug", "Free"]

        col = self.position.x
        row = self.position.y

        for y_offset in [-1, 0, 1]:
            for x_offset in [-1, 0, 1]:

                new_col = col + x_offset
                new_row = row + y_offset

                if 0 <= new_row < len(items_map) and 0 <= new_col < len(items_map[0]) \
                        and items_map[new_row][new_col].name in possible_targets:

                    if y_offset == -1:
                        if x_offset == -1:
                            actions.append(Actions.step_left_up)
                        elif x_offset == 0:
                            actions.append(Actions.step_up)
                        elif x_offset == 1:
                            actions.append(Actions.step_right_up)
                    elif y_offset == 0:
                        if x_offset == -1:
                            actions.append(Actions.step_left)
                        elif x_offset == 0:
                            continue
                        elif x_offset == 1:
                            actions.append(Actions.step_right)
                    elif y_offset == 1:
                        if x_offset == -1:
                            actions.append(Actions.step_left_down)
                        elif x_offset == 0:
                            actions.append(Actions.step_down)
                        elif x_offset == 1:
                            actions.append(Actions.step_right_down)

        return [item.value for item in actions]

    def act(self, items_map: []):

        surroundings = np.array(self.get_surrounding_elements(items_map))

        action = self.behavior_model.predict(surroundings.reshape(1, 8))

        possible_actions = self.getPossibleActions(items_map)

        x_pos = self.position.x
        y_pos = self.position.y

        if not possible_actions:
            return items_map
        elif action not in possible_actions:
            action = choice(possible_actions)

        x_offset = 0
        y_offset = 0

        match action:
            case Actions.step_left_up.value:
                x_offset -= 1
                y_offset -= 1
            case Actions.step_up.value:
                y_offset -= 1
            case Actions.step_right_up.value:
                x_offset += 1
                y_offset -= 1
            case Actions.step_left.value:
                x_offset -= 1
            case Actions.step_right.value:
                x_offset += 1
            case Actions.step_left_down.value:
                x_offset -= 1
                y_offset += 1
            case Actions.step_down.value:
                y_offset += 1
            case Actions.step_right_down.value:
                x_offset += 1
                y_offset += 1

        target = items_map[y_pos + y_offset][x_pos + x_offset]

        match target.name:
            case "GrassBug":
                items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
                self.hunger += 5 % 10
                self.goToPosition(target.position)
                items_map[self.position.y][self.position.x] = self
            case "Free":
                items_map[self.position.y][self.position.x] = Free(self.position.x, self.position.y)
                self.goToPosition(target.position)
                items_map[self.position.y][self.position.x] = self

        # Birth new bug
        if self.hunger >= 10 or self.pregnant:
            nearest_free_positions = self.findNearestFreeSpace(items_map)
            if nearest_free_positions:
                target = choice(nearest_free_positions)
                items_map[target.y][target.x] = MeatBug(target.x, target.y, self.behavior_model)
                self.hunger = self.hunger - 5
                self.pregnant = False
            else:
                self.pregnant = True

        self.acted = True
        return items_map

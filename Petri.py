import time
import os
from MeatBug import MeatBug
from GrassBug import GrassBug
from Food import Food
from Free import Free
from random import random

from consts import *

class Petri:
    items_map = []
    alive_entitys = ["GrassBug", "MeatBug"]
    simulation_speed: int
    food_spawn_rate: int

    def __init__(self, simulation_speed, food_spawn_rate):
        self.simulation_speed = simulation_speed
        self.food_spawn_rate = food_spawn_rate

    # Processes map
    def render(self):

        for y_index in range(len(self.items_map)):
            for x_index in range(len(self.items_map[0])):
                item = self.items_map[y_index][x_index]
                if item.name in self.alive_entitys:
                    if not item.acted:
                        self.items_map = item.act(self.items_map)

    def printMatrix(self):
        for row in self.items_map:
            for item in row:
                match item.name:
                    case "MeatBug":
                        print("!", end=" ")
                    case "GrassBug":
                        print("@", end=" ")
                    case "Food":
                        print(".", end=" ")
                    case "Free":
                        print(" ", end=" ")
            print()

    def readMatrix(self, file_path: str):

        with open(file_path) as file:
            temp_class_line = []
            x_pos = 0
            y_pos = 0
            for line in file:
                for class_name in line.strip().split(" "):
                    match class_name:
                        case "MeatBug":
                            temp_class_line.append(MeatBug(x_pos, y_pos))
                        case "GrassBug":
                            temp_class_line.append(GrassBug(x_pos, y_pos))
                        case "Food":
                            temp_class_line.append(Food(x_pos, y_pos))
                        case "Free":
                            temp_class_line.append(Free(x_pos, y_pos))
                    x_pos += 1
                self.items_map.append(temp_class_line)
                temp_class_line = []
                x_pos = 0
                y_pos += 1

    # Makes all bugs non acted
    def clearActed(self):
        for line in self.items_map:
            for item in line:
                if item.name in self.alive_entitys:
                    item.acted = False

    # Starves bugs
    def starve(self):
        for line in self.items_map:
            for item in line:
                if item.name in self.alive_entitys:
                    item.hunger -= STARVE_PACE

    # Deletes starved bugs
    def clearStarved(self):
        for line in self.items_map:
            for item in line:
                if item.name in self.alive_entitys:
                    if item.hunger <= 0:
                        self.items_map[item.position.y][item.position.x] = Free(item.position.y, item.position.x)

    # Spawns food
    def spawnFood(self):
        for line in self.items_map:
            for item in line:
                if item.name == "Free" and random() < self.food_spawn_rate:
                    self.items_map[item.position.y][item.position.x] = Food(item.position.y, item.position.x)

    # Checks if map empty of bugs
    def isEmpty(self):

        flag = True
        for line in self.items_map:
            for item in line:
                if item.name in self.alive_entitys:
                    flag = False
        return flag

    def run(self):
        while True:
            self.printMatrix()
            self.render()
            self.clearActed()
            self.starve()
            self.clearStarved()
            if self.isEmpty():
                clearConsole()
                exit(0)
            self.spawnFood()
            time.sleep(1 / self.simulation_speed)
            clearConsole()


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

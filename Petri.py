import time
import os
from Bug import *
from Food import *
from Free import *
from random import random


class Petri:
    items_map = []
    simulation_speed: int
    food_spawn_rate: int

    def __init__(self, simulation_speed, food_spawn_rate):
        self.simulation_speed = simulation_speed
        self.food_spawn_rate = food_spawn_rate

    def render(self):
        for y_index in range(len(self.items_map)):
            for x_index in range(len(self.items_map[0])):
                item = self.items_map[y_index][x_index]
                if item.name == "Bug":
                    if not item.acted:
                        self.items_map = item.act(self.items_map)

    def printMatrix(self):
        for row in self.items_map:
            for item in row:
                match item.name:
                    case "Bug":
                        print("@", end=" ")
                    case "Food":
                        print("*", end=" ")
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
                        case "Bug":
                            temp_class_line.append(Bug(x_pos, y_pos))
                        case "Food":
                            temp_class_line.append(Food(x_pos, y_pos))
                        case "Free":
                            temp_class_line.append(Free(x_pos, y_pos))
                    x_pos += 1
                self.items_map.append(temp_class_line)
                temp_class_line = []
                x_pos = 0
                y_pos += 1

    def clearActed(self):
        for line in self.items_map:
            for item in line:
                if item.name == "Bug":
                    item.acted = False

    def starve(self):
        for line in self.items_map:
            for item in line:
                if item.name == "Bug":
                    item.hunger -= 1

    def clearStarved(self):
        for line in self.items_map:
            for item in line:
                if item.name == "Bug":
                    if item.hunger <= 1:
                        self.items_map[item.position.y][item.position.x] = Free(item.position.y, item.position.x)

    def spawnFood(self):
        for line in self.items_map:
            for item in line:
                if item.name == "Free" and random() < self.food_spawn_rate:
                    self.items_map[item.position.y][item.position.x] = Food(item.position.y, item.position.x)

    def isEmpty(self):
        flag = True
        for line in self.items_map:
            for item in line:
                if item.name == "Bug":
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
            time.sleep(self.simulation_speed)
            clearConsole()


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

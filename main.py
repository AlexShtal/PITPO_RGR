from Petri import *

SIMULATION_SPEED = 1
FOOD_SPAWN_RATE = 0

petri = Petri(SIMULATION_SPEED, FOOD_SPAWN_RATE)
petri.readMatrix("matrixs/10x10.txt")
petri.run()

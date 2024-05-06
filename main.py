from Petri import Petri

from consts import *


petri = Petri(SIMULATION_SPEED, FOOD_SPAWN_RATE)
petri.readMatrix("matrixs/55x55singlebug.txt")
petri.run()

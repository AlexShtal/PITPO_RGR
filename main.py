from Petri import Petri

SIMULATION_SPEED = 0.5
FOOD_SPAWN_RATE = 0.01

petri = Petri(SIMULATION_SPEED, FOOD_SPAWN_RATE)
petri.readMatrix("matrixs/5x5.txt")
petri.run()

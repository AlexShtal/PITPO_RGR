# Generates map matrix
with open("55x55singlebug.txt", "a") as f:
    for row in range(55):
        if row == 10:
            f.write("Food " * 27 + "GrassBug " + "Food " * 26 + "Food\n")
        else:
            f.write("Food " * 54 + "Food\n")
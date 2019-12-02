def task1(moduleList):
    # What is the sum of the fuel requirements for all of the modules on your spacecraft?
    fuelSum = 0
    for listitem in moduleList:
        fuelSum += calculateFuel(listitem)
    return fuelSum


def task2(moduleList):
    # What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking
    # into account the mass of the added fuel? (Calculate the fuel requirements for each module separately,
    # then add them all up at the end.)
    massSum = 0
    for listitem in moduleList:
        fuelMass = calculateFuel(listitem)

        while fuelMass > 0:
            massSum += fuelMass
            fuelMass = calculateFuel(fuelMass)

    return massSum


def calculateFuel(mass):
    # Fuel required to launch a given module is based on its mass.
    # Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    return max(0, (mass // 3) - 2)


def main():
    # open file and read the lines, stripping the newlines and converting to int
    with open("input.txt") as file:
        moduleList = [int(line.strip()) for line in file]

    print(task1(moduleList))
    print(task2(moduleList))


if __name__ == '__main__':
    main()


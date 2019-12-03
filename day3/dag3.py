def main():
    with open("input.txt") as f:
        firstWire = [(line[0], int(line[1:])) for line in f.readline().strip().split(",")]
        secondWire = [(line[0], int(line[1:])) for line in f.readline().strip().split(",")]

        # map directions
        direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

        firstCoordinates = set()
        firstSteps = {}
        xCoordinate, yCoordinate, steps = 0, 0, 0

        for (directionIndexLetter, amountOfSteps) in firstWire:
            xDirection, yDirection = direction[directionIndexLetter]
            for i in range(amountOfSteps):
                xCoordinate += xDirection
                yCoordinate += yDirection
                steps += 1
                firstSteps[(xCoordinate, yCoordinate)] = steps
                firstCoordinates.add((xCoordinate, yCoordinate))

        intersect = set()
        xCoordinate, yCoordinate, steps = 0, 0, 0

        for (directionIndexLetter, amountOfSteps) in secondWire:
            xDirection, yDirection = direction[directionIndexLetter]
            for i in range(amountOfSteps):
                xCoordinate += xDirection
                yCoordinate += yDirection
                steps += 1
                if (xCoordinate, yCoordinate) in firstCoordinates:
                    intersect.add((xCoordinate, yCoordinate, steps + firstSteps[(xCoordinate, yCoordinate)]))

        # What is the Manhattan distance from the central port to the closest intersection?
        print("Task 1: {}".format(min(map(lambda x: abs(x[0]) + abs(x[1]), intersect))))

        # What is the fewest combined steps the wires must take to reach an intersection?
        print("Task 2: {}".format(min(map(lambda x: x[2], intersect))))


if __name__ == '__main__':
    main()

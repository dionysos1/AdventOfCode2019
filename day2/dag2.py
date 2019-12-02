def runProgram(sequence):
    sequenceIndex = 0

    # read the sequence 4 at a time
    while sequenceIndex < len(sequence):

        if sequence[sequenceIndex] == 99:
            break

        sequence = runOpCode(sequence, sequenceIndex)
        sequenceIndex += 4
    return sequence


def runOpCode(sequence, sequenceIndex):
    if sequence[sequenceIndex] == 1:
        sequence[sequence[sequenceIndex + 3]] = sequence[sequence[sequenceIndex + 1]] + sequence[sequence[sequenceIndex + 2]]
    if sequence[sequenceIndex] == 2:
        sequence[sequence[sequenceIndex + 3]] = sequence[sequence[sequenceIndex + 1]] * sequence[sequence[sequenceIndex + 2]]

    return sequence


def nounVerbProgram(original):

    for noun in range(100):
        for verb in range(100):
            sequence = original[:]
            sequence[1] = noun
            sequence[2] = verb

            if runProgram(sequence)[0] == 19690720:
                return "output: {}".format(100 * sequence[1] + sequence[2])


def main():

    with open("input.txt") as file:
        sequence = [int(number) for number in file.read().split(",")]
        sequence[1] = 12
        sequence[2] = 2

        # Task 1
        # print(runProgram(sequence))

        # Task 2
        print(nounVerbProgram(sequence))


if __name__ == '__main__':
    main()

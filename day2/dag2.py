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


def main():

    with open("input.txt") as file:
        sequence = [int(number) for number in file.read().split(",")]
        sequence[1] = 12
        sequence[2] = 2
        print(runProgram(sequence))


if __name__ == '__main__':
    main()

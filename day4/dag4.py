def main():

    begin = 158126
    end = 624574

    totalPasswords = 0
    secondCriteria = 0

    for number in range(begin, end + 1):
        lastDigit = 0
        lastCount = 0
        sameDigitOrMore = False
        sameDigit = False

        for currentDigit in str(number):
            currentDigit = int(currentDigit)
            if currentDigit < lastDigit:
                break
            elif currentDigit == lastDigit:
                sameDigitOrMore = True
                lastCount += 1
            else:
                if lastCount == 2:
                    sameDigit = True
                lastCount = 1
            lastDigit = currentDigit
        else:
            if sameDigitOrMore:
                totalPasswords += 1
            if sameDigit or lastCount == 2:
                secondCriteria += 1

    print("Task 1: {}".format(totalPasswords))
    print("Task 2: {}".format(secondCriteria))


if __name__ == '__main__':
    main()

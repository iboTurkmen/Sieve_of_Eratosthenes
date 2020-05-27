import math


def checkNum(inputNum):
    number = 0
    prime = "2,"
    for number in range(2, int(inputNum)+1):
        if int(number) % 2 != 0:
            prime += str(number)+","
    print(prime)
    main()


def main():
    print("For Exit please enter 'EXIT' or 'exit'")
    inputNum = input("Please Enter Limit of a Prime Number That You Want: ")
    if inputNum.upper() == "EXIT":
        exit()
    if inputNum == "":
        main()
    if int(inputNum) < 2:
        print("Please Enter Positive Numbers only and bigger than 2!!!")
        main()
    else:
        checkNum(inputNum)


main()
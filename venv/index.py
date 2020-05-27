import math


def checkNum(inputNum):
    p = 2
    prime = [True]*(int(inputNum)-1)
    while True:
        multi = 2
        calculate = p * multi
        while calculate <= int(inputNum):
            prime[calculate - 2] = False
            multi += 1
            calculate = p * multi

        for i, pri in enumerate(prime):
            if pri and i + 2 > p:
                p = i + 2
                break
        else:
            break

    for i, pri in enumerate(prime):
        if pri:
            print(i+2)
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
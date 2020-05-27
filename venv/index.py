






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
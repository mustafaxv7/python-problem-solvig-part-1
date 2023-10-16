#A simple Calcolator that can perform Addition , Substraction , Multiplication , Division ,...
while True:
    print("\n\n\t\t------ Calcolator :MENU ------\n\n")
    print("1.Press Number One To Perform Addition\n")
    print("2.Press Number Two To Perform Substraction\n")
    print("3.Press Number Three To Perform Multiplication\n")
    print("4.Press Number Four To Perform Division\n")
    print("5.Press Number Five To Perform Reminder of a Division Operation\n") 
    print("6.Press Number Six To Perform Power\n")

    operation = int(input("\nChoose From The Table Above An Operation To Perform>>: "))
    numberOne = float(input("\nNumber One>>: "))
    numberTwo = float(input("\nNumber Two>>: "))
    if(operation == 1):
        result = numberOne + numberTwo
        print(f"\nResult ==> {result}")
    elif(operation == 2):
        result = numberOne - numberTwo
        print(f"\nResult ==> {result}")
    elif(operation == 3):
        result = numberOne * numberTwo
        print(f"\nResult ==> {result}")
    elif(operation == 4):
        try:
            result = numberOne / numberTwo
        except ZeroDivisionError:
            print("\nMath Error\n")
            continue
        print(f"\nResult ==> {result}")
    elif(operation == 5):
        try:
            result = numberOne % numberTwo
        except ZeroDivisionError:
            print("Math Error")
            continue
        print(f"\nResult ==> {result}")
    elif(operation == 6):
        result = numberOne ** numberTwo
        print(f"\nResult ==> {result}")
    else:
        print("\nError This Operation is Not Difine\n")

    print("\nPress C to Continue")
    print("\nPress E or e to Exit\n")
    decision = input(">> ")
    if(decision.upper() == "E"):
        break
    
terminate = False
while not terminate:
    num1 = input("Please enter a number: ")
    num1 = int(num1)
    num2 = input("Please enter a number: ")
    num2 = int(num2)

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add" , "sub"]:
            print("unknown operation! ")
            continue
        if operation == "add":
            print("Result is: ", num1+num2)
            break
        if operation == "sub":
            print("Result is: ", num1-num2 )
            break
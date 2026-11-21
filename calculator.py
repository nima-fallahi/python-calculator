print("New Version")
while True:
    command = input("Stay or Exit: ")
    if command == "Exit":
        print("You entered:", repr(command))
        break
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    operation = input(" +, -, *, /, ")
    if operation == "+":
        x = num1 + num2
        print("Addition", x)
    elif operation == "-":
        y = num1 - num2
        print("Subtraction", y)
    elif operation == "*":
        z = num1 * num2
        print("Multiplication", z)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

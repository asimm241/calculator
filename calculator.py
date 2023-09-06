"""calculator for four simple operation"""
import operations as math

exitCommand: str = ''
while exitCommand != 'exit':
    operation = input("Enter operation\n + \n - \n * \n /\n")
    try:
        num1 = int(input("left operand: "))
        num2 = int(input("right operand: "))
    except ValueError:
        print("invalid operands only digits allowed")
        continue

    if operation == "+":
        print(f"{num1} + {num2} = {math.add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {math.minus(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {math.multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} / {num2} = {math.divide(num1, num2)}")
    else:
        print(f"can not perform \"{operation}\"")

    exitCommand = input(
        "enter \"exit\" to exit or anything else to continue\n")

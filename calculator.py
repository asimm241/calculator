"""calculator for four simple operation"""

def add(op1, op2):
    """Add given params"""
    return op1 + op2


def subtract(op1, op2):
    """Subtract given params"""
    return op1 - op2


def multiply(op1, op2):
    """Multiply given params"""
    return op1 * op2


def divide(op1, op2):
    """divide given params"""
    return op1 / op2


exitCommand: str = ''
while exitCommand != 'exit':
    operation = input(" + \n - \n * \n /")
    num1 = int(input("operand: "))
    num2 = int(input("operand: "))

    if operation == "+":
        print(add(num1, num2))
    if operation == "-":
        print(subtract(num1, num2))
    if operation == "*":
        print(multiply(num1, num2))
    if operation == "/":
        print(divide(num1, num2))

    exitCommand = input()

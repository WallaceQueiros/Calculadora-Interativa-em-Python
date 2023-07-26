def display_menu():
    print("==== CALCULATOR ====")
    print("[1]: Sum")
    print("[2]: Subtract")
    print("[3]: Multiply")
    print("[4]: Divide")
    print("[5]: Exit")


def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Cannot divide by zero.")


def calculate():
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the first number:  "))

    if operation == '+':
        result = sum_numbers(num1, num2)
    elif operation == '-':
        result = subtract_numbers(num1, num2)
    elif operation == '*':
        result = multiply_numbers(num1, num2)
    elif operation == '/':
        result = divide_numbers(num1, num2)
    else:
        raise ValueError('Invalid operation')

    print(f"Resultado: {result}")


calculate()

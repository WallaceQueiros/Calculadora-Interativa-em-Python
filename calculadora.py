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


while True:
    display_menu()

    operation = input("Enter the number operation: ")

    if operation == '5':
        print('EXIT...')
        break

    numb1 = float(input("Enter the first number: "))
    numb2 = float(input("Enter the first number:  "))

    if operation == '1':
        result = sum_numbers(numb1, numb2)
    elif operation == '2':
        result = subtract_numbers(numb1, numb2)
    elif operation == '3':
        result = multiply_numbers(numb1, numb2)
    elif operation == '4':
        result = divide_numbers(numb1, numb2)
    else:
        raise ValueError('Invalid operation')

    print(f"Result: {result}")

#!/usr/bin/env python3
# match_case_calculator.py (compatible Python 3.8.10)

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    operation = input("Choose the operation (+, -, *, /): ").strip()

    if operation == "+":
        result = num1 + num2
        print(f"The result is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result is {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result is {result}")
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    else:
        print("Invalid operation. Please choose +, -, * or /.")

if __name__ == "__main__":
    main()

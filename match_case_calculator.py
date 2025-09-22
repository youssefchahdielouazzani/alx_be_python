# match_case_calculator.py

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation
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
    print("Invalid operation. Please choose one of (+, -, *, /).")




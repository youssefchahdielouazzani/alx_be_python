# match_case_calculator.py

# Demander les deux nombres
num1 = float(input("Saisir le premier nombre : "))
num2 = float(input("Saisir le deuxième nombre : "))

# Demander l'opération
operation = input("Choisissez l'opération (+, -, *, /) : ")

# Effectuer le calcul avec if / elif / else
if operation == "+":
    result = num1 + num2
    print(f"Le résultat est {result}.")
elif operation == "-":
    result = num1 - num2
    print(f"Le résultat est {result}.")
elif operation == "*":
    result = num1 * num2
    print(f"Le résultat est {result}.")
elif operation == "/":
    if num2 == 0:
        print("Division par zéro impossible.")
    else:
        result = num1 / num2
        print(f"Le résultat est {result}.")
else:
    print("Opération invalide.")
:wq

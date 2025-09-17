num1 = float(input("Saisir le premier nombre : "))
num2 = float(input("Saisir le deuxième nombre : "))
operation = input("Choisissez l'opération (+, -, *, /) : ")

if operation == "+":
    print(f"Le résultat est {num1 + num2}.")
elif operation == "-":
    print(f"Le résultat est {num1 - num2}.")
elif operation == "*":
    print(f"Le résultat est {num1 * num2}.")
elif operation == "/":
    if num2 == 0:
        print("Division par zéro impossible.")
    else:
        print(f"Le résultat est {num1 / num2}.")
else:
    print("Opération invalide.")
# match_case_calculator.py compatible Python 3.8

num1 = float(input("Saisir le premier nombre : "))
num2 = float(input("Saisir le deuxième nombre : "))

operation = input("Choisir l'opération (+, -, *, /) : ")

if operation == "+":
    print("Résultat :", num1 + num2)
elif operation == "-":
    print("Résultat :", num1 - num2)
elif operation == "*":
    print("Résultat :", num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Erreur : Division par zéro impossible.")
    else:
        print("Résultat :", num1 / num2)
else:
    print("Opération invalide. Veuillez choisir parmi +, -, *, /.")

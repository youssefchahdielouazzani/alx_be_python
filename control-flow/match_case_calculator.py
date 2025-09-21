# match_case_calculator.py

# Demande des deux nombres
num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))

# Demande l'opération
operation = input("Choisissez l'opération (+, -, *, /): ")

# On utilise if / elif / else au lieu de match case
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erreur: division par zéro"
else:
    result = "Opération non valide"

print("Résultat:", result)

# multiplication_table.py

# Demander à l'utilisateur de saisir un nombre
num = int(input("Enter a number: "))

# Afficher la table de multiplication de ce nombre
print(f"Multiplication table of {num}:")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

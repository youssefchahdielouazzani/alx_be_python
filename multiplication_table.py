# multiplication_table.py

# Demander un nombre à l'utilisateur
number = int(input("Enter a number to see its multiplication table: "))

# Générer et afficher la table de multiplication
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")


# Fonction pour afficher le menu
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Fonction principale
def main():
    shopping_list = []  # Liste vide pour stocker les articles

    while True:  # Boucle pour le menu
        display_menu()
        choice = input("Enter your choice: ")

        # Ajouter un article
        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the list.")

        # Supprimer un article
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} is not in the list.")

        # Afficher la liste
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        # Quitter le programme
        elif choice == '4':
            print("Goodbye!")
            break

        # Gestion des choix invalides
        else:
            print("Invalid choice. Please try again.")

# Lancer le programme
if __name__ == "__main__":
    main()


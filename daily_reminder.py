# daily_reminder.py

# Demander la tâche
task = input("Enter your task: ")

# Demander la priorité
priority = input("Priority (high/medium/low): ").lower()

# Demander si c'est urgent
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Fonction pour générer le rappel
def remind_task(task, priority, time_bound):
    if priority == "high":
        message = f"'{task}' is a high priority task"
    elif priority == "medium":
        message = f"'{task}' is a medium priority task"
    elif priority == "low":
        message = f"'{task}' is a low priority task"
    else:
        message = f"'{task}' has an unknown priority"

    # Vérifier si la tâche est urgente
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    print("\nReminder:", message)

# Appeler la fonction
remind_task(task, priority, time_bound)

print("\nWell done on completing this project! Let the world hear about this milestone achieved. 🚀")


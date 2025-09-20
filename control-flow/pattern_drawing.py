# pattern_drawing.py

# Ask the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print '*' in each row
    for col in range(size):
        print("*", end="")  # stay on same line

    # After finishing one row, go to next line
    print()

    # Move to next row
    row += 1


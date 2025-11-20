# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    # After each row, print a newline
    print()
    row += 1

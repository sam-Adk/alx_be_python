# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop to print asterisks in the row
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()
    
    # Increment row counter
    row += 1

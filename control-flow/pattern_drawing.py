# define variable and prompt user to enter input
size = int(input("Enter the size of the pattern:"))

# Define the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to print each row of the square
while row < size:
    # For each row, use a for loop to print the asterisks side by side
    for col in range(size):
        print("*", end="")  # Print '*' without a newline
    print()  # Move to the next row
    row += 1  # Increment the row counter

print("Loop has ended.")

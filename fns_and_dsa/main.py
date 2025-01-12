#define function 

def perform_operation(num1, num2, operation):
  """
    Perform basic arithmetic operations.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float or str: The result of the operation, or an error message for invalid operations or division by zero.
    """
  if operation == "add":
    return num1 + num2
  
  elif operation == "subtract":
    return num1 - num2
  
  elif operation == "multiply":
    return num1 * num2
  
  elif operation == "divide":
    if num2 == 0:
      return "Error: Division by zero is not allowed"
    return num1/num2
  else:
    return "Error: invalid operation"
  
# main.py  
from arithmetic_operations import perform_operation

from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations Program")

    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

        # Call the perform_operation function
        result = perform_operation(num1, num2, operation)

        # Display the result
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
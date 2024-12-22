# prompt user input: two numbers and operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for operations
operation = (input("Choose operation (+, -, *, /):"))

# Match operation with numbers
match operation:
  case "+":
   result = num1 + num2
   print("The result", num1, "+", num2, "is", result)
  case "-":
    result = num1 - num2
    print("The result", num1, "-", num2, "is", result) 
  case "*":
   result = num1 * num2
   print("The result", num1, "*", num2, "is", result) 
  case "/":
        if num2 != 0:  # Handle division by zero
            result = num1 / num2
            print("The result of", num1, "/", num2, "is", result)
        else:
            print("Error: Division by zero is not allowed.")
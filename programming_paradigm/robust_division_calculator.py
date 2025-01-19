# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divides two numbers, handling errors gracefully."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt the division
        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."


# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
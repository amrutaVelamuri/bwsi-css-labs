"""
lab_1b.py
This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.
"""
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")


def request_sanitized_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print(f"===== Simple Calculator =====")
    
    # Fix 1: sanitize number inputs
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    
    # Fix 2: sanitize operation input
    valid_operations = ["add", "subtract", "multiply", "divide"]
    while True:
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        if operation in valid_operations:
            break
        print("Invalid operation. Please choose from add, subtract, multiply, divide.")

    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

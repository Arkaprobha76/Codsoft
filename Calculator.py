# A simple Python Programme to Make a calculator
def add(x, y):     # This Function is used to add two Numbers
    return x + y

def subtract(x, y):  # This Function is used to Subbtract two Numbers
    return x - y

def multiply(x, y):    # This Function is used to Multiply two Numbers
    return x * y

def divide(x, y):     # This Function is used to Divide two Numbers
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    try:
        choice = int(input("Enter operation choice (1/2/3/4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

        print("Result:", result)
        break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


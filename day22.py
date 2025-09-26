# Simple Calculator Program

def calculete(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
result = calculete(num1, num2, operation)   
print(f"The result is: {result}")
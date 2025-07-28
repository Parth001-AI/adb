#Create a program for calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return a ** 0.5

# Usage example
calc1 = Calculator()
print("Addition:", calc1.add(10, 5))    
print("Subtraction:", calc1.subtract(10, 5))
print("Multiplication:", calc1.multiply(10, 5))


#Implement a Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)


result = Calculator(10, 94)
print("Addition:", result.add())
print("Subtraction:", result.subtract())
print("Mutliplication:", result.multiply())
print("Division:", result.divide())

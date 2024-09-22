import math




class Calculator:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    
    def add(self):
        return self.value1 + self.value2
    
    def subtract(self):
        return self.value1 - self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def divide(self):
        if self.value2 == 0:
            return "Can't divide by zero"
        else:
            return self.value1 / self.value2
    
    def power(self):
        return math.pow(self.value1, self.value2)
    
    def square_root(self):
        if self.value1 < 0:
            return "cannot take the square root of a negative number"
        else:
            return math.sqrt(self.value1)
    
    def factorial(self):
        if self.value1 < 0:
            return "Factorial of a negative number is not defined"
        elif self.value1 == 0:
            return 1
        else:
            return math.factorial(self.value1)
    
    def logarithm(self):
        self.value2 = 10
        return math.log(self.value1, self.value2)

    def trigonometric_functions(self):
        if self.value2 == "sin":
            return math.sin(self.value1)
        elif self.value2 == "cos":
            return math.cos(self.value1)
        elif self.value2 == "tan":
            return math.tan(self.value1)
        else:
            return "invalid trigonometric functions"



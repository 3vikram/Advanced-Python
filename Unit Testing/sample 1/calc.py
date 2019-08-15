import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return  a - b

    def multiply(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def square_root(self, a):
        return math.sqrt(a)

    def power(self, a, b):
        return pow(a, b)

if __name__ == "__main__":
    run = Calculator()
    print(run.add(5, 6))
    print(run.subtract(6, 3))
    print(run.multiply(6, 2))
    print(run.division(4, 3))
    print(run.square_root(45))
    print(run.power(5, 8))

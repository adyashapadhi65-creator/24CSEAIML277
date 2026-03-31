# Q2. Write a program using multilevel inheritance to perform
# addition, subtraction, multiplication, division

class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Add(Base):
    def addition(self):
        print("Addition:", self.a + self.b)

class Sub(Add):
    def subtraction(self):
        print("Subtraction:", self.a - self.b)

class Mul(Sub):
    def multiplication(self):
        print("Multiplication:", self.a * self.b)

class Div(Mul):
    def division(self):
        if self.b != 0:
            print("Division:", self.a / self.b)
        else:
            print("Division not possible")


obj = Div(10, 5)
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
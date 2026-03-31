# Q1. Write a program to create a class for employee using parameterized constructor
# and calculate gross pay (TA = 10%, DA = 40%)

class Employee:
    def __init__(self, empid, name, basic):
        self.empid = empid
        self.name = name
        self.basic = basic

    def calculate(self):
        ta = 0.10 * self.basic
        da = 0.40 * self.basic
        gross = self.basic + ta + da
        return gross

    def display(self):
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basic)
        print("Gross Pay:", self.calculate())


emp = Employee(101, "Pallavi", 20000)
emp.display()
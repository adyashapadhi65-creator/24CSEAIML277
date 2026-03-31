## Q1. What are positional (required) arguments? Write a function to add two numbers using positional arguments
def add(a, b):
    return a + b

print("Q1 Output:", add(5, 10))


# Q2. Write a program using positional arguments to find product of two numbers
def product(a, b):
    return a * b

print("Q2 Output:", product(4, 5))


# Q3. What are keyword arguments? Write a function using keyword arguments to display name and age
def display(name, age):
    print("Name:", name)
    print("Age:", age)

print("Q3 Output:")
display(name="Ravi", age=20)
display(age=25, name="Anil")


# Q4. Write a program using keyword arguments to display student details
def student(name, course):
    print("Name:", name)
    print("Course:", course)

print("Q4 Output:")
student(course="B.Tech", name="Sita")


# Q5. Write a program using default arguments to display student name
def greet(name="Student"):
    print("Hello", name)

print("Q5 Output:")
greet("Ravi")
greet()


# Q6. Write a program using default arguments
def bill(amount=100):
    print("Bill amount:", amount)

print("Q6 Output:")
bill(500)
bill()


# Q7. What are arbitrary arguments? Write a program using *args
def total(*nums):
    print("Sum =", sum(nums))

print("Q7 Output:")
total(10, 20, 30)

#Q8. WAP using *args

def total(*nums):
    s = 0
    for i in nums:
        s += i
    print("Sum =", s)

total(10, 20, 30, 40)




# Q9. Write a program using **kwargs
def employee(**details):
    for k, v in details.items():
        print(k, ":", v)

print("Q8 Output:")
employee(name="Kiran", id=101, dept="IT")


# Q10. Differentiate between *args and **kwargs
print("Q9 Output:")
print("*args stores values as tuple")
print("**kwargs stores values as dictionary")
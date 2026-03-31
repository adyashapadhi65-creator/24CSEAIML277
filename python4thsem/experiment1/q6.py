# Q6. WAP to swap 2 numbers without using third variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Before swap a =", a, "b =", b)

a, b = b, a

print("After swap a =", a, "b =", b)
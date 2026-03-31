# Q7. Print Fibonacci series of a number (using while loop)
n = int(input("Enter a number: "))
a, b = 0, 1

print(a, b, end=" ")

c = 0
while c <= n:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
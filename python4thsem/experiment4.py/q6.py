# Q6. Find the factorial of a number (using while loop)
num = int(input("Enter a number: "))
fact = 1
n = num

while n > 0:
    fact *= n
    n -= 1

print("Factorial is:", fact)
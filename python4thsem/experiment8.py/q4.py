#Write a function to find factorial of a number
def factorial(n):
    if n < 0:
        return "Invalid"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter number: "))
print(factorial(n))
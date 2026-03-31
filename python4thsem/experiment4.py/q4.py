# Q4. WAP to find the sum of digits of a number
num = int(input("Enter a number: "))
s = 0

while num > 0:
    s += num % 10
    num = num // 10

print("Sum of digits =", s)
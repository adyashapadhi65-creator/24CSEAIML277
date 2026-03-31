# Q2. WAP to test a number is prime or not
num = int(input("Enter a number: "))
n = 2
flag = True

while n <= num // 2:
    if num % n == 0:
        flag = False
        break
    n += 1

if flag and num > 1:
    print("Prime number")
else:
    print("Not a prime number")
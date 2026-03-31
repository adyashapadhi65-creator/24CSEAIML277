# Q5. WAP to test a number is palindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not a palindrome")
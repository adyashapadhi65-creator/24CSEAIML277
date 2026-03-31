# Q3. WAP to find GCD of three numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

i = 1
gcd = 1

while i <= a and i <= b and i <= c:
    if a % i == 0 and b % i == 0 and c % i == 0:
        gcd = i
    i += 1

print("GCD =", gcd)
#WAP to generate all prime numbers within a given range from m to n.
m = int(input("Enter start number: "))
n = int(input("Enter end number: "))

primes = []

for i in range(m, n + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

print("Prime numbers:", primes)

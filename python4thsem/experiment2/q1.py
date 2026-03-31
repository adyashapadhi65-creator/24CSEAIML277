# Q1. Display simple interest and compound interest
p = float(input("Enter the principal: "))
t = float(input("Enter the time: "))
r = float(input("Enter the rate: "))

si = (p * t * r) / 100
ci = p * (1 + r/100) ** t

print("The simple interest is:", si)
print("The compound interest is:", ci)
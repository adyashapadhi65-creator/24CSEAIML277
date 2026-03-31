# Q7. WAP to input marks of 3 subjects, find sum and percentage
a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

total = a + b + c
percentage = (total / 300) * 100

print("Total marks =", total)
print("Percentage =", percentage)
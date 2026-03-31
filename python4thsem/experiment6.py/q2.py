#WAP to create a dictionary and input keys and values, then create another dictionary which collects the values of the first dictionary as keys and the keys of the first dictionary as values, and then display both.
d1 = {}
n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

d2 = {}
for key, value in d1.items():
    d2[value] = key

print("First Dictionary:", d1)
print("Second Dictionary:", d2)
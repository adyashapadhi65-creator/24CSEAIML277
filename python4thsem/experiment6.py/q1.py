#WAP to create a list which contains some group of fruits names. Display the elements from last index to 1st index (reversely), and also show the length of each element. Create another list which collects the reverse of each element.
fruits = ["apple", "banana", "mango", "orange", "grapes"]

print("Elements from last index to first index:")
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])

print("\nLength of each element:")
for fruit in fruits:
    print(fruit, "=", len(fruit))

reversed_fruits = []
for fruit in fruits:
    reversed_fruits.append(fruit[::-1])

print("\nList containing reverse of each element:")
print(reversed_fruits)
#Write a program to create a list containing natural numbers from a given input (create using for loop), find the sum, average, largest and smallest in the list. Create another list which contains all the members of the list except numbers divisible by 3.
n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

total = sum(lst)
avg = total / len(lst)
largest = max(lst)
smallest = min(lst)

new_list = []
for x in lst:
    if x % 3 != 0:
        new_list.append(x)

print("List:", lst)
print("Sum:", total)
print("Average:", avg)
print("Largest:", largest)
print("Smallest:", smallest)
print("New List:", new_list)
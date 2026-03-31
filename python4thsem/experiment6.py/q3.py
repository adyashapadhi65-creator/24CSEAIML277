#WAP to input a sentence, store each word as an element into a list (List1), display the elements of the list along with index numbering, create another list using enumerate() (List2) having elements as a series of numbers.
sentence = input("Enter a sentence: ")

list1 = sentence.split()

print("Elements with index:")
for index, word in enumerate(list1):
    print(index, word)

list2 = list(range(len(list1)))

print("Second list:", list2)
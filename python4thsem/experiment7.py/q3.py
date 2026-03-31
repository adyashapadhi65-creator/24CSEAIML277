#WAP to create a string which contains a paragraph, now find:
#i) Count how many vowels exist
#ii) Count how many palindrome words exist
#iii) Print each word in reverse order
text = input("Enter a paragraph: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

words = text.split()

palindrome_count = 0
for w in words:
    if w == w[::-1]:
        palindrome_count += 1

reversed_words = []
for w in words:
    reversed_words.append(w[::-1])

print("Vowel count:", vowel_count)
print("Palindrome words:", palindrome_count)
print("Reversed words:", reversed_words)
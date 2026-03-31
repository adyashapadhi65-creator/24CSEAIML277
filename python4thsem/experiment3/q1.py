# Q1. WAP to test a string is palindrome or not
string = input("Enter a string: ")
reverse_string = string[::-1]

if string == reverse_string:
    print("Palindrome")
else:
    print("Not palindrome")
#Write a function to check whether a number is even or odd
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
print(check_even(num))
# Q6. WAP to check whether an alphabet is vowel or consonant
ch = input("Enter an alphabet: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print("It is a vowel")
else:
    print("It is a consonant")
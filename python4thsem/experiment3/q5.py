# Q5. WAP to input marks (out of 50), find percentage and display grade
marks = float(input("Enter marks out of 50: "))
percentage = (marks / 50) * 100

print("Percentage =", percentage)

if percentage >= 90:
    print("Grade O")
elif percentage >= 80:
    print("Grade E")
elif percentage >= 70:
    print("Grade A")
elif percentage >= 60:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Grade F")
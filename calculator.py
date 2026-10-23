# Student Grade Calculator

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
english = float(input("Enter English marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
computer = float(input("Enter Computer marks: "))

# Calculate total and percentage
total = maths + english + physics + chemistry + computer
percentage = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

# Calculate grade
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")


















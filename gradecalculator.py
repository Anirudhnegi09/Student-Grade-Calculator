
# Program: Student Grade Calculator
# Author: Anirudh Negi

# Input as strings (simulate user input)
name=input("Enter your name")
marks_str=input("enter your marks")
total_str = "100"

# Convert to proper types
marks = int(marks_str)
total = int(total_str)

# Calculate percentage
percentage = (marks / total) * 100

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "F"

# Is passed (bool)
is_passed = percentage >= 40

# Display
print("Student Name:", name)
print("Marks:", marks, "| Type:", type(marks))
print("Total:", total, "| Type:", type(total))
print("Percentage:", percentage, "| Type:", type(percentage))
print("Grade:", grade, "| Type:", type(grade))
print("Is Passed:", is_passed, "| Type:", type(is_passed))
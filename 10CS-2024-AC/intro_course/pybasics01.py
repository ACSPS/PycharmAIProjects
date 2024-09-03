# Variables
# Variables are used to store data in a program.
# In python, variables are created by assigning a value to a meaningful name.
# The value of a variable can be changed or updated throughout the program.
# Variables contain one type of data at a time, but the data type can change.
# Data types in Python include integers, floats, strings, and booleans.
# Must indent a line after colon

name = "Fred" # this variable contains a string (text)
age = 5 # this variable contains an integer 'int' which is a whole number
salary = 1000.50
is_student = True


name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
is_student = bool(input("Are you a student? (True/False): "))

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))
print("Name:", name)
if is_student == True:
    student = "Yes"
# Why do we need a else statement here?
else:
    student = "No"
# the following is an F-String
print(f"{name} is {age} years old and earns $ {salary} per month. Is he a student? {is_student}")
# Fred is 15 years old and earns $ 1000.50 per month. Is he a student? True
print(f"{name} is {age} years old and earns ${salary}0 per month. Is he a student? {student}")
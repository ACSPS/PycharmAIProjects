import os
repeat = "yes"
while repeat == "yes":
    # Get the user to input their name
    # Get the user to input their birth year
    # Calculate the user's age
    # Expected output: "Hi NAME, you are 15 years old."
    # Test the program with your own name and birth year
    # Test with my name and birth year 1976

    name = input("Enter your name: ").strip()
    birth_year = int(input("Enter your birth year: ").strip())
    age = 2024 - birth_year

    birthday = input("Have you had your birthday this year? (Yes/No): ").lower().strip()
    if birthday == "no":
        age = age - 1
    print(f"Hi {name}, you are {age} years old.")

    repeat = input("Would you like to run the program again? (Yes/No): ").lower().strip()
    os.system('cls')
# if repeat == "no": thank the user and exit the program
print("Thank you for using the age calculator")

sports = ["Basketball", 35, 5.5, True]
'''
print(sports)
print(type(sports))
print(len(sports))
print(sports[0])
print(sports[-1])
print(sports[-2])
print(sports[0:3])
# print(type(sports[0]))
# print(type(sports[1]))
# print(type(sports[2]))
# print(type(sports[3]))

for sport in sports:
    print(type(sport))
    print(sport)


new_sport =input("Enter your favourite sport:")
sports.append(new_sport)
print("Updated sports list:", sports)
'''


import os

file_path = 'sports02.txt'

#Function to read the sports list from the file
def read_sports(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

# A function consists of a function definition
# A function definition consists brackets
#Function to write the sports list from the file
def write_sports(file_path, sports_list):
    with open(file_path, 'w') as file:
        for sport in sports_list:
            file.write(f"{sport}\n")

repeat = "yes"
while repeat == "yes":
# read the current sports list from  the file
    sports = read_sports(file_path) # Empty list

    #Get user input
    new_sport = input("Enter your favourite sport: ").capitalize().strip() # Get user input

    # Append the new sport if provided
    if new_sport:
        if new_sport in sports:
            print(f"{new_sport} is already in the list")
        else:
            sports.append(new_sport)
            print("Updated sports list: ", sports)
    else:
        print("No new sport added. ")
        # Write the updated sports list back to the file
        write_sports(file_path, sports)
        # print the updated sports list
        print("Sports list:") # Fix this line

    for i, sport in enumerate(sports): # loop through the sports list with index
        print(f"Sport {i+1}: {sport}") # Print the index and sport

    repeat = input("Do you want to add another sport? (yes/no): ").strip().lower() # Ask if the user wants to add another sport
print("Exiting the program. ")


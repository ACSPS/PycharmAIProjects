import os


file_path = 'sports03.txt'

sports[]

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        sports = [line.strip() for line in file.readlines()]

repeat = "yes"
while repeat == "yes":
        new_sport = input ("Enter your favourite sport: ")

        if new_sport
            if new_sport in sports:
                print(f"{new_sport} is already in the list")
            else:
                sports.append(new_sport)
                print("Updated sport list: ", sports)
        else:
            print("No new sport added")

        with open(file_path, 'w') as file:
            for sport in sports:
                file.write(f"{sport}\n")


        print("Sports list:")
        for i, sport in enumerate(sports):
            print(f"{i+1}: {sport}")



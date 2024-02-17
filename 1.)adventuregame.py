# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")

# Task 2: Add to existing code, to provide two questions and the outcomes if the user chooses "cave"
elif place == "cave":
    action = input("Would you like to: light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Your path will be well lit.")
    elif action == "proceed in the dark":
        print("Be cautious of what you can't see.")
        
else:  # Task 3: Use a pass statement for the default path: for invalid choices
     pass

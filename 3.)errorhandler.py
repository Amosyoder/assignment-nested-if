# Task 1: Code Correction

try:   
    x = 1 / 0
except ZeroDivisionError:
    pass

try: # Task 2: Enhance the program to handle other errors: such as TypeError when trying to divide a number by a string
    y = 1 / "5"
except TypeError:
    pass
    
# Task 3 Ask the user for filename, if filename doesn not exist use pass statement to handle error silently.
filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:")   
        print(content)
except FileNotFoundError:
    pass
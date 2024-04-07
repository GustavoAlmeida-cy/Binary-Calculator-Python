# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
from scripts.calc_functions import binary_addition # Bring the calculation functions

# Program title
print(f"{tcolors.HEADER}-----[ Binary Calculator ]-----\n{tcolors.ENDC}")

# Multiple choice message and logic
print(f"{tcolors.WARNING}| What type of calculation do you wish? (type the correct number corresponding to the right option){tcolors.ENDC}")
choice = input((f"{tcolors.WARNING}| 1. Addition\n| 2. Subtract\n\n| : {tcolors.ENDC}"))

if choice != "1" and choice != "2":
    while choice != "1" and choice != "2":
        print(f"{tcolors.FAIL}\n| Invalid choice! Please type other option{tcolors.ENDC}")
        choice = input((f"{tcolors.WARNING}\n| 1. Addition\n| 2. Subtract\n\n| : {tcolors.ENDC}"))

# Reading user inputs
first_num = input(f"{tcolors.HEADER}\n| Type the first number: {tcolors.ENDC}")
second_num = input(f"{tcolors.HEADER}\n| Type the second number: {tcolors.ENDC}")

if choice == "1":
    binary_addition(first_num, second_num)

# Program end
print(f"{tcolors.HEADER}\n-------[ PROGRAM END ]-------{tcolors.ENDC}")
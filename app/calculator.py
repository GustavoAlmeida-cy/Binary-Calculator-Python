# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
import scripts.calc_functions # Bring the calculation functions

# Functions
def multiple_choice_logic(a): # Check the option chosen by the user
    if a != '1' and a != '2' and a != '3' and a != '4':
        return True
    else:
        return False

# Program title
print(f'{tcolors.HEADER}\n-----[ BINARY CALCULATOR ]-----\n{tcolors.ENDC}')

# Multiple choice message and logic
print(f'{tcolors.WARNING}| What type of calculation do you wish? (type the correct number corresponding to the right option){tcolors.ENDC}')
choice = input((f'{tcolors.WARNING}\n| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n| 4. Division\n\n| : {tcolors.ENDC}'))

mult_ch_logic_value = multiple_choice_logic(choice)

if mult_ch_logic_value: # Validates whether the option chosen by the user is correct
    while mult_ch_logic_value:
        print(f'{tcolors.FAIL}\n| Invalid choice! Please type other option{tcolors.ENDC}')
        choice = input((f'{tcolors.WARNING}\n| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n| 4. Division\n\n| : {tcolors.ENDC}'))
        mult_ch_logic_value = multiple_choice_logic(choice)

choice = int(choice)
msg = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']

print(f'{tcolors.HEADER}\n| [ {msg[choice - 1]} ] {tcolors.ENDC}')

# Reading user inputs
first_num = input(f'{tcolors.HEADER}\n| Type the first number: {tcolors.ENDC}')
second_num = input(f'{tcolors.HEADER}\n| Type the second number: {tcolors.ENDC}')

# Logic of choice to choose what type of calculation the user wish
match choice:
    case 1:
        scripts.calc_functions.binary_addition(first_num, second_num)
    case 2:
        scripts.calc_functions.binary_subtraction(first_num, second_num)
    case 3:
        scripts.calc_functions.binary_multiplication(first_num, second_num)
    case 4:
        scripts.calc_functions.binary_division(first_num, second_num)

# Program end
print(f'{tcolors.HEADER}\n-------[ PROGRAM END ]-------\n{tcolors.ENDC}')

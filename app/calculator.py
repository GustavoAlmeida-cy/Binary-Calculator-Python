# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
import scripts.calc_functions # Bring the calculation functions

# Functions
def multiple_choice_logic(choice): # Check the option chosen by the user
    if choice != '1' and choice != '2' and choice != '3' and choice != '4':
        return True
    else:
        return False

def multiple_choice_YN(choice): # Check the option chosen by the user
    if choice != 'Y' and choice != 'N':
        return True
    else:
        return False
    
def is_binary(input_str): #Checks if the input string represents a valid binary number
    if input_str == "" or input_str == " ":
        return False
        
    for char in input_str:
        if char not in '01.':
            return False
    return True

def main():
    # Multiple choice message and logic
    print(f'{tcolors.WARNING}\n| What type of calculation do you wish? (type the correct number corresponding to the right option){tcolors.ENDC}')
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

    # Check if the input is a valid binary number
    if not is_binary(first_num) or not is_binary(second_num):
        while not is_binary(first_num) or not is_binary(second_num):
            print(f'{tcolors.FAIL}\n| Invalid numbers! Please type other numbers{tcolors.ENDC}')
            first_num = input(f'{tcolors.HEADER}\n| Type the first number: {tcolors.ENDC}')
            second_num = input(f'{tcolors.HEADER}\n| Type the second number: {tcolors.ENDC}')

    # Logic of choice to choose what type of calculation the user wish
    match choice:
        case 1:
            scripts.calc_functions.binary_calculation_DA(first_num, second_num, 1)
        case 2:
            scripts.calc_functions.binary_calculation_DA(first_num, second_num, 2)
        case 3:
            scripts.calc_functions.binary_calculation_DA(first_num, second_num, 3)
        case 4:
            scripts.calc_functions.binary_calculation_DA(first_num, second_num, 4)

# Program title
print(f'{tcolors.HEADER}\n-----[ BINARY CALCULATOR ]-----\n{tcolors.ENDC}')

choice = "Y"

while choice == "Y":
    main()

    choice = input(f"{tcolors.WARNING}| Do you like to do another calculation? (Y/N)\n\n| : {tcolors.ENDC}").upper()

    controller = multiple_choice_YN(choice)

    if controller: # Validates whether the option chosen by the user is correct
        while controller:
            print(f'{tcolors.FAIL}\n| Invalid choice! Please try again{tcolors.ENDC}')
            choice = input(f"{tcolors.WARNING}\n| Do you like to do another calculation? (Y/N)\n\n| : {tcolors.ENDC}").upper()
            controller = multiple_choice_YN(choice)
            
# Program footer
print(f'{tcolors.HEADER}\n-------[ PROGRAM END ]-------\n{tcolors.ENDC}')

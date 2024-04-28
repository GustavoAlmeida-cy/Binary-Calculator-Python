# Importing scripts
from scripts.terminal_colors import tcolors as TC # Enable terminal colors
import scripts.calc_functions  as CF# Bring the calculation functions
import scripts.basic_functions as BF # Bring the basic functions

def main():
    # Multiple choice message and logic
    print(f'{TC.WARNING}\n| What type of calculation do you wish? (type the correct number corresponding to the right option){TC.ENDC}')
    choice = input((f'{TC.WARNING}\n| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n| 4. Division\n\n| : {TC.ENDC}'))

    mult_ch_logic_value = BF.multiple_choice_logic(choice)

    if mult_ch_logic_value: # Validates whether the option chosen by the user is correct
        while mult_ch_logic_value:
            print(f'{TC.FAIL}\n| Invalid choice! Please type other option{TC.ENDC}')
            choice = input((f'{TC.WARNING}\n| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n| 4. Division\n\n| : {TC.ENDC}'))
            mult_ch_logic_value = BF.multiple_choice_logic(choice)

    choice = int(choice)
    msg = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']

    print(f'{TC.HEADER}\n| [ {msg[choice - 1]} ] {TC.ENDC}')

    # Reading user inputs
    first_num = input(f'{TC.HEADER}\n| Type the first number: {TC.ENDC}')
    second_num = input(f'{TC.HEADER}\n| Type the second number: {TC.ENDC}')

    # Check if the input is a valid binary number
    if not BF.is_binary(first_num) or not BF.is_binary(second_num):
        while not BF.is_binary(first_num) or not BF.is_binary(second_num):
            print(f'{TC.FAIL}\n| Invalid numbers! Please type other numbers{TC.ENDC}')
            first_num = input(f'{TC.HEADER}\n| Type the first number: {TC.ENDC}')
            second_num = input(f'{TC.HEADER}\n| Type the second number: {TC.ENDC}')

    # Logic of choice to choose what type of calculation the user wish
    match choice:
        case 1:
            CF.binary_calculation_DA(first_num, second_num, 1)
        case 2:
            CF.binary_calculation_DA(first_num, second_num, 2)
        case 3:
            CF.binary_calculation_DA(first_num, second_num, 3)
        case 4:
            CF.binary_calculation_DA(first_num, second_num, 4)

# Program title
print(f'{TC.HEADER}\n-----[ BINARY CALCULATOR ]-----\n{TC.ENDC}')

choice = "Y"

while choice == "Y":
    main()

    choice = input(f"{TC.WARNING}| Would you like to do another calculation? (Y/N)\n\n| : {TC.ENDC}").upper()

    controller = BF.multiple_choice_YN(choice)

    if controller: # Validates whether the option chosen by the user is correct
        while controller:
            print(f'{TC.FAIL}\n| Invalid choice! Please try again{TC.ENDC}')
            choice = input(f"{TC.WARNING}\n| Would you like to do another calculation? (Y/N)\n\n| : {TC.ENDC}").upper()
            controller = BF.multiple_choice_YN(choice)
            
# Program footer
print(f'{TC.HEADER}\n-------[ PROGRAM END ]-------\n{TC.ENDC}')

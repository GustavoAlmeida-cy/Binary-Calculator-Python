# Importing scripts
import scripts.calc_functions  as CF# Bring the calculation functions
import scripts.basic_functions as BF # Bring the basic functions

# Importing libs
from rich.console import Console
console = Console()

# Main function
def app():
    # Multiple choice message and logic
    console.print(f'\n[bold][cyan]| What type of calculation do you wish? (type the correct number corresponding to the right option)[/][/]')
    choice = console.input((f'\n[bold][cyan][orange1]| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n\n[/]| : [/][/]'))

    mult_ch_logic_value = BF.multiple_choice_logic(choice)

    if mult_ch_logic_value: # Validates whether the option chosen by the user is correct
        while mult_ch_logic_value:
            console.print(f'\n[bold][red]| [underline]Invalid choice! Please type other option.[/][/][/]')
            choice = console.input((f'\n[bold][cyan][orange1]| 1. Addition\n| 2. Subtraction\n| 3. Multiplication\n\n[/]| : [/][/]'))
            mult_ch_logic_value = BF.multiple_choice_logic(choice)

    choice = int(choice)
    msg = ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION']

    console.print(f'\n[bold][orange1]| [ {msg[choice - 1]} ][/][/]')

    # Reading user inputs
    first_num = console.input(f'\n[bold][cyan]| Type the first number: [/][/]')
    second_num = console.input(f'\n[bold][cyan]| Type the second number: [/][/]')

    # Check if the input is a valid binary number
    if not BF.is_binary(first_num) or not BF.is_binary(second_num):
        while not BF.is_binary(first_num) or not BF.is_binary(second_num):
            console.print(f'\n[bold][red]| [underline]Invalid numbers! Please type other numbers.[/][/][/]')
            first_num = console.input(f'\n[bold][cyan]| Type the first number: [/][/]')
            second_num = console.input(f'\n[bold][cyan]| Type the second number: [/][/]')

    # Logic of choice to choose what type of calculation the user wish
    match choice:
        case 1:
            CF.binary_calculation_BA(first_num, second_num, 1)
        case 2:
            CF.binary_calculation_BA(first_num, second_num, 2)
        case 3:
            CF.binary_calculation_BA(first_num, second_num, 3)

# Program start
if __name__ == "__main__":
    # Program title
    console.print(f'\n[bold][reverse]|========================================[ BINARY CALCULATOR ]=======================================|[/][/]\n')

    choice = "Y"
    while choice == "Y":
        app()

        choice = console.input(f"[bold][cyan]| Would you like to do another calculation? [orange1](Y/N)\n\n[/]| : [/][/]").upper()
        controller = BF.multiple_choice_YN(choice)

        if controller: # Validates whether the option chosen by the user is correct
            while controller:
                console.print(f'\n[bold][red]| [underline]Invalid choice! Please try again[/][/][/]')
                choice = console.input(f"\n[bold][cyan]| Would you like to do another calculation? [orange1](Y/N)\n\n[/]| : [/][/]").upper()
                controller = BF.multiple_choice_YN(choice)
                
    # Program footer
    console.print(f'\n[bold][reverse]|===========================================[ PROGRAM END ]==========================================|[/][/]\n')

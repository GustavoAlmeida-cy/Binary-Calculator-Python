# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
from scripts.convert_functions import binary_to_decimal, decimal_to_binary # Bring the convert functions

# Functions
def binary_addition(first_b_num:str, second_b_num:str): # Addition function
    # print(f"{tcolors.WARNING}\n - Before decimal conversion\n First number: {first_b_num}\n Second number: {second_b_num}\n{tcolors.ENDC}") # Debug comment!
    
    # Converting Binary to Decimal
    first_d_num = binary_to_decimal(first_b_num)
    second_d_num = binary_to_decimal(second_b_num)
    
    # print(f"{tcolors.WARNING}\n - After decimal conversion\n First number: {first_d_num}\n Second number: {second_d_num}\n{tcolors.ENDC}") # Debug comment!
    
    decimal_result = first_d_num + second_d_num
    binary_result = decimal_to_binary(decimal_result)

    return print(f"{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{tcolors.ENDC}"), print(f"{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{tcolors.ENDC}")

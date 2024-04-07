# Importing scripts
from terminal_colors import tcolors # Enable terminal colors
from conversions import binary_to_decimal, decimal_to_binary # Bring the conversions functions

# Program title
print(f"{tcolors.HEADER}-----[ Binary Calculator ]-----\n{tcolors.ENDC}")

# Addition function
def binary_addition(first_b_num:str, second_b_num:str):
    # print(f"{tcolors.WARNING}\n - Before decimal conversion\n First number: {first_b_num}\n Second number: {second_b_num}\n{tcolors.ENDC}") # Debug comment!
    
    # Converting Binary to Decimal
    first_d_num = binary_to_decimal(first_b_num)
    second_d_num = binary_to_decimal(second_b_num)
    
    # print(f"{tcolors.WARNING}\n - After decimal conversion\n First number: {first_d_num}\n Second number: {second_d_num}\n{tcolors.ENDC}") # Debug comment!
    
    decimal_result = first_d_num + second_d_num
    binary_result = decimal_to_binary(decimal_result)

    print(f"{tcolors.OKCYAN}\n [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{tcolors.ENDC}")
    print(f"{tcolors.OKGREEN}\n [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{tcolors.ENDC}")

# Reading user inputs
first_num = input(f"{tcolors.HEADER}\n Type the first number: {tcolors.ENDC}")
second_num = input(f"{tcolors.HEADER}\n Type the second number: {tcolors.ENDC}")

binary_addition(first_num, second_num)

# Program end
print(f"{tcolors.HEADER}\n-------[ PROGRAM END ]-------{tcolors.ENDC}")

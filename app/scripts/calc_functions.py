# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
import scripts.convert_functions # Bring the convert functions

# Functions

# Calculation functions - Decimal arithmetic
def binary_addition(first_b_num:str, second_b_num:str): # Addition function    
    # Converting Binary to Decimal
    first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
    second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)
        
    # Decimal calculation and Converting Decimal to Binary
    decimal_result = first_d_num + second_d_num
    binary_result = scripts.convert_functions.decimal_to_binary(decimal_result)

    return print(f'{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{tcolors.ENDC}'), print(f'{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{tcolors.ENDC}')

def binary_subtraction(first_b_num:str, second_b_num:str): # Subtraction function
    # Converting Binary to Decimal
    first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
    second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)
    
    # Decimal calculation and Converting Decimal to Binary
    decimal_result = first_d_num - second_d_num
    binary_result = scripts.convert_functions.decimal_to_binary(decimal_result)

    return print(f'{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} - {second_d_num} = {decimal_result}{tcolors.ENDC}'), print(f'{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} - {second_b_num} = {binary_result}\n{tcolors.ENDC}')

def binary_multiplication(first_b_num:str, second_b_num:str): # Multiplication function
    # Converting Binary to Decimal
    first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
    second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)
    
    # Decimal calculation and Converting Decimal to Binary
    decimal_result = first_d_num * second_d_num
    binary_result = scripts.convert_functions.decimal_to_binary(decimal_result)

    return print(f'{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} * {second_d_num} = {decimal_result}{tcolors.ENDC}'), print(f'{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} * {second_b_num} = {binary_result}\n{tcolors.ENDC}')

def binary_division(first_b_num:str, second_b_num:str): # Division function
    # Converting Binary to Decimal
    first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
    second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)
    
    # Decimal calculation and Converting Decimal to Binary
    decimal_result = first_d_num // second_d_num
    binary_result = scripts.convert_functions.decimal_to_binary(decimal_result)

    return print(f'{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} / {second_d_num} = {decimal_result}{tcolors.ENDC}'), print(f'{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} / {second_b_num} = {binary_result}\n{tcolors.ENDC}')

# Importing scripts
from scripts.terminal_colors import tcolors # Enable terminal colors
import scripts.convert_functions # Bring the convert functions

# Functions
def is_float_binary(binary): # Check if the number is decimal or float
    # Split the binary number into integer and fractional parts
    parts = binary.split('.')
    
    # Ensure there are two parts
    if len(parts) != 2:
        return False

    integer_part, fractional_part = parts

    # Check if both parts consist only of '0's and '1's
    if not all(bit in '01' for bit in integer_part) or not all(bit in '01' for bit in fractional_part):
        return False

    # Check if there's at least one '1' in the fractional part
    if '1' not in fractional_part:
        return False

    return True

# Calculation functions - Decimal arithmetic
def binary_addition(first_b_num:str, second_b_num:str): # Addition function    
    # Check which type of conversion will be
    if is_float_binary(first_b_num) or is_float_binary(second_b_num): # If any number is a float number the following code wil be executed
        # Check which the type of each one
        match is_float_binary(first_b_num): # If the first number is a float
            case True:
                first_d_num = scripts.convert_functions.float_b_to_float_d(first_b_num) 
            case False:
                first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num) # Convert to integer

        # Check which the type of each one
        match is_float_binary(second_b_num): # If the first number is a float
            case True:
                second_d_num = scripts.convert_functions.float_b_to_float_d(second_b_num) # Convert to float
            case False:
                second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num) # Convert to integer

        # Decimal calculation and converting decimal to binary
        decimal_result = round(first_d_num + second_d_num, 3)
        binary_result = scripts.convert_functions.float_d_to_float_b(decimal_result)
    else:
        # Converting binary to integer
        first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
        second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)

        # Decimal calculation and converting decimal to binary
        decimal_result = first_d_num + second_d_num
        binary_result = scripts.convert_functions.decimal_to_binary(decimal_result)

    return print(f'{tcolors.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{tcolors.ENDC}'), print(f'{tcolors.OKGREEN}\n| [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{tcolors.ENDC}')

def binary_subtraction(first_b_num:str, second_b_num:str): # Subtraction function
     # Check which type of conversion will be
    if is_float_binary(first_b_num) or is_float_binary(second_b_num): # If any number is a float number the following code wil be executed
        # Check which the type of each one
        match is_float_binary(first_b_num): # If the first number is a float
            case True:
                first_d_num = scripts.convert_functions.float_b_to_float_d(first_b_num) 
            case False:
                first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num) # Convert to integer

        # Check which the type of each one
        match is_float_binary(second_b_num): # If the first number is a float
            case True:
                second_d_num = scripts.convert_functions.float_b_to_float_d(second_b_num) # Convert to float
            case False:
                second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num) # Convert to integer

        # Decimal calculation and converting decimal to binary
        decimal_result = round(first_d_num - second_d_num, 3)
        binary_result = scripts.convert_functions.float_d_to_float_b(decimal_result)
    else:
        # Converting binary to integer
        first_d_num = scripts.convert_functions.binary_to_decimal(first_b_num)
        second_d_num = scripts.convert_functions.binary_to_decimal(second_b_num)

        # Decimal calculation and converting decimal to binary
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

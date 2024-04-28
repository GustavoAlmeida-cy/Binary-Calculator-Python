# Importing scripts
from scripts.terminal_colors import tcolors as TC# Enable terminal colors
import scripts.convert_functions as ConF # Bring the convert functions
import scripts.basic_functions as BF # Bring the basic functions


# Calculation functions - Decimal arithmetic

def binary_calculation_DA(first_b_num:str, second_b_num:str, choice):
    # Check which type of conversion will be
    validator = False

    if BF.is_float_binary(first_b_num) or BF.is_float_binary(second_b_num): # If any number is a float number the following code wil be executed
        # Check which type is and convert
        match BF.is_float_binary(first_b_num): # If the first number is a float
            case True:
                first_d_num = ConF.float_b_to_float_d(first_b_num) # Convert to float
            case False:
                first_d_num = ConF.binary_to_decimal(first_b_num) # Convert to integer

        # Check which type is and convert
        match BF.is_float_binary(second_b_num): # If the first number is a float
            case True:
                second_d_num = ConF.float_b_to_float_d(second_b_num) # Convert to float
            case False:
                second_d_num = ConF.binary_to_decimal(second_b_num) # Convert to integer

        validator = True
    else:
        validator = False

    match choice:
        case 1:
            if validator:
                # Decimal calculation and converting decimal to binary
                decimal_result = round(first_d_num + second_d_num, 3)
                binary_result = ConF.float_d_to_float_b(decimal_result)
            
                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{TC.ENDC}')
            else:
                # Converting binary to integer
                first_d_num = ConF.binary_to_decimal(first_b_num)
                second_d_num = ConF.binary_to_decimal(second_b_num)

                # Decimal calculation and converting decimal to binary
                decimal_result = first_d_num + second_d_num
                binary_result = ConF.decimal_to_binary(decimal_result)

                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} + {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} + {second_b_num} = {binary_result}\n{TC.ENDC}')
        case 2:
            if validator:
                # Decimal calculation and converting decimal to binary
                decimal_result = round(first_d_num - second_d_num, 3)
                binary_result = ConF.float_d_to_float_b(decimal_result)
            
                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} - {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} - {second_b_num} = {binary_result}\n{TC.ENDC}')
            else:
                # Converting binary to integer
                first_d_num = ConF.binary_to_decimal(first_b_num)
                second_d_num = ConF.binary_to_decimal(second_b_num)

                # Decimal calculation and converting decimal to binary
                decimal_result = first_d_num - second_d_num
                binary_result = ConF.decimal_to_binary(decimal_result)

                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} - {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} - {second_b_num} = {binary_result}\n{TC.ENDC}')
        case 3:
            if validator:
                # Decimal calculation and converting decimal to binary
                decimal_result = round(first_d_num * second_d_num, 3)
                binary_result = ConF.float_d_to_float_b(decimal_result)
            
                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} * {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} * {second_b_num} = {binary_result}\n{TC.ENDC}')
            else:
                # Converting binary to integer
                first_d_num = ConF.binary_to_decimal(first_b_num)
                second_d_num = ConF.binary_to_decimal(second_b_num)

                # Decimal calculation and converting decimal to binary
                decimal_result = first_d_num * second_d_num
                binary_result = ConF.decimal_to_binary(decimal_result)

                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} * {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} * {second_b_num} = {binary_result}\n{TC.ENDC}')
        case 4:
            if validator:
                # Decimal calculation and converting decimal to binary
                decimal_result = round(first_d_num / second_d_num, 3)

                # Check if the fractional part of the result is iqual to 0 and if it return True convert the float number into intenger
                if BF.is_fractional_zero(decimal_result):
                    decimal_result = int(decimal_result)

                binary_result = ConF.float_d_to_float_b(decimal_result)
            
                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} +/{second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} / {second_b_num} = {binary_result}\n{TC.ENDC}')
            else:
                # Converting binary to integer
                first_d_num = ConF.binary_to_decimal(first_b_num)
                second_d_num = ConF.binary_to_decimal(second_b_num)

                # Decimal calculation and converting decimal to binary
                decimal_result = round(first_d_num / second_d_num, 3)

                # Check if the fractional part of the result is iqual to 0 and if it return True convert the float number into intenger
                if BF.is_fractional_zero(decimal_result):
                    decimal_result = int(decimal_result)

                binary_result = ConF.decimal_to_binary(decimal_result)

                return print(f'{TC.OKCYAN}\n| [Decimal result]: The addition of {first_d_num} / {second_d_num} = {decimal_result}{TC.ENDC}'), print(f'{TC.OKGREEN}\n| [Binary result]: The addition of {first_b_num} / {second_b_num} = {binary_result}\n{TC.ENDC}')

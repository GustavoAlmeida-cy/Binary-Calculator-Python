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

def is_fractional_zero(number): # Check if a fractional part of a number is iqual to zero
    # Convert the float number to a string
    num_str = str(number)

    # Split the string into integer and fractional parts
    integer_part, _, fractional_part = num_str.partition('.')

    # Check if the fractional part is 0
    return fractional_part == '0'

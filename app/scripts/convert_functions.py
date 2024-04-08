# Functions
def binary_to_decimal(binary_num:str): # Converts binary numbers into decimal numbers
    decimal_num = int(binary_num, 2)
    return decimal_num

def decimal_to_binary(decimal_num:int): # Converts decimal numbers into binary numbers
    if decimal_num == 0:
        return '0'
    
    binary_num = ''

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    return binary_num

def float_d_to_float_b(number, precision=8): # Converts float decimal numbers into float binary numbers
    # Convert the integer part to binary
    integer_part = int(number)
    integer_binary = bin(integer_part)[2:]

    # Convert the fractional part to binary
    fractional_part = number - integer_part
    fractional_binary = ''
    for _ in range(precision):
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit

    return integer_binary + '.' + fractional_binary

def float_b_to_float_d(binary): # Converts float binary numbers into float decimal numbers
    # Split the binary number into integer and fractional parts
    integer_part, fractional_part = binary.split('.')

    # Convert the integer part to decimal
    decimal_integer = int(integer_part, 2)

    # Convert the fractional part to decimal
    decimal_fractional = sum(int(bit) * (0.5 ** (i + 1)) for i, bit in enumerate(fractional_part))

    # Combine the integer and fractional parts to get the decimal representation
    decimal = decimal_integer + decimal_fractional

    return decimal

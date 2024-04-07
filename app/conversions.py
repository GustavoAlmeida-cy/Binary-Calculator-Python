# Converts binary numberns in decimal numbers
def binary_to_decimal(binary_num:str):
    decimal_num = int(binary_num, 2)
    return decimal_num

# Converts decimal numberns in binary numbers
def decimal_to_binary(decimal_num:int):
    if decimal_num == 0:
        return '0'
    
    binary_num = ''

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    return binary_num

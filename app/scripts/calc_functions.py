# Importing scripts

# Importing libs
from rich.console import Console
console = Console()

# Calculation functions
def binary_addition(bin1, bin2):
    # Check if both binary numbers are all zeros
    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '00000000'

    # Check if bin1 is all zeros
    if all(bit == '0' for bit in bin1):
        return bin2.zfill(8)

    # Check if bin2 is all zeros
    if all(bit == '0' for bit in bin2):
        return bin1.zfill(8)

    # Remove leading zeros
    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    # Pad the binary strings with zeros to make them of equal length
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)

    # Initialize variables
    result = ''
    carry = 0

    # Iterate through the binary strings from right to left
    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])

        # Calculate the sum of the current bits along with the carry
        current_sum = bit1 + bit2 + carry

        # Append the result to the beginning of the result string
        result = str(current_sum % 2) + result

        # Update the carry for the next iteration
        carry = current_sum // 2

    # If there's a carry left after the iteration, prepend it to the result
    if carry:
        result = '1' + result

    # Check if the result exceeds 8 bits
    if len(result) > 8:
        raise ValueError('[ Binary addition result exceeds 8 bits ]')

    # Pad the result with leading zeros to make it 8 bits long
    result = result.zfill(8)

    return result

def binary_subtraction(bin1, bin2):
    # Convert binary strings to integers for comparison
    int_bin1 = int(bin1, 2)
    int_bin2 = int(bin2, 2)
    
    # Check if the second binary number is greater than the first
    if int_bin2 > int_bin1:
        raise ValueError('[ Binary subtraction result is negative ]')

    # Check if the second binary number is zero
    if all(bit == '0' for bit in bin2):
        return bin1.zfill(8)
    
    # Pad the binary strings with zeros to make them of equal length
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)
    
    # Initialize variables
    result = ''
    borrow = 0
    
    # Iterate through the binary strings from right to left
    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        
        # Subtract the current bits along with the borrow
        current_diff = bit1 - bit2 - borrow
        
        # If the difference is negative, borrow from the next higher-order bit
        if current_diff < 0:
            current_diff += 2
            borrow = 1
        else:
            borrow = 0
        
        # Append the result to the beginning of the result string
        result = str(current_diff) + result
    
    return result.zfill(8)

def binary_multiplication(bin1, bin2):
    # Function to perform binary addition
    def binary_add(a, b):
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            bit_a = int(a[-1 - i]) if i < len(a) else 0
            bit_b = int(b[-1 - i]) if i < len(b) else 0
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])

    # Check if one of both binary numbers are all zeros
    if all(bit == '0' for bit in bin1) or all(bit == '0' for bit in bin2):
        return '00000000'

    # Remove leading zeros
    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    # If after removing leading zeros, either of the inputs is empty, return '0'
    if not bin1 or not bin2:
        return '0'

    # Multiply each bit of bin1 with entire bin2 and shift the result
    result = "0"
    for i in range(len(bin1)):
        if bin1[-1 - i] == "1":
            temp = bin2 + "0" * i
            result = binary_add(result, temp)

    # Ensure result is 8 bits long
    if len(result) > 8:
        raise ValueError('[ Binary addition result exceeds 8 bits ]')
    else:
        result = result.zfill(8)

    return result

# Multiple choice function for calculations
def binary_calculation_BA(first_b_num:str, second_b_num:str, choice):
    match choice:
        case 1:
            try:
                console.print(f'\n[bold][orange1][cyan]| [Binary result]: [green]{first_b_num}[/][/] + [green]{second_b_num}[/] = [green]{binary_addition(first_b_num, second_b_num)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| ERROR -> [orange1][underline]{e}[/][/][/]\n')
        case 2:
            try:
                console.print(f'\n[bold][orange1][cyan]|| [Binary result]: [green]{first_b_num}[/][/] - [green]{second_b_num}[/] = [green]{binary_subtraction(first_b_num, second_b_num)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| ERROR -> [orange1][underline]{e}[/][/][/]\n')
        case 3:
            try:
                console.print(f'\n[bold][orange1][cyan]|| [Binary result]: [green]{first_b_num}[/][/] * [green]{second_b_num}[/] = [green]{binary_multiplication(first_b_num, second_b_num)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| ERROR -> [orange1][underline]{e}[/][/][/]\n')

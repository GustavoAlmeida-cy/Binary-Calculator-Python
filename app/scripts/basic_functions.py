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
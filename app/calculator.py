# Importing scripts
from terminal_colors import tcolors # Enable terminal colors

# Program title
print(f"{tcolors.HEADER}-----[ Binary Calculator ]-----\n{tcolors.ENDC}")

# 10 = 1010 / 5 = 101

# Addition function
def binary_addition(x:str, y:str):
    print(f"{tcolors.WARNING}\n - Before decimal conversion\n First: {x}\n Seconfd: {y}\n{tcolors.ENDC}") # Debug comment!
    
    # Converting Binary to Decimal
    x = int(x, 2)
    y = int(y, 2)
    
    print(f"{tcolors.WARNING}\n - After decimal conversion\n First: {x}\n Second: {y}\n{tcolors.ENDC}") # Debug comment!
    
    result = x + y
    print(f"{tcolors.OKCYAN}\n The addition of {x} + {y} = {result}\n{tcolors.ENDC}")

# Reading user inputs
num1 = input(f"{tcolors.HEADER}\n Type the first number: {tcolors.ENDC}")
num2 = input(f"{tcolors.HEADER}\n Type the second number: {tcolors.ENDC}")

binary_addition(num1, num2)

# Program end
print(f"{tcolors.HEADER}\n-------[ PROGRAM END ]-------{tcolors.ENDC}")

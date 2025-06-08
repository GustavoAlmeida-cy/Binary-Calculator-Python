# ===============================
# Importando bibliotecas
# ===============================
from rich.console import Console  # Adiciona a função de console da biblioteca
console = Console()


# ===============================
# Função de conversão
# ===============================
def binary_to_decimal(binary_num: str):  # Converte números binários em decimais
    decimal_num = int(binary_num, 2)
    return decimal_num


# ===============================
# Funções de cálculo
# ===============================
def binary_addition(bin1, bin2, length):  # Adição
    length = int(float(length))
    original_length = length

    if length <= 0:
        raise ValueError("[ A quantidade de bits não pode ser menor que 1 bit! ]")

    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    if all(bit == '0' for bit in bin1):
        return bin2.zfill(length)

    if all(bit == '0' for bit in bin2):
        return bin1.zfill(length)

    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)

    result = ''
    carry = 0

    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        current_sum = bit1 + bit2 + carry
        result = str(current_sum % 2) + result
        carry = current_sum // 2

    if carry:
        result = '1' + result

    length = original_length

    if len(result) > length:
        raise ValueError(f'[ O resultado excede {original_length} bits! ]')

    return result.zfill(length)


def binary_subtraction(bin1, bin2, length):  # Subtração
    length = int(float(length))
    original_length = length

    if length <= 0:
        raise ValueError("[ The length cannot be less than 1 bit! ]")

    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    int_bin1 = int(bin1, 2)
    int_bin2 = int(bin2, 2)

    if int_bin2 > int_bin1:
        raise ValueError('[ Resultado negativo! ]')

    if all(bit == '0' for bit in bin2):
        return bin1.zfill(length)

    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)

    result = ''
    borrow = 0

    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        current_diff = bit1 - bit2 - borrow

        if current_diff < 0:
            current_diff += 2
            borrow = 1
        else:
            borrow = 0

        result = str(current_diff) + result

    length = original_length
    return result.zfill(length)


def binary_multiplication(bin1, bin2, length):  # Multiplicação
    length = int(float(length))
    original_length = length

    if length <= 0:
        raise ValueError("[ A quantidade de bits não pode ser menor que 1 bit! ]")

    def binary_add(a, b):  # Adição interna
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

    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    if not bin1 or not bin2:
        return '0' * length

    result = "0"
    for i in range(len(bin1)):
        if bin1[-1 - i] == "1":
            temp = bin2 + "0" * i
            result = binary_add(result, temp)

    length = original_length

    if len(result) > length:
        raise ValueError(f'[ O resultado excede {original_length} bits! ]')

    return result.zfill(length)


# ===============================
# Função principal de cálculo (baseada na escolha do usuário)
# ===============================
def binary_calculation_BA(first_b_num: str, second_b_num: str, choice, length):
    match choice:
        case 1:  # Adição
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: '
                              f'[purple]{binary_to_decimal(first_b_num)}[/][/] + '
                              f'[purple]{binary_to_decimal(second_b_num)}[/] = '
                              f'[purple]{binary_to_decimal(binary_addition(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: '
                              f'[green]{first_b_num}[/][/] + [green]{second_b_num}[/] = '
                              f'[green]{binary_addition(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')

        case 2:  # Subtração
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: '
                              f'[purple]{binary_to_decimal(first_b_num)}[/][/] - '
                              f'[purple]{binary_to_decimal(second_b_num)}[/] = '
                              f'[purple]{binary_to_decimal(binary_subtraction(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: '
                              f'[green]{first_b_num}[/][/] - [green]{second_b_num}[/] = '
                              f'[green]{binary_subtraction(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')

        case 3:  # Multiplicação
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: '
                              f'[purple]{binary_to_decimal(first_b_num)}[/][/] * '
                              f'[purple]{binary_to_decimal(second_b_num)}[/] = '
                              f'[purple]{binary_to_decimal(binary_multiplication(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: '
                              f'[green]{first_b_num}[/][/] * [green]{second_b_num}[/] = '
                              f'[green]{binary_multiplication(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')

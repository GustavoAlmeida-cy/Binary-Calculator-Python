# Funções de validação

def bit_length_check(length):
    """Verifica a quantidade de bits escolhida."""
    if not length or length == " ":
        return True

    if not length.replace('.', '', 1).isdigit():
        return True

    length = int(float(length))

    if length == 0 or length <= 0:
        return True
    else:
        return False


def multiple_choice_logic(choice):
    """Verifica a opção de múltipla escolha feita pelo usuário (1, 2 ou 3)."""
    if choice != '1' and choice != '2' and choice != '3':
        return True
    else:
        return False


def multiple_choice_YN(choice):
    """Verifica a opção de escolha sim/não feita pelo usuário (S ou N)."""
    if choice != 'S' and choice != 'N':
        return True
    else:
        return False


def is_binary(input_str):
    """Verifica se os números digitados pelo usuário são binários válidos (apenas 0 e 1)."""
    if input_str == "" or input_str == " ":
        return False

    for char in input_str:
        if char not in '01':
            return False

    return True

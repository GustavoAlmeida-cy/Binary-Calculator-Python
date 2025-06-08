# ========================
# IMPORTAÇÕES
# ========================

# Scripts internos
import scripts.calc_functions  as CF  # Funções de cálculo
import scripts.basic_functions as BF  # Funções básicas

# Bibliotecas externas
from rich.console import Console       # Console estilizado
from rich.traceback import install     # Traceback detalhado
from rich.markdown import Markdown     # Suporte a Markdown

# ========================
# CONFIGURAÇÃO
# ========================

console = Console()
install()

# Markdown de título e rodapé
title = '# 🔥 CALCULADORA BINÁRIA 🔥'
mdtitle = Markdown(title)

footer = '# 🔥 FIM DO PROGRAMA 🔥'
mdfooter = Markdown(footer)

# ========================
# FUNÇÃO PRINCIPAL
# ========================

def app():
    # ------------------------
    # Solicita a quantidade de bits
    # ------------------------
    console.print(
        f'\n[bold][cyan]| 🤓 Quantos bits você deseja usar para o cálculo? [italic][orange1](O valor padrão é 8 bits)[/][/][/]'
    )
    bit_length = console.input(f'\n[bold][cyan]| : [/][/]') or "8"
    bit_lenght_logic_value = BF.bit_length_check(bit_length)

    while bit_lenght_logic_value:
        console.print(f'\n[bold][red]| 😕 [underline]Quantidade de bits inválida! Por favor, digite outro valor.[/][/][/]')
        bit_length = console.input(f'\n[bold][cyan]| : [/][/]') or "8"
        bit_lenght_logic_value = BF.bit_length_check(bit_length)

    # ------------------------
    # Escolha do tipo de cálculo
    # ------------------------
    console.print(
        f'\n[bold][cyan]| 🤓 Qual o tipo de cálculo você deseja? [italic][orange1](Digite o número correspondente a opção desejada)[/][/][/]'
    )
    choice = console.input(
        f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'
    )
    mult_ch_logic_value = BF.multiple_choice_logic(choice)

    while mult_ch_logic_value:
        console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
        choice = console.input(
            f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'
        )
        mult_ch_logic_value = BF.multiple_choice_logic(choice)

    choice = int(choice)
    msg = ['Adição', 'Subtração', 'Multiplicação']
    console.print(f'\n[bold][orange1]| [ {msg[choice - 1]} ][/][/]')

    # ------------------------
    # Leitura dos números binários
    # ------------------------
    first_num  = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
    second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    while not BF.is_binary(first_num) or not BF.is_binary(second_num):
        console.print(f'\n[bold][red]| 😕 [underline]Número inválido! Por favor, digite outro número.[/][/][/]')
        first_num  = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
        second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    # ------------------------
    # Chamada da função de cálculo
    # ------------------------
    CF.binary_calculation_BA(first_num, second_num, choice, bit_length)

# ========================
# EXECUÇÃO PRINCIPAL
# ========================

if __name__ == "__main__":
    console.print(mdtitle, '\n')

    choice = "S"
    while choice == "S":
        app()

        choice = console.input(
            f"[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : "
        ).upper()

        controller = BF.multiple_choice_YN(choice)

        while controller:
            console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
            choice = console.input(
                f"\n[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : "
            ).upper()
            controller = BF.multiple_choice_YN(choice)

    console.print('\n', mdfooter)

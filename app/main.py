# Importando scripts
import scripts.calc_functions  as CF # Funções de cálculo
import scripts.basic_functions as BF # Funções basicas

# Importando bibliotecas
from rich.console import Console # Adicionando a função de console da biblioteca
console = Console()

from rich.traceback import install # Adicionando uma melhor menssagem de erro pela biblioteca
install()

from rich.markdown import Markdown # Adicionando suporte a Markdown pela biblioteca

# Construindo título e rodapé do programa usando Markdown
title = '# 🔥 CALCULADORA BINÁRIA 🔥'
mdtitle = Markdown(title)

footer = '# 🔥 FIM DO PROGRAMA 🔥'
mdfooter = Markdown(footer)

# Função principal
def app():
    # Opção de definição de quantidade de bits pelo usuário
    console.print(f'\n[bold][cyan]| 🤓 Quantos bits você deseja usar para o cálculo? [italic][orange1](O valor padrão é 8 bits)[/][/][/]')
    bit_length = console.input((f'\n[bold][cyan]| : [/][/]'))

    bit_length = bit_length if bit_length else "8"
    bit_lenght_logic_value = BF.bit_length_check(bit_length)

    if bit_lenght_logic_value: # Valida se a quantidade de bits escolhida
        while bit_lenght_logic_value:
            console.print(f'\n[bold][red]| 😕 [underline]Quantidade de bits inválida! Por favor, digite outro valor.[/][/][/]')
            bit_length = console.input((f'\n[bold][cyan]| : [/][/]'))

            bit_length = bit_length if bit_length else "8"
            bit_lenght_logic_value = BF.bit_length_check(bit_length)

    # Opção de multipla escolha entre os tipos de cálculos
    console.print(f'\n[bold][cyan]| 🤓 Qual o tipo de cálculo você deseja? [italic][orange1](Digite o número correspondente a opção desejada)[/][/][/]')
    choice = console.input((f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'))

    mult_ch_logic_value = BF.multiple_choice_logic(choice)

    if mult_ch_logic_value: # Valida a opção de escolha do usuário
        while mult_ch_logic_value:
            console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
            choice = console.input((f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'))
            mult_ch_logic_value = BF.multiple_choice_logic(choice)

    choice = int(choice)
    msg = ['Adição', 'Subtração', 'Multiplicação'] # Mensagem da opção escolhida

    console.print(f'\n[bold][orange1]| [ {msg[choice - 1]} ][/][/]') # Escolha da mensagem com base na escolha do usuário

    # Lendo os números obtidos pelo usuário
    first_num = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
    second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    # Verifica se os números são válidos
    if not BF.is_binary(first_num) or not BF.is_binary(second_num):
        while not BF.is_binary(first_num) or not BF.is_binary(second_num):
            console.print(f'\n[bold][red]| 😕 [underline]Número inválido! Por favor, digite outro número.[/][/][/]')
            first_num = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
            second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    # Lógica de escolha do tipo de cálculo
    match choice:
        case 1:
            CF.binary_calculation_BA(first_num, second_num, 1, bit_length)
        case 2:
            CF.binary_calculation_BA(first_num, second_num, 2, bit_length)
        case 3:
            CF.binary_calculation_BA(first_num, second_num, 3, bit_length)

# Início do programa
if __name__ == "__main__":
    # Título do programa
    console.print(mdtitle, '\n')

    choice = "S" # Declarando variável de escolha
    
    while choice == "S": # Laço de repetição do programa
        app()

        choice = console.input(f"[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : ").upper()
        controller = BF.multiple_choice_YN(choice)

        if controller: # Valida se a opção escolhida pelo usuário
            while controller:
                console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
                choice = console.input(f"\n[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : ").upper()
                controller = BF.multiple_choice_YN(choice)
                
    # Program footer
    console.print('\n', mdfooter)

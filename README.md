# 🧮 Calculadora Binária em Python

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&style=flat-square)
![Licença](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Rich](https://img.shields.io/badge/UI-Rich-orange?style=flat-square)

---

## 📌 Sobre o Projeto

Esta é uma **calculadora binária interativa** desenvolvida em **Python**, com uma interface de terminal aprimorada pela biblioteca [`Rich`](https://github.com/Textualize/rich). Ela permite realizar operações básicas com números binários de forma clara, educativa e amigável ao usuário.

### ✅ Funcionalidades

- 🔢 Definição da **quantidade de bits** (padrão: 8)
- ➕ Operações suportadas:
  - Adição
  - Subtração
  - Multiplicação
- 🖥️ Interface de linha de comando com cores e formatação (via `rich`)
- 🔁 Execução contínua (permite realizar múltiplos cálculos)
- 📌 Validações de entrada com mensagens amigáveis

---

## 🚀 Instalação

Antes de executar o programa, certifique-se de que o Python (versão 3.6 ou superior) esteja instalado. Em seguida, instale a dependência:

```bash
pip install rich
```

---

## ▶️ Como Usar

1. Clone ou baixe este repositório.
2. Execute o script principal:

```bash
python main.py
```

3. Siga as instruções no terminal para escolher:
   - A quantidade de bits
   - O tipo de operação (adição, subtração ou multiplicação)
   - Os números binários para cálculo

---

## 📁 Estrutura do Projeto

```text
📦 calculadora-binaria/
├── scripts/
│   ├── basic_functions.py     # Validações e utilitários
│   └── calc_functions.py      # Lógica dos cálculos binários
├── main.py                    # Arquivo principal do programa
└── README.md                  # Este arquivo
```

---

## 🖼️ Demonstração

Abaixo está uma captura de tela do funcionamento da calculadora binária no terminal:

![Demonstração da Calculadora Binária](/app/images/screenshot-1.png)

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais informações.

---

## 💡 Créditos

Projeto desenvolvido para fins educacionais, com foco em lógica binária, operações aritméticas e uso de interfaces interativas no terminal com Python.

---

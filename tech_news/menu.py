import sys


# Requisitos 11 e 12
def analyzer_menu():
    try:
        option = input(
            """Selecione uma das opções a seguir:\n"""
            """0 - Popular o banco com notícias;\n"""
            """1 - Buscar notícias por título;\n"""
            """2 - Buscar notícias por data;\n"""
            """3 - Buscar notícias por categoria;\n"""
            """4 - Listar top 5 categorias;\n"""
            """5 - Sair."""
        )
        print(option)
    except (IndexError, ValueError, TypeError):
        print("Opção inválida", sys.stderr)

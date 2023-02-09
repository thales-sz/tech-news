import sys


# Requisitos 11 e 12
def analyzer_menu():
    try:
        option = input(
            """Selecione uma das opções a seguir:
            0 - Popular o banco com notícias;
            1 - Buscar notícias por título;
            2 - Buscar notícias por data;
            3 - Buscar notícias por categoria;
            4  - Listar top 5 categorias;
            5 - Sair."""
        )
        print(option)
    except (IndexError, ValueError, TypeError):
        print("Opção inválida", sys.stderr)

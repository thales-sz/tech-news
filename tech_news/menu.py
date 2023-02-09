import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_category, search_by_date


# Requisitos 11 e 12
def analyzer_menu():
    def option00():
        value = input("Digite a quantidade de noticias: ")
        return get_tech_news(int(value))

    def option01():
        value = input("Digite a quantidade de noticias: ")
        return get_tech_news(int(value))

    switch = {
        "0": option00,
        "1": option01,
        "2": "Opção 2",
        "3": "Opção 3",
        "4": "Opção 4",
        "5": "Opção 5",
    }
    try:
        option = input(
            """Selecione uma das opções a seguir:\n"""
            """ 0 - Popular o banco com notícias;\n"""
            """ 1 - Buscar notícias por título;\n"""
            """ 2 - Buscar notícias por data;\n"""
            """ 3 - Buscar notícias por categoria;\n"""
            """ 4 - Listar top 5 categorias;\n"""
            """ 5 - Sair.\n"""
        )
        print(option)
        switch.get(option)
    except (IndexError, ValueError, TypeError):
        print("Opção inválida", sys.stderr)

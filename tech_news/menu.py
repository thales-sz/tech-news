import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.analyzer.ratings import top_5_categories


def option00():
    value = input("Digite a quantidade de noticias: ")
    return get_tech_news(int(value))


def option01():
    value = input("Digite a categoria: ")
    return search_by_title(value)


def option02():
    value = input("Digite a data: ")
    return search_by_date(value)


def option03():
    value = input("Digite a categoria: ")
    return search_by_category(value)


def option05():
    print("Encerrando script")
    return


# Requisitos 11 e 12
def analyzer_menu():
    switch = {
        "0": option00,
        "1": option01,
        "2": option02,
        "3": option03,
        "4": top_5_categories,
        "5": option05,
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
        if option == "":
            raise ValueError()
        print(switch.get(option)())
    except (IndexError, ValueError, TypeError, AssertionError):
        print("Opção inválida", sys.stderr)

from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = []
    data = search_news({"title": {"$regex": title, "$options": "-i"}})
    for new in data:
        news.append((new["title"], new["url"]))
    return news


# Requisito 8
def search_by_date(date):
    news = []
    try:
        formated = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        data = search_news({"timestamp": formated})
        for new in data:
            news.append((new["title"], new["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

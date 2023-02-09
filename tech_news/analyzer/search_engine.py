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
    formated_date = datetime.strptime(date, '%d/%m/%Y')
    data = search_news(
        {"timestamp": {"$regex": formated_date, "$options": "-i"}}
    )
    print(data)
    for new in data:
        news.append((new["title"], new["url"]))
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()
    teste = Counter([new["category"] for new in news])
    print(teste)

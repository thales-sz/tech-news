from parsel import Selector
import requests
import time

headers = {"user-agent": "Fake user-agent"}
base_url = "https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url=url, headers=headers, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = (
        selector.css("div.pk-share-buttons-wrap")
        .xpath("@data-share-url")
        .get()
    )
    writer = selector.css("a.url.fn.n::text").get()
    title = (
        selector.css("h1.entry-title::text").get().replace("\xa0", " ").strip()
    )
    category = selector.css("span.label::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    summary = (
        "".join(selector.xpath("//div[1]/p[1]//text()").getall())
        .replace("\xa0", " ")
        .strip()
    )

    return {
        "url": url,
        "writer": writer,
        "title": title,
        "category": category,
        "reading_time": reading_time,
        "timestamp": timestamp,
        "summary": summary,
    }


# Requisito 5
def get_tech_news(amount):
    pass

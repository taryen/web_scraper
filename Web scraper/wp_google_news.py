import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        xml = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(xml, parser)

        with open('noticias.txt', 'w', encoding='utf-8') as file:
            for item in sp.find_all("item"):
                title = item.find("title")
                if title is None:
                    continue

                else:
                    print("\n" + title.text)
                    file.write(title.text + '\n')


news = "https://news.google.com/news/rss/headlines"
Scraper(news).scrape()

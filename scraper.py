
"""
Sites to scrape from:
https://www.knmi.nl/nederland-nu/weer/verwachtingen
https://racingnews365.nl/
https://nos.nl/
"""

from selenium import webdriver 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

class Scraper():
    def __init__(self, url):
        self.url = url
        self.client = req(self.url)
        self.html = self.client.read()
        self.soup = soup(self.html, "html.parser")

    def get_links(self):
        self.links=[]
        for link in self.top_news_container.find_all("a", href=True):
            self.links.append(link["href"])

    def find_with_css_selector(self, css_selector):
        found_elem = self.soup.select(css_selector)[0].get_text(strip=True)
        return found_elem

class Weather(Scraper):
    def __init__(self, url):
        Scraper.__init__(self, url)
        self.scrape()

    def scrape(self):
        self.weather = self.find_with_css_selector("div.weather__text.media__body > p:nth-child(3)")

class Racing(Scraper):
    def __init__(self, url):
        Scraper.__init__(self, url)
        self.scrape()

    def scrape(self):
        self.soup = soup(self.html, "html.parser")
        self.top_news_container = self.soup.find("div", {"class":"top-news"})

        self.get_links()

        self.article_1 = self.soup.select("div:nth-child(1) > a > div.card__content-wrapper > span.card__title")[0].get_text(strip=True)
        self.link_1 = self.links[0]

        self.article_2 = self.soup.select("div:nth-child(3) > a > div.card__content-wrapper > span.card__title")[0].get_text(strip=True)
        self.link_2 = self.links[1]

        self.article_3 = self.soup.select("div:nth-child(4) > a > div.card__content-wrapper > span.card__title")[0].get_text(strip=True)
        self.link_3 = self.links[2]

class Gaming(Scraper):
    def __init__(self, url):
        Scraper.__init__(self, url)
        self.top_news_container = self.soup.find("div", {"class":"mainCarousel"})
        self.scrape()

    def scrape(self):
        self.get_links()

        self.article_1 = self.find_with_css_selector("#Item1 > a.article-link > figure > figcaption > span.article-name")
        self.link_1 = self.links[0]

        self.article_2 = self.find_with_css_selector("#Item2 > a.article-link > figure > figcaption > span.article-name")
        self.link_2 = self.links[2]

        self.article_3 = self.find_with_css_selector("#Item3 > a.article-link > figure > figcaption > span.article-name")
        self.link_3 = self.links[4]

class News(Scraper):
    def __init__(self, url):
        Scraper.__init__(self, url)
        self.scrape()

    def scrape(self):
        self.top_news_container = self.soup.find("ol", {"class":"topStoryList_3h-yfm5a"})

        self.get_links()

        self.article_1 = self.find_with_css_selector("#topstories > div > section > ol > li:nth-child(1) > a > div.inner_bjtffV3s > div > h2")
        self.link_1 = self.url + self.links[0]
       
        self.article_2 = self.find_with_css_selector("#topstories > div > section > ol > li:nth-child(2) > a > div.inner_bjtffV3s > div > h2")
        self.link_2 = self.url + self.links[1]
    
def main():
    weather = Weather("https://www.knmi.nl/nederland-nu/weer/verwachtingen")
    racing = Racing("https://racingnews365.nl/")
    gaming = Gaming("https://www.pcgamer.com/news/")
    news = News("https://nos.nl")

if __name__ == '__main__':
    main()

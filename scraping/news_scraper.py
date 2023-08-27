from parsel import Selector
import requests


#'//div[@class="b-content__inline_item"]/div[@class="b-content__inline_item-link"]/a/@href'
#"https://rezka.ag/new/"


class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    START_URL = "https://www.prnewswire.com/news-releases/news-releases-list/"
    LINK_XPATH = '//div[@class="row newsCards"]/div/a/@href'
    TEXT_XPATH = '//div[@class="col-lg-10 col-lg-offset-1"]//text()'

    def parse_data(self):
        text = requests.get(self.START_URL).text
        tree = Selector(text=text)
        links = tree.xpath(self.LINK_XPATH).extract()
        data = []
        for link in links:
            print(self.PLUS_URL + link)
            data.append(self.PLUS_URL + link)
        return data[:5]


    def parse_detail(self, urls):
        for url in urls:
            text = requests.get(self.PLUS_URL + url).text
            tree = Selector(text=text)
            text = tree.xpath(self.TEXT_XPATH).extract()
            print(''.join(text))


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()
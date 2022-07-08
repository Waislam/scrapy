import scrapy
from ..items import ZillowItem

class ZillowCrawler(scrapy.Spider):
    name = 'zillowspider'
    start_urls = ['https://www.zillow.com/homes/6405-Phinney-Drive,-Frisco,-TX-75035_rb/63673696_zpid/']

    def parse(self, response):
        items = ZillowItem()

        heartext = response.xpath("//div[@class='page-header']/div/div/h1/text()").get()

        items['Header_text'] = heartext
        yield items
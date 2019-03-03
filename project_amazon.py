import scrapy
from ..items import ProjItem

class ProjAmazonSpider(scrapy.Spider):
    name = 'proj_amazon'

    start_urls = ['https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook']

    def parse(self, response):
        items = ProjItem()
        p_name = response.css('.s-access-title::text').extract()

        p_price = response.css('.s-price').css('::text').get()
        p_img = response.css('.cfMarker::attr(src)').get()
        items['p_name'] = p_name

        items['p_price'] = p_price
        items['p_img'] = p_img
        yield items

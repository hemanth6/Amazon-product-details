import scrapy


class ProjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_name = scrapy.Field()

    p_price = scrapy.Field()
    p_img = scrapy.Field()
    pass

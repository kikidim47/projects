import scrapy

class ZhihuItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    answer_author = scrapy.Field()
    answer_content = scrapy.Field()
    vote_count = scrapy.Field()
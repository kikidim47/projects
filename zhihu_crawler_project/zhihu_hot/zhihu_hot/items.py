# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuHotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 热榜标题
    url = scrapy.Field()  # 热榜链接
    excerpt = scrapy.Field()  # 热榜摘要
    hot_index = scrapy.Field()  # 热度指数
    timestamp = scrapy.Field()  # 热榜时间戳
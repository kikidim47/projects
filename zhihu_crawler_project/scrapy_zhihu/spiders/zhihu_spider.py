import scrapy
from scrapy_zhihu.items import ZhihuItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/billboard']

    def parse(self, response):
        for question in response.css('.HotList-item'):
            title = question.css('.HotList-itemTitle::text').get()
            link = question.css('a::attr(href)').get()
            if title and link:
                yield scrapy.Request(url=link, callback=self.parse_question, meta={'title': title})

    def parse_question(self, response):
        title = response.meta['title']
        answers = response.css('.List-item')
        for answer in answers[:3]:  # 取前三个回答
            item = ZhihuItem()
            item['title'] = title
            item['url'] = response.url
            item['answer_author'] = answer.css('.AuthorInfo-name::text').get()
            item['answer_content'] = ''.join(answer.css('.RichText ztext::text').getall())
            item['vote_count'] = answer.css('.Button.VoteButton::text').get()
            yield item
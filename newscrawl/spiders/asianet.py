import scrapy
from ..items import NewscrawlItem

class news_crawl(scrapy.Spider):
    name = "asianet"
    start_urls = ["https://www.asianetnews.com/search?topic=drugs"]
    def parse(self,response):
        urls = response.css('div.sr-text a::attr(href)').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_news_list)

    def parse_news_list(self,response):
        item = NewscrawlItem()
        content = response.css('div.postContent p::text').extract()
        time = response.css('div.date::text').extract()
        item['time'] = time
        item['content'] = content
        yield item

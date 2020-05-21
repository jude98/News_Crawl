import scrapy
from ..items import NewscrawlItem
import pickle

class news_crawl(scrapy.Spider):
	name = "oneindia"
	start_urls = ["https://malayalam.oneindia.com/search/results.html?q=drugs&tab=oneindia&page=0"]
	def parse(self,response):
		urls = response.css('div.text-head a::attr(href)').extract()
		for url in urls:
			yield response.follow(url, callback=self.parse_news_list)

	#next = response.css('.next::attr(data-pageno)').extract()

	#if next <= 2:


	def parse_news_list(self,response):
		item = NewscrawlItem()
		content = response.css('p::text').extract()
		time = response.css('time::text').extract()
		item['time'] = time
		item['content'] = content

		yield item

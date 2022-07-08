import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass

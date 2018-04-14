# http://books.toscrape.com


import scrapy

class BooksSpider(scrapy.Spider): #inherit from scrapy.spider

    # define scrapy name
    name = 'bookspider'

    # define url
    start_urls = ['http://books.toscrape.com']

    # define parse method
    def parse(self, response):

        for article in response.css('article.product_pod'):


            # used in spider as return
            yield {
                'price' : article.css(".price_color::text").extract(),
                'title' : article.css("h3 > a::attr(title)").extract()
            }

        next = response.css(".next a::attr(href)").extract()[0]
        if next:
            yield response.follow(next, self.parse)

import scrapy
from inflearn_tutorial.items import Dmoz_books

# 클래스 이름 임의로 지정
# 단, scrapy.Spider 상속
class DmozSpider(scrapy.Spider):

    # spider를 지정하는 유니크한 이름
    name = "dmoz"

    # 허용된 도메인
    allowed_domains = ["dmoztools.net"]

    # 스크랩을 할 url 지정
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    # 실질적으로 spider가 url로 가서 동작하는 부분
    def parse(self, response):

        # 첫번째 아이템 xpath: //*[@id="site-list-content"]/div[1]/div[3]/a
        # 두번째 아이템 xpath: //*[@id="site-list-content"]/div[2]/div[3]/a
        # 그렇다면 //*[@id="site-list-content"]/div 이하로 모두 가져오면 되겠다

        for sel in response.xpath('//*[@id="site-list-content"]/div'):
            item = Dmoz_books()

            # title xpath : //*[@id="site-list-content"]/div[1]/div[3]/a/div
            item['title'] = sel.xpath('div[3]/a/div/text()').extract()

            # link xpath : //*[@id="site-list-content"]/div[1]/div[3]/a
            item['link'] = sel.xpath('div[3]/a/@href').extract()

            # description xpath : //*[@id="site-list-content"]/div[1]/div[3]/div/text()
            item['desc'] = sel.xpath('div[3]/div/text()').extract()

            yield item

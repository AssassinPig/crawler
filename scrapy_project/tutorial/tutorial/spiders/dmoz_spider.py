import scrapy
from tutorial.items import DmozItem
from scrapy.selector import Selector

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
	
    def parse(self, response):
        items = [] 
        sel = Selector(response)
        books = sel.xpath('//ul[@class="directory-url"]/li')
        for book in books:
            item = DmozItem()
            item['title'] = book.xpath('a/text()').extract()
            item['link'] = book.xpath('a/@href').extract()
            item['desc'] = book.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        #books = sel.xpath('//ul/li')
        #for book in books:
        #    item = DmozItem()
        #    item['title'] = book.xpath('a/text()').extract()
        #    item['link'] = book.xpath('a/@href').extract()
        #    item['desc'] = book.xpath('text()').re('-\s[^\n]*\\r')
        #    print item
        #    items.append(item)
        return items

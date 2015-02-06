# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from jd.items import JdItem
import re

class JdSpider(CrawlSpider):
    name = "jd_spider"
    allowed_domains = ["jd.com"]
    #start_urls = ['http://www.jd.com/']
    start_urls = ['http://item.jd.com/11417193.html']
    visited_list = []
    rules = [
        #Rule(SgmlLinkExtractor(allow=('/group/[^/]+/$', )), callback='parse_group_home_page', process_request='add_cookie'),
        #Rule(SgmlLinkExtractor(allow=('/group/explore\?tag', )), follow=True, process_request='add_cookie'),
    ]
    item_name = ''
    item_url = ''
    item_price = ''
    item_id =''

    def parse(self, response):
        href_list = response.xpath('//a[contains(@href, ".html")]/@href').extract()
        for h in href_list:
            if h in self.visited_list:
                pass
            else:
                self.visited_list.append(h)
                #print 'add visited_urls: %s' % h
                
                validate_url = re.match('http://\w+.jd.com/\d+.html', h)
                if validate_url is None:
                    print 'this page will be fetched %s' % h
                    yield scrapy.http.Request(h, callback=self.parse)
                else:
                    self.item_id = h.split('/')[-1].split('.')[0]
                    item_name = response.xpath('//div[@id=\"name\"]/h1/text()').extract()
                    price_url = 'http://p.3.cn/prices/get?skuid=J_%s' % self.item_id 
                    print 'price_url %s' % price_url
                    yield scrapy.http.Request(price_url, callback=self.parse_price)
            #yield scrapy.http.Request(h, callback=self.parse)

    def parse_price(self, response):
        print 'parse_price===================='
        print response.body
        print self.item_id 
        #item = JdItem()
        #item['name'] = item_name 
        #item['price'] = '0.0' 
        #return item

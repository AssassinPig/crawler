# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider


class MultiplePagesSpider(CrawlSpider):
    name = "multiple_pages"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = (
            'http://tieba.baidu.com/f?kw=%D6%D0%B3%AC&fr=index',
    )
    visited_list = []

    def parse(self, response):
        l = response.xpath('//a/@href').re('/p/\d+')
        for e in l:
            url = 'http://tieba.baidu.com%s' % e
            if url in self.visited_list:
                pass
            else:
                self.visited_list.append(url)
                yield scrapy.http.Request(url, callback=self.parse_page1)

        #fecth next page
        next_pages = response.xpath('//a/@href').re('^.*pn=\d+$')
        for p in next_pages:
            url = "http://tieba.baidu.com%s" % p 
            if url in self.visited_list:
                pass
            else:
                print 'next page==========%s' % url
                self.visited_list.append(url)
                yield scrapy.http.Request(url, callback=self.parse)

    def parse_page1(self,response):
        print 'parse_page1=========='
        l = response.xpath('//a[@data-field]/@href').extract()
        for e in l:
            n = "%s%s" % (self.start_urls[0], e)
            return scrapy.http.Request(n, callback=self.parse_page2)

    def parse_page2(self, response):
        print 'parse_page2=========='

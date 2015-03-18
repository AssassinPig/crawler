# -*- coding: utf-8 -*-
from crawler import Crawler
from crawleritem import CrawlerItem
from StringIO import StringIO
import lxml.html as LH
from strategy import Strategy

class WoaiduCrawlerItem(CrawlerItem):
    def __init__(self, url):
        super(WoaiduCrawlerItem, self).__init__(url)

    def parse(self):
        strHtml = StringIO(self.html_body)
        tree = LH.parse(strHtml)
        l1 = tree.xpath('//div[@class=\'wudongqiank\']/a[@href]/text()')
        l2 = tree.xpath('//div[@class=\'wudongqiank\']/a[@href]/@href')
        url_list = []
        for i, elem  in enumerate(l1):
            print elem.encode('utf8')
            print l2[i].encode('utf8')
            if l2[i].find('http:') == 0:
                url_list.append(l2[i])
            else:
                url = 'http://%s%s' % (self.refer, l2[i])
                print 'new url: %s' % url
                url_list.append(url)

        print 'parse list'
        print url_list
        return url_list

if __name__ == '__main__':
    start_url = ['http://www.woaidu.org/']
    strategy = Strategy(Strategy.BSF)
    crawler = Crawler(start_url, WoaiduCrawlerItem, strategy)
    crawler.run()

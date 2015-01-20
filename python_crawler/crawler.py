# -*- coding: utf-8 -*-
import urllib2
from lxml import etree
from StringIO import StringIO
import lxml.html as LH

class Crawler:
    visited_list = []
    todo_list = []
    start_url = ['http://www.woaidu.org/']

    def run(self):
        #add to list
        for e in self.start_url:
            self.todo_list.append(e)
        
        while(True):
            if len(self.todo_list):
                item = CrawlerItem(self.todo_list.pop())
                item.fetch()
                self.url_list = item.parse()
                
                self.visited_list.append(item.url)

                #todo_list.remove()

                #url_list process
                #1.add 'http' prefix
                #2.reject duplicate item
                for e in self.visited_list:
                    if e in self.url_list:
                        self.url_list.remove(e)

                self.todo_list.extend(self.url_list)
            else:
                break
        pass

class CrawlerItem:
    url = None
    html_body = None
    refer = None

    def __init__(self, url):
        self.url = url
        self.refer = url.split('/')[2] 

    def fetch(self):
        #print 'fetch===='
        req = urllib2.Request(url=self.url)
        f = urllib2.urlopen(req)
        self.html_body = f.read()
        #print 'html_body %s' % self.html_body

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
                url = 'http://%s/%s' % (self.refer, l2[i])
                print 'new url: %s' % url
                url_list.append(url)

        return url_list

    def getHtmlBody(self):
        pass

    def getHeader(self):
        pass

crawler = Crawler()
crawler.run()

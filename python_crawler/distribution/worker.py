# -*- coding: utf-8 -*-
import settings
import redis
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

class Worker(Crawler):

    def __init__(self, start_urls=None, template_cls=None, strategy=None, settings=None):
        super(Worker, self).__init__(start_urls=start_urls, template_cls=WoaiduCrawlerItem, strategy=strategy)

        if settings is None:
            try:
                self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
                if self.r is None:
                    raise redis.exceptions.ConnectionError 
            except (redis.exceptions.ConnectionError), e:
                raise e 
        else:
            self.host = settings.REDIS_HOST
            self.port = settings.PORT

            self.QUEUE_TODO = settings.QUEUE_TODO
            self.QUEUE_VISITED = settings.QUEUE_VISITED
            self.QUEUE_FETCHED = settings.QUEUE_FETCHED

            self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)
    
    def run(self):
        while True:
            print 'run loop...'
            url = self.r.brpop(self.QUEUE_TODO)
            #suppose url is validate
            self.strategy.append(url[1])

            if self.strategy.todo_count() != 0:
                item = self.template_cls(self.strategy.pop())
                item.fetch()
                url_list = item.parse()
                
                #self.visited_list.append(item.url)
                self.strategy.append(item.url)
                
                for l in url_list:
                    self.r.lpush(self.QUEUE_FETCHED, l)
                    print 'push %s' % l
                #print 'push %s' % item.url

                #url_list process
                #self.strategy.extend_list(url_list)
             


if __name__ == '__main__':
    #start_urls = ['http://www.woaidu.org/']
    start_urls = []
    strategy = Strategy(Strategy.BSF)
    worker = Worker(start_urls=start_urls, strategy=strategy, settings=settings)
    worker.run()

# -*- coding: utf-8 -*-
from crawleritem import CrawlerItem
import strategy

class Crawler:
    visited_list = []
    todo_list = []

    start_url = []
    template_cls = None
    strategy = None

    def __init__(self, start_url, template_cls, strategy):
        self.start_url.extend(start_url)
        self.template_cls = template_cls
        self.strategy = strategy 

    def run(self):
        #add to list
        for e in self.start_url:
            #self.todo_list.append(e)
            print e
            self.strategy.append(e)
        
        while(True):
            print 'run loop...'
            if self.strategy.todo_count() != 0:
                item = self.template_cls(self.strategy.pop())
                item.fetch()
                url_list = item.parse()
                
                #self.visited_list.append(item.url)
                self.strategy.append(item.url)

                #url_list process
                self.strategy.extend(url_list)
            else:
                break




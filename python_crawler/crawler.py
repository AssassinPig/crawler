# -*- coding: utf-8 -*-
from crawleritem import CrawlerItem

class Crawler:
    visited_list = []
    todo_list = []
    start_url = ['http://www.woaidu.org/']
    template_item = None

    def set_template(self, template_item):
        self.template_item = template_item

    def run(self):
        #add to list
        for e in self.start_url:
            self.todo_list.append(e)
        
        while(True):
            print 'run loop...'
            if len(self.todo_list) != 0:
                item = self.template_item(self.todo_list.pop())
                item.fetch()
                url_list = item.parse()
                
                self.visited_list.append(item.url)

                #url_list process
                #1.add 'http' prefix
                #2.reject duplicate item
                for e in self.visited_list:
                    if e in url_list:
                        url_list.remove(e)

                self.todo_list.extend(url_list)
            else:
                break




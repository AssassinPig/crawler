# -*- coding: utf-8 -*-
'''
    author: assassinpig
    email: assassinpig@gmail.com
'''
import requests
class CrawlerItem(object):
    url = None
    html_body = None
    refer = None

    def __init__(self, url):
        self.url = url
        self.refer = url.split('/')[2] 

    def fetch(self):
        print 'fetch %s' % self.url
        res = requests.get(self.url)
        self.html_body = res.content 

    def parse(self):
        pass

    def getHtmlBody(self):
        pass

    def getHeader(self):
        pass

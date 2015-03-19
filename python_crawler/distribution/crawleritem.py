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
    headers = None

    def __init__(self, url):
        self.url = url
        self.refer = url.split('/')[2] 

    def fetch(self):
        res = requests.get(self.url)
        self.html_body = res.content 
        self.headers = ''
        for key in res.headers:
            self.headers += ( '%s: %s\n' % (key, res.headers[key]))

    def parse(self):
        pass

    def getHtmlBody(self):
        return self.html_body

    def getHeader(self):
        return self.headers


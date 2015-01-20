# -*- coding: utf-8 -*-
import urllib2
class CrawlerItem(object):
    url = None
    html_body = None
    refer = None

    def __init__(self, url):
        self.url = url
        self.refer = url.split('/')[2] 

    def fetch(self):
        print 'fetch %s' % self.url
        req = urllib2.Request(self.url)
        f = urllib2.urlopen(req)
        self.html_body = f.read()
        #print 'html_body %s' % self.html_body

    def parse(self):
        pass

    def getHtmlBody(self):
        pass

    def getHeader(self):
        pass

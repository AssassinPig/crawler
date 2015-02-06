# -*- coding: utf-8 -*-
import scrapy
from scrapy import log

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["django-china.cn"]
    start_urls = (
        'http://www.django-china.cn/accounts/signin',
    )

    status = 0  #0-haven't logined 1-have logined

    def parse(self, response):
        #get csrfmiddlewaretoken
        if response.headers.get('Set-Cookie'):
            csrfmiddlewaretoken = response.headers['Set-Cookie']
            csrfmiddlewaretoken = csrfmiddlewaretoken.split(';')[0].split('=')[1] 
            print "csrfmiddlewaretoken %s" % csrfmiddlewaretoken

        #send start url 
        if self.status == 0:
            #haven't logined
            request = scrapy.FormRequest.from_response(response, method='POST', formdata={'csrfmiddlewaretoken':csrfmiddlewaretoken, 'identification': 'assassinpig@gmail.com', 'password': 'shao2014'}, callback=self.after_login)
            return request
        elif self.status == 1:
            #have logined
            for k,v in response.headers.items():
                print("%s, %s" % (k, v))
            print "body %s" % response.body

    def after_login(self, response):
        for k,v in response.headers.items():
            print("%s, %s" % (k, v))
        #update status
        self.status = 1
        yield self.parse(response)

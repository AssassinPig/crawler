#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
#=============================================================================
#     FileName: conf.py
#         Desc: 配置文件
#       Author: lizherui
#        Email: lzrak47m4a1@gmail.com
#     HomePage: https://github.com/lizherui/spider_python
#      Version: 0.0.1
#   LastChange: 2013-08-22 11:37:25
#=============================================================================
'''
# Web页面的ip
HOST_NAME = '127.0.0.1'

# Web页面的port
PORT_NUMBER = 8888

# Redis的ip
REDIS_IP = '127.0.0.1'

# Redis的port
REDIS_PORT = 6379

# Redis清空的频率
REDIS_FLUSH_FREQUENCE = 10

# 爬虫爬取的频率，默认为每小时爬取一次
CRAWLER_FREQUENCE_HOURS = 1

# 短信通知的频率，默认为每10分钟检查一次，并抓取到符合要求的消息才会发短信
MESSAGE_FREQUENCE_MINUTES = 10

# Web页面筛选的关键词
# 包含PRI_KEYS的链接一定会被抓取
WEB_FILETER_PRI_KEYS = (u'校招', u'应届', u'毕业生',)
# 包含KEYS且不包含EXCLUDE_KEYS的链接会被抓取
WEB_FILETER_KEYS = (u'百度', u'阿里', u'腾讯',u'网易',)
WEB_FILETER_EXCLUDE_KEYS = (u'社招',)

# 短信通知筛选的关键词
# 包含PRI_KEYS的链接一定会被抓取
MESSAGE_FILETER_PRI_KEYS= ()
# 包含KEYS且不包含EXCLUDE_KEYS的链接会会被抓取
MESSAGE_FILETER_KEYS = (u'Google', u'网易游戏', u'阿里',)
MESSAGE_FILETER_EXCLUDE_KEYS = (u'社招',)

# 发件箱的域名
SEND_MAIL_POSTFIX = "163.com"

# 发件箱的smtp
SEND_MAIL_HOST = "smtp.163.com"

# 发件箱的用户名
SEND_MAIL_USER = "用户名"

# 发件箱的密码
SEND_MAIL_PASSWORD = "密码"

# 发件箱的用户昵称
SEND_MAIL_USER_NAME = "昵称"

# 139收件箱的用户名，即手机号
RECEIVE_MAIL_USER_139 = "手机号"

# 139收件箱的域名
RECEIVE_MAIL_POSTFIX_139 = "139.com"

# 收件箱
RECEIVE_MAIL_LIST = ["xiyoulaoyuanjia@gmail.com","test@qq.com",]

# 爬取的目标网站
HTTP_QUERYS = (
                {
                    'host' : 'http://bbs.byr.cn',
                    'url'  : 'http://bbs.byr.cn/board/JobInfo',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/article/JobInfo/\d+$",
                    'source' : u'北邮人论坛-招聘信息',
                },

                {
                    'host' : 'http://www.newsmth.net',
                    'url'  : 'http://www.newsmth.net/nForum/board/Career_Campus',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/nForum/article/Career_Campus/\d+$",
                    'source' : u'水木社区',
                },

                {
                    'host' : 'http://bbs.byr.cn',
                    'url'  : 'http://bbs.byr.cn/board/Job',
                    'headers' : {
                        "X-Requested-With" : "XMLHttpRequest",
                    },
                    'href' : "^/article/Job/\d+$",
                    'source' : u'北邮人论坛-找工作',
                },
            )


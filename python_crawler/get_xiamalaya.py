#http://www.ximalaya.com/tracks/5212015.json

import httplib, urllib
headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"BAIDU_DUP_lcr=http://www.ximalaya.com/1000202/sound/5212015",
        "Host":"fdfs.xmcdn.com",
        "If-Range":"Mon, 26 Jan 2015 11:37:35 GMT",
        "Range":"bytes=48076-48076",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36"
        }

conn = httplib.HTTPConnection("fdfs.xmcdn.com")
conn.request("GET", "/group5/M08/71/3E/wKgDtVTGJv-huRrRAMEz4Hbao4Y163.mp3")
response = conn.getresponse()
print response.status
data = response.read()
f=open('tmp.mp3', 'ab+')
f.write(data)
f.close()

#!/usr/bin/env python2 
# coding:utf-8

import urllib2,os
import lxml.html

url = "http://www.xiami.com/chart/data?c=101&type=0&page=1&limit=10&_=1456582894957"
userAgent = " User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 "
headers = { 'User-Agent' : userAgent }
requst = urllib2.Request(url,headers = headers) 
result = urllib2.urlopen(requst).read()

# 开始获取返回数据的所有歌曲ID
html_obj = lxml.html.fromstring(result)

song_href = html_obj.xpath('tr//strong/a/@href')
for l in song_href:
    song_id = l.split('/')[2]
    os.system("python xiami.py -s " + song_id)
    
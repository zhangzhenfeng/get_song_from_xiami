#!/usr/bin/env python2 
# coding:utf-8

import urllib2,os
import lxml.html,shutil
import pygame

# 获取配置文件内的配置信息
config = ""
if os.path.isfile("setting.config"):
    config = open("setting.config").readlines()
else:
    print("配置文件[setting.config]不存在")
# 存放配置信息的字典
config_dic = {}
for cfg in config:
    key,value = cfg.split(":")
    config_dic[key.replace("\n","")] = value.replace("\n","")

url = "http://www.xiami.com/chart/data?c=101&type=0&page=1&limit=10&_=1456582894957"
userAgent = " User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 "
headers = { 'User-Agent' : userAgent }
requst = urllib2.Request(url,headers = headers) 
result = urllib2.urlopen(requst).read()
 
# 开始获取返回数据的所有歌曲ID
html_obj = lxml.html.fromstring(result)
 
# 下载热曲前，先将之前的清空
# if os.path.exists("top10"):
#     shutil.rmtree("top10")
 
song_href = html_obj.xpath('tr//strong/a/@href')
for l in song_href[0:int(config_dic.get("top"))]:
    song_id = l.split('/')[2]
    #os.system("python xiami.py -s " + song_id)

print("下载结束，共下载%s首歌曲" % config_dic.get("top"))

# 找到音乐目录的所有文件，进行顺序播放
mp3_list = []
for file in os.listdir("top10"):
    print(file.decode("gbk"))
    if os.path.isfile("top10"+os.path.sep+file.decode("gbk")):
        mp3_list.append(file)
a = os.getcwd() + os.path.sep+"top10"+os.path.sep+mp3_list[0].decode("gbk")
print(a)
print("当前播放列表有%s"%mp3_list)
pygame.mixer.init()
# 循环播放
track2=pygame.mixer.Sound(a)
track2.play()
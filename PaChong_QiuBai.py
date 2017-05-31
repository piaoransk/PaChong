# -*- coding=utf-8 -*-
'''
@author: Administrator
@time:2017年5月28日}
@description:读取糗百text第一页的,用户名,内容
'''
# import urllib2
#  
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/text/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
#     regstr=r'_blank"\stitle=.*?">|"content">[\s\S]*?</span>'#爬虫备注：发帖人，发帖内容，赞的数量，但是找不到发帖时间
    regstr=r'h2.*?h2>|"content">[\s\S]*?</span>'#爬虫备注：发帖人，发帖内容，赞的数量，但是找不到发帖时间
#     pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    pattern=re.compile(regstr,re.S)
    items=re.findall(pattern,content)
    list_new=[]
#     print items
    length=len(items)
    for i in range(0,length-2,2):
        print 'i:' ,i
#         print len(items[i])
        print "title: ",items[i][3:-5]

#         print 'title_index: ',items[i].index('title')
#         span_index=items[i+1].index('span')
#         print span_index
#         print len(items[i+1])
        print "content:",items[i+1][20:-7]
#     print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

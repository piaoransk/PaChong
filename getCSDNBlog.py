# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: E:\TestScript\python\PaChong\getCSDNBlog.py

@time: 2018/1/8 10:06

@desc:get CSDN blog of xyh421
把我所有的文章爬下来
然后转换成md格式

'''

# import urllib2
#
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()
from tomd import Tomd
import urllib2
import re
import xlrd
import xlwt
from bs4 import BeautifulSoup
# from cycler import concat
import sys
import requests
reload(sys)

sys.setdefaultencoding('utf-8')
# href = '001374738125095c955c1e6d8bb493182103fac9270762a000'  # 2.7
content_type='application/x-www-form-urlencoded'
content_length='12'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'Content-Type': content_type, 'Content-Length': content_length, 'User-Agent': user_agent}
# data='id=reload...'
new_dict={}

def get_title(name):
    """
    获取所有文章的title和连接

    """
    url_index = 'https://blog.csdn.net/%s'%name
    url_prefix='http://blog.csdn.net'
    try:
        # request = urllib2.Request(url_index)
        # response = urllib2.urlopen(request)
        sock = requests.get(url_index)
        sock.endcoding = 'utf-8'
        data=sock.text
        soup=BeautifulSoup(data,'lxml')
        print type(soup)        #<class 'bs4.BeautifulSoup'>
        # print soup
        # soup = BeautifulSoup(html, 'lxml', from_encoding='gb18030')
        # filter_res=soup.find_all("a",)
        # print filter_res
        # re_cmd='.*?title="%s.*?'%(u'一人之下')
        # print re_cmd
        # filter_res=soup.find_all(title=re.compile('blog-title odd-overhidden bottom-dis-8') ,target="_blank" ,href=re.compile(r'/xyh421/article/details/'))
        # filter_res = soup.find_all(class_='blog-units blog-units-box') #<class 'bs4.element.ResultSet'>
        filter_res = soup.find_all(target="_blank", href=re.compile(r"blog.csdn.net/xyh421/article/details/"))  # <class 'bs4.element.ResultSet'>
        print type(filter_res)
        # print dir(filter_res)
        # filter_res1=filter_res.find_all(target="_blank", href=re.compile(r"blog.csdn.net/xyh421/article/details/"))
        # print filter_res
        # filter_res1=filter_res[0]
        # print type(filter_res1) #<class 'bs4.element.Tag'>
        # print filter_res1
        # filter_res = soup.find_all(href=re.compile(r'/xyh421/article/details/'))
        # print filter_res
        k=0
        PageInfo=[] #所有title 链接等待
        dict={}
        for i in filter_res:
            print "顺序",k
            # title = i.find_all(class_='blog-title bottom-dis-8')     #i  就是tag属性  title就是标题
            # if "'" in title:
            #     title=title.replace("'", "")
            # if '"' in title:
            #     title=title.replace('"', '')
            # p = i.parent        #整个大的块,块包含title,是否原创标签,时间,阅读人数,评论数
            print type(i)
            # print dir(i)
            url = i.get('href')
            #content = r"href=.*?target"
            # res= re.findall(i, content)
            # print res
            # pattern = re.compile(i, re.S)
            # print i.find(class_='blog-title bottom-dis-8')
            # print title
            # print(title.text)
            # readnum_tag = p.find_all(class_="icon iconfont icon-read")[0] #找到
            # read_num = readnum_tag.parent.text.strip()
            # table = p.find_all(class_="unit-con-left clearfix floatL")      #<class 'bs4.element.ResultSet'>
            # list = table[0].text.split()                                     #Tag  [u'\u539f\u521b', u'2016-08-04', u'15:43:53', u'9635', u'0']
            # print "title  %d : %s  hyperlink: %s"%(k, title, hyperlink)
            # dict["title"] = title
            # dict["hyperlink"] = hyperlink
            # dict["table"] = list
            # print dict
            # PageInfo.append(dict)
            # getpage(hyperlink,title)
            getpage(url)
            k+=1
            # if k==1:break
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    # print PageInfo
    return PageInfo


def getpage(address):
    try:
        sock = requests.get(address)
        data = sock.text
        soup = BeautifulSoup(data, 'lxml')
        print "type: ",type(data)
        article=soup.find_all(id="article_content")
        title = soup.find_all('h1')
        filename =  title[0].text
        print "filename: ",filename
        # del article[0][]
        # print article[0]
        # print soup.head
        fullname = "%s.html"%filename
        with open(fullname, "w") as f:
            f.write(soup.head.prettify()+article[0].prettify())
        # text=Tomd(data).markdown
        # # print text
        # with open(filename+'.md', 'w') as f:
        #     f.write(text)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

def correct_file_name():
    pass


def to_excel(dict1,excel_name):
    #to_excel(new_dict,'readIDs.xls')
    # 表格操作
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet Name")
    i=0
    for key in dict1:
        # print key, dict1[key]
        sheet.write(i, 0, key)  # row, column, value
        sheet.write(i, 1, dict1[key])  # row, column, value
        i=i+1
    workbook.save(excel_name)


def get_rows(excel_name):
    data = xlrd.open_workbook(excel_name)
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    print nrows
    return nrows

# 获取所有的title,网址
print get_title("xyh421")
# http://ac.qq.com/ComicView/index/id/531490/cid/388 一人之下：313
# getIMG("http://ac.qq.com/ComicView/index/id/531490/cid/388","一人之下：313")
getpage("https://blog.csdn.net/xyh421/article/details/79714596")

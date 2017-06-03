# -*- coding=utf-8 -*-
'''
@author: Administrator
@time:2017年5月28日
'''
# import urllib2
#
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()
import urllib2
import re
import xlrd
import xlwt

href = '001374738125095c955c1e6d8bb493182103fac9270762a000'  # 2.7
content_type='application/x-www-form-urlencoded'
content_length='12'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'Content-Type': content_type, 'Content-Length': content_length, 'User-Agent': user_agent}
data='id=reload...'
new_dict={}

def get_ids():
    url_index = 'http://shenfenzheng.293.net/'
    try:
        request = urllib2.Request(url_index, data=data, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        regstr = r'<td>.*?\s\d{18}</td>'  # 爬虫备注：发帖人，发帖内容，赞的数量，但是找不到发帖时间
        pattern = re.compile(regstr, re.S)
        items = re.findall(pattern, content)
        list_new = []
        # print items
        length = len(items)
        list1=[]
        print length
        for i in range(0, length):
            # print 'i:', i
            # print items[i]
            # print type(items[i])
            list1=items[i].split("<td>")
            # print list1[-1]
            list2=list1[-1].split(' ')
            # print list2
            name=list2[0]
            id=list2[1][:-5]
            # print "name :",name
            # print "id :",id
            new_dict[name]=id
        # print 'length of dict is  ',len(new_dict)

        # return new_dict
        return length
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

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
print 'length of dict is  ',len(new_dict)
num=0
for i in range(100):
    num1=get_ids()
    num=num+num1
    print "num:",num
    if num>1000:break
excel_name='readIDs.xls'
to_excel(new_dict,excel_name)
# get_rows(excel_name)
print 'done'

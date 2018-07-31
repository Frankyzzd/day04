# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 06抓取法院数据.py
@time: 2018/7/5 19:27
@author:frankyzzd
'''
import math
import time

import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

originUrl = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search.jsp?'

# POST的api接口
apiUrl = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'


#种子数据
data = {
    'yzm': 'tXxb',
    'ft': '',
    'ktrqks': '2018-07-05',
    'ktrqjs': '2018-08-05',
    'spc': '',
    'yg': '',
    'bg': '',
    'ah': '',
    'pagesnum': '1'
}

def getPageNum(apiUrl):

    res = requests.post(apiUrl,data=data,headers=headers).text
    # print(res)

    mytree = lxml.etree.HTML(res)

    totalNum = mytree.xpath('/html/body/div/div/font/strong/text()')[0]
    pageNum = math.ceil(int(totalNum)/15)
    return pageNum


def getInfo(url):
    pageNum = getPageNum(url)
    print(pageNum)
    for i in range(1,pageNum + 1):
        data = {
            'yzm': 'tXxb',
            'ft': '',
            'ktrqks': '2018-07-05',
            'ktrqjs': '2018-08-05',
            'spc': '',
            'yg': '',
            'bg': '',
            'ah': '',
            'pagesnum': i
        }
        res = requests.post(apiUrl, data=data, headers=headers).text
        # print(res)
        mytree = lxml.etree.HTML(res)
        infoList = mytree.xpath('//table[@id="report"]//tr[position()>1]')
        for info in infoList:
            fy = info.xpath('./td[1]/font/text()')[0]
            ft = info.xpath('./td[2]/font/text()')[0]
            fTime =  info.xpath('./td[3]/text()')[0]
            why = info.xpath('./td[5]/text()')[0]
            print(fy,ft,fTime,why)

def test():
    data = {
        'yzm': 'tXxb',
        'ft': '',
        'ktrqks': '2018-07-05',
        'ktrqjs': '2018-08-05',
        'spc': '',
        'yg': '',
        'bg': '',
        'ah': '',
        'pagesnum': '1460'
    }
    res = requests.post(apiUrl,data=data,headers=headers).text
    print(res)

if __name__ == '__main__':
    apiUrl = 'http://www.hshfy.sh.cn/shfy/gweb2017/ktgg_search_content.jsp'
    getInfo(apiUrl)
    # test()
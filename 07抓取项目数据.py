# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 07抓取项目数据.py
@time: 2018/7/5 19:58
@author:frankyzzd
'''
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
url = 'http://bbs.pinggu.org/prj/list/-4_1.html'
res = requests.get(url,headers=headers).text

mytree = lxml.etree.HTML(res)

prjList = mytree.xpath('//div[@class="liebiao_tiao"]')
pageNum = mytree.xpath('//a[@class="page_N"][last()]/text()')[0].replace('...','').strip()
print(pageNum)
for prj in prjList:
    prjNum = prj.xpath('./div[@class="guding"]/a/text()')[0]
    prjName = prj.xpath('./div[@class="ming"]/a/text()')[0]
    prjPrice = prj.xpath('./div[@class="jiage"]/text()')[0].strip()
    prjPerson = prj.xpath('./div[@class="renshu"]/text()')[0]
    prjTime = prj.xpath('./div[@class="shijian"]/text()')[0]
    print(prjNum,prjName,prjPrice,prjPerson,prjTime)
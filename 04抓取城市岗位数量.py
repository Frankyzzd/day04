# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 04抓取城市岗位数量.py
@time: 2018/7/5 17:18
@author:frankyzzd
'''
import re

import requests
import lxml
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

def getCityUrl(url):
    '''
    获取城市字典
    :param url: 种子url
    :return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/  67.0.3396.99 Safari/537.36'}

    res = requests.get(url,headers=headers).content.decode('gbk')
    mytree = lxml.etree.HTML(res)

    cityList = mytree.xpath('//div[@class="e e4"][1]/div[@class="lkst"]/a')

    cityDict = {}
    for city in cityList:
        cityName = city.xpath('./text()')[0]
        cityUrl = city.xpath('./@href')[0]
        cityDict[cityName] = cityUrl
        print(cityName,cityUrl)
    return cityDict


def getPageNum(url):
    res = requests.get(url, headers=headers).content.decode('gbk')

    mytree = lxml.etree.HTML(res)


    pageNum = mytree.xpath('//span[@class="td"]/text()')[0]
    pageNum = re.findall(r'共(\d+)页',pageNum)[0]
    return int(pageNum)

if __name__ == '__main__':
    url = 'https://jobs.51job.com/guangzhou/p1/'
    print(getPageNum(url))
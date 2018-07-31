# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 02抓取51城市列表.py
@time: 2018/7/5 17:04
@author:frankyzzd
'''

import requests
import lxml
from lxml import etree

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

if __name__ == '__main__':
    url = 'https://jobs.51job.com/'
    print(getCityUrl(url))
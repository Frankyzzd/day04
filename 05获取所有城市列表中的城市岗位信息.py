# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 05获取所有城市列表中的城市岗位信息.py
@time: 2018/7/5 17:50
@author:frankyzzd
'''
import re
import time

import requests
import lxml
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


#获取城市列表
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
    return cityDict

#获取城市所对应的岗位总页数
def getPageNum(url):
    res = requests.get(url, headers=headers).content.decode('gbk')

    mytree = lxml.etree.HTML(res)


    pageNum = mytree.xpath('//span[@class="td"]/text()')[0]
    pageNum = re.findall(r'共(\d+)页',pageNum)[0]
    return int(pageNum)

#获取城市岗位信息
def getCityInfo(cityUrl,totalPage,cityName):

    for i in range(1,totalPage+1):
        url = cityUrl+'p%d'%i
        res = requests.get(url,headers=headers).content.decode('gbk')

        mytree = lxml.etree.HTML(res)

        jobList = mytree.xpath('//div[@class="detlist gbox"]/div')
        if jobList:
            for job in jobList:
                jobName = job.xpath('./p[@class="info"]/span[1]/a/@title')[0]
                jobCompany = job.xpath('./p[@class="info"]/a/@title')[0]
                jobArea = job.xpath('./p[@class="info"]/span[2]/text()')[0]
                jobMoney = job.xpath('./p[@class="info"]/span[3]/text()')
                if jobMoney:
                    jobMoney =jobMoney[0]
                else:
                    jobMoney = ''
                jobOrders = job.xpath('./p[@class="order"]/text()')
                Orders = ''
                for jobOrder in jobOrders:
                    Orders += jobOrder.strip()
                jobDescription = job.xpath('./p[@class="text"]/@title')[0].replace(' ','')
                with open('./data/%s'%(cityName)+'.txt','a+',encoding='utf-8',errors='ignore') as f:
                    f.write(str((jobName,jobCompany,jobArea,jobMoney,Orders,jobDescription))+'\n')
                    f.flush()
                # print(jobName,jobCompany,jobArea,jobMoney,Orders,jobDescription+'\n')


if __name__ == '__main__':
    url = 'https://jobs.51job.com/'
    #获取城市:城市Url的字典
    cityDict = getCityUrl(url)
    cityName = input('请输入您想搜索的地区:')
    cityUrl = cityDict[cityName]
    print(cityUrl)
    jobPageNum = getPageNum(cityUrl)
    print(jobPageNum)
    time.sleep(1)
    getCityInfo(cityUrl,jobPageNum,cityName)
    # for cityName,cityUrl in cityDict.items():
    #     jobPageNum = getPageNum(cityUrl)
    #     time.sleep(1)
    #     getCityInfo(cityUrl,jobPageNum,cityName)

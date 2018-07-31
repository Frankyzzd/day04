# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 03抓取城市岗位信息.py
@time: 2018/7/5 17:17
@author:frankyzzd
'''
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}



def getCityInfo(url):
    res = requests.get(url,headers=headers).content.decode('gbk')

    mytree = lxml.etree.HTML(res)

    jobList = mytree.xpath('//div[@class="detlist gbox"]/div')
    if jobList:
        for job in jobList:
            jobName = job.xpath('./p[@class="info"]/span[1]/a/@title')[0]
            jobCompany = job.xpath('./p[@class="info"]/a/@title')[0]
            jobArea = job.xpath('./p[@class="info"]/span[2]/text()')[0]
            jobMoney = job.xpath('./p[@class="info"]/span[3]/text()')[0]
            if jobMoney:
                jobMoney =jobMoney
            else:
                jobMoney = ''
            jobOrders = job.xpath('./p[@class="order"]/text()')
            Orders = ''
            for jobOrder in jobOrders:
                Orders += jobOrder.strip()
            jobDescription = job.xpath('./p[@class="text"]/@title')[0]
            print(jobName,jobCompany,jobArea,jobMoney,Orders,jobDescription+'\n')

if __name__ == '__main__':
    url = 'https://jobs.51job.com/guangzhou/p1/'
    getCityInfo(url)
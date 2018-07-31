# encoding: utf-8
'''
@license: (C) Copyright 2018-2017, Node Supply Chain Manager Corporation Limited.
@contact: 905321213@qq.com
@file: 01xpath.py
@time: 2018/7/5 14:31
@author:frankyzzd
'''

import requests
import lxml
from lxml import etree

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul>
        <li id='l1' class="liClass">1</li>
        <li id='l2'>2</li>
        <li class="liClass">3</li>
        <li id='l4'>4</li>
        <li class="liClass" id="sb">5</li>
    </ul>

    <div class="liClass" id = "feu">feicai</div>
</body>
</html>
'''

mytree = lxml.etree.HTML(html_doc)

print(mytree.xpath('//div[@class="liClass"]/@id'))

print(mytree.xpath('//ul')[0].xpath('//li[2]'))
print(mytree.xpath('//li'))
print(mytree.xpath('//li[1]/text()'))
print(mytree.xpath('//li[last()]/@*'))
print(mytree.xpath('//li[last()]/@id="sg"'))
print(mytree.xpath('//li[last()]/@id="sb"'))
print(mytree.xpath('//*[@class="liClass"]'))
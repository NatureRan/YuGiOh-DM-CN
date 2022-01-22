# coding:utf-8

import requests
from lxml import etree
import json

if __name__ == '__main__':
    while True:
        print('输入卡片名称：')
        card_name = input('')
        try:
            search_url = 'https://www.ourocg.cn/search/'
            res = requests.get(search_url + card_name)
            html = etree.HTML(res.content)
            data = html.xpath('//script[2]')
            json_str = data[0].text.replace('window.__STORE__ = ', '')[:-2]
            json_map = json.loads(json_str)
            hash_id = json_map['cards'][0]['hash_id']
            url = 'https://www.ourocg.cn/card/' + hash_id
            res = requests.get(url)
            html = etree.HTML(res.content)
            cn_name = html.xpath("//div[@class='val el-col-xs-18 el-col-sm-12 el-col-md-14 el-col-sm-pull-8 el-col-md-pull-6']/template[2]")
            effect = html.xpath("//div[@class='val el-col-24 effect']/template[2]")
            print('中文名：', cn_name[0].text.strip())
            print('效果：',effect[0].text.strip())
        except Exception as e:
            print('查询失败：', e)
        print('------------------------------------')

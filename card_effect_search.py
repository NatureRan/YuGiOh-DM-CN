# coding:utf-8

import requests
from lxml import etree
import json,difflib,re

def name_similar_en(name1, name2):
    if not name1 or not name2:
        return 0
    ratio = difflib.SequenceMatcher(None, name1.lower(), name2.lower()).quick_ratio()
    return ratio

def search_card(card_name):
    search_url = 'https://www.ourocg.cn/search/'
    card = None
    similar_ratio = 0
    for i in range(1, 5):
        res = requests.get(search_url + card_name + '/' + str(i))
        html = etree.HTML(res.content)
        data = html.xpath('//script[2]')
        json_str = data[0].text.replace('window.__STORE__ = ', '')[:-2].strip()
        json_map = json.loads(json_str)
        cards = json_map['cards']
        if not cards:
            break
        for c in cards:
            ratio = name_similar_en(card_name, c['name_en'])
            if ratio - similar_ratio > 0:
                similar_ratio = ratio
                card = c
        if len(cards) < 10:
            break
            
    if card:
        print('英文名:', card['name_en'])
        print('中文名:', card['name'])
        print('效果/描述:', card['desc_nw'])
    else:
        print('没有查询到相关卡片信息')


if __name__ == '__main__':
    while True:
        print('输入卡片名称：')
        card_name = input('')
        try:
            search_card(card_name)
        except Exception as e:
            print('查询失败：', e)
        print('------------------------------------')

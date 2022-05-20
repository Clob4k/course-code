# 1.1.2 AmazonCrawler.py

import requests


url = "https://www.amazon.cn/gp/product/B01M9XJZQA"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

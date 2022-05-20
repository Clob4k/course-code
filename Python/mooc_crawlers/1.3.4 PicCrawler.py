# 1.3.4 PicCrawler.py

import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/0702/20170702095646773.jpg"
root = "D:/Python/mooc_crawlers/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
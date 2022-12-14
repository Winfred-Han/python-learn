#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import os
import requests
from bs4 import BeautifulSoup
import re
# 定义请求url

url_base = "http://tupu.3456.tv/liangshizuowu"
# 定义请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 爬取的数据存放位置
folder="E:/作物病虫害"

# 从虫害种类
desease_list=["binghai_9","chonghai_9"]

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"
folder_flag = 0
for d in desease_list:
    count = 0
    file_flag = 0
    desease_type=None
    response = requests.get(
        url=url_base + f"/{d}-{1}",
        headers=headers,
        verify=False
    )
    content = response.content
    # 转换成字符串
    string = content.decode(response.encoding)
    # 把字符串转成python数据类型
    # html字符串创建BeautifulSoup对象
    soup = BeautifulSoup(string, 'html.parser', from_encoding='utf-8')

    a_tag_list = soup.select("#main > div > div.leftbuf > div.left1 > div.classPages > div > div.dev_pgnum")[0]
    pageSize = len(soup.select("#main > div > div.leftbuf > div.left1 > div.classPages > div > div.dev_pgnum")[0].find_all("a")) + 1
    for i in range(1,pageSize+1) :
        res = requests.get(
            url=url_base+f"/{d}-"+str(i),
            headers=headers,
            verify=False
        )
        content = res.content
        # 转换成字符串
        string = content.decode(res.encoding)
        # html字符串创建BeautifulSoup对象
        soup = BeautifulSoup(string, 'html.parser', from_encoding='utf-8')

        for a in soup.find_all("a",{"class":{"nav"}}):
            if(a["class"][0]== "nav"):
                count += 1
                if(count==1 and folder_flag==0):
                    folder_flag=1
                    folder=folder +"/"+ a.string
                    mkdir(folder)
                if(count==2 and file_flag==0):
                    file_flag=1
                    desease_type=a.string
                    f = open(folder + f"/{a.string}.txt", "a", encoding="utf-8")
                    print(f"病虫害分类：{a.string}")
        for a in soup.find_all("a",{"target":{"_blank"}}):
            if(a["href"].startswith("http://zhuanti.3456.tv/weixin")):
                break
            if(a["href"].startswith("/news/")):
                    if(a.string!=None and a.string!=""):
                        print(f"{desease_type}:{a.string}")
                        f.write(f"{desease_type}:{a.string}" + "\n")

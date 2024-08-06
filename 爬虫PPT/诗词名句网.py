# -*- coding: utf-8 -*-

#%%爬取诗词名句网排名页面的信息（链接地址https://www.shicimingju.com/paiming），
# 诗词网
import requests
from bs4 import BeautifulSoup
import os
import re
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei'] 

# 向服务器发送请求并获取html源代码的函数
def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        # requests.packages.urllib3.disable_warnings()
        r = requests.get(url, headers=headers,verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text  # 返回网页源代码。
    except Exception as e:
        print(e)


def get_info(soup):
    all_divs = soup.find_all('div', class_='card shici_card')
    for a in all_divs:
        # 排名
        info = a.find('div', class_='list_num_info')
        no = info.find('span').get_text()
        print("第{}名:".format(no), end="")
        # 标题
        titles = a.h3.get_text()
        print("{}".format(titles))
        # 朝代
        time = re.search('<br/?>(.*?)<br/?>', str(info), re.S | re.M).group(1)
        print("朝代：", time[1:-1])  # 去除朝代两端的中括号
        if time[1:-1] != '':
            dynasty.append(time[1:-1])
        else:
            print("第{}名无朝代".format(no),end="")
        # 作者
        name = info.find('a').get_text().strip()
        print("诗人：{}".format(name))
        # 图片保存
        picDiv = a.find('div', class_='shici_list_pic')
        if not picDiv:
            print("无图片")
        else:
            pic_url = picDiv.find('img').get("src")            
            root = r"c:/t2/"
            path = root + str(no) + '.' + pic_url.split('.')[-1]
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r = requests.get("https://www.shicimingju.com/{}".format(pic_url))
                    r.raise_for_status()
                    with open(path, 'wb') as f:
                        f.write(r.content)
                        print("文件保存成功")
                else:
                    print("文件已存在")
            except:
                print("产生异常")
    return dynasty


# 统计各朝代诗词数量和绘图
def cou(dynasty):
    # 统计
    dyn_n = []
    count_n = []
    for who in set(dynasty):
        dyn_n.append(who)
        count_n.append(dynasty.count(who))
        print(who, ':', dynasty.count(who))
    # 绘制
    plt.figure()
    plt.title('各朝代诗词')
    plt.xlabel('朝代')
    plt.ylabel('诗词数量')
    plt.bar(x=dyn_n, height=count_n, width=0.8)
    for i, j in zip(dyn_n, count_n):
        plt.text(i, j, j, va='bottom', ha='center')


dynasty = []
for num in range(1,2):#range(1,101)
    url = 'https://www.shicimingju.com/paiming?p=' + str(num)
    content = get_page(url)
    if content:
        soup = BeautifulSoup(content,'html.parser')
        get_info(soup)
cou(dynasty)

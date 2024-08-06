# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests  
url="https://blog.csdn.net/WhereIsHeroFrom?type=blog"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
           AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/74.0.3729.108 Safari/537.36"}
# 获取页面信息
r = requests.get(url,headers=headers)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, 'html.parser')

#用户名
name=soup.find("div",class_="user-profile-head-name" )
print(name.div.text)
#总访问量、原创等数据
num=soup.find_all("div",class_="user-profile-statistics-num")
for nu in num:
    print(nu.text)
#个人简介    
profile=soup.find("p",class_="introduction-fold default")
print(profile.text)
#前10个文章标题（按“最近”栏目中，发布时间）
article=soup.find_all("div",class_="blog-list-box-top")
for a in article[:10]:
    print(a.text)
#第一篇文章的阅读数   
view_num=soup.find("span",class_="view-num")
print(view_num.text)
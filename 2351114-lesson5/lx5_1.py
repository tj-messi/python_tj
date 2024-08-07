# 2351114 朱俊泽 大数据科学与技术
'''
参考https://www.cnblogs.com/machangwei-8/p/10738244.html  学习xlwt 写入excel的使用

1）实现抓取https://top.baidu.com/board 十条百度热搜的文字
2)将抓取的十条百度热搜写入 hot_list.xls
'''
import requests
from bs4 import BeautifulSoup
import xlwt


# 抓取百度热搜的前十条文字
def fetch_baidu_hot_search():
    url = 'https://top.baidu.com/board'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到热搜榜，对应的 <div class_="content_1YWBm">
    hot_search_list = soup.find_all('div', class_='c-single-text-ellipsis')

    # 提取前十条热搜文字
    top_ten_hot_search = []
    id=1
    for item in hot_search_list[:20]:
        if (id % 2 == 1):
            id+=1
        else:
            id += 1
            title = item.text.strip()
            top_ten_hot_search.append(title)

    return top_ten_hot_search


# 将抓取的热搜写入Excel文件
def write_to_excel(hot_list, filename):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('百度热搜')

    # 写入表头
    worksheet.write(0, 0, '排名')
    worksheet.write(0, 1, '热搜关键词')

    # 写入数据
    for index, keyword in enumerate(hot_list):
        worksheet.write(index + 1, 0, index + 1)
        worksheet.write(index + 1, 1, keyword)

    workbook.save(filename)


if __name__ == '__main__':
    hot_list = fetch_baidu_hot_search()
    write_to_excel(hot_list, 'hot_list.xls')
    print("数据已成功写入 hot_list.xls 文件。")

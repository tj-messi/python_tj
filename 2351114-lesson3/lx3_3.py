#2351114 朱俊泽 大数据科学与技术
'''
读入course.txt 的数据
输入关键字，显示包含该关键字所有数据
请输入要搜索的关键字：王
共找到5条数据：
{'学号': '2350489', '姓名': '王奕杰', '英文姓名': 'Wang Yijie', '性别': '男', 'score': [{'学期': '2023上', '英语': 88.0, '高程': 91.5}, {'学期': '2023下', '英语': 89.5, '高程': 90.5, '摄影': 88.0}]}
{'学号': '2351592', '姓名': '王丽宁', '英文姓名': 'Wang Lining', '性别': '女', 'score': [{'学期': '2023上', '英语': 88.0, '高程': 91.5, '高数': 88.5}, {'学期': '2023下', '英语': 90.5, '高程': 90.5, '高数': 88.5, '摄影': 88.0}]}
{'学号': '2351884', '姓名': '王晓涵', '英文姓名': 'wang xiao han', '性别': '女', 'score': [{'学期': '2023上', '英语': 93.0, '高程': 86.0}, {'学期': '2023下', '英语': 90.0, '高程': 88.0}]}
{'学号': '2352837', '姓名': '王采毅', '英文姓名': 'CaiYi Wang', '性别': '女', 'score': [{'学期': '2023上', '英语': 87.0, '高程': 88.0, '高数': 99.0}, {'学期': '2023下', '英语': 86.0, '高程': 88.0}]}
{'学号': '2353606', '姓名': '王瀚威', '英文姓名': 'Wang Hanwei', '性别': '男', 'score': [{'学期': '2023下', '英语': 99.0, '高程': 92.0, '高数': 97.0}, {'学期': '2023下', '英语': 88.0, '高程': 99.0, '高数': 98.0}]}

-------------------
请输入要搜索的关键字：海
没找到相关数据
'''

from typing import Optional
import json

def read_json_file(filename: Optional[str] = 'course.txt'):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)#拿到json文件
    return data


def json_query(query_str: Optional[str]):
    datas = read_json_file()  # 读取JSON文件内容
    res = []
    for data in datas:
        # 尝试将data转换为字符串，以便进行包含检查
        if query_str and query_str in str(data):
            res.append(data)
    return res


if __name__ == "__main__":
    query_str = input("请输入要搜索的关键字：")
    query_ans = json_query(query_str)
    ans_num = len(query_ans)

    if ans_num == 0:#没找到
        print("没找到相关数据！")
    else:
        print(f"共找到{ans_num}条数据：\n")
        for data in query_ans:
            #打印整个字典
            print(data)

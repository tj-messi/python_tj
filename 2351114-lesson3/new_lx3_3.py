
from typing import Optional
import json
def read_json_file(filename: Optional[str] = 'course.txt'):
    # 这里我们使用一个模拟的字典来代替从文件读取的JSON数据
    # 实际应用中，这里应该是通过某种方式（非json库）从文件中提取的字典
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)  # 拿到json文件
    return data


def json_query(query_str: Optional[str], datas=None):
    if datas is None:
        datas = read_json_file()
    res = []
    for data in datas:
        # 将data转换为字符串（如果它不是字符串），以便进行包含检查
        if query_str and query_str in str(data):
            res.append(data)
    return res


if __name__ == "__main__":
    query_str = input("请输入要搜索的关键字：")
    query_ans = json_query(query_str)
    ans_num = len(query_ans)

    if ans_num == 0:
        print("没找到相关数据！")
    else:
        print(f"共找到{ans_num}条数据：\n")
        for data in query_ans:
            print(data)
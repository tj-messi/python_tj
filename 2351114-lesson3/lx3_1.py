#2351114 朱俊泽 大数据科学与技术
'''
学习json库的基础使用
编写excel_to_json.py ，将上次Table_merge 合成的结果导出为json格式文本文件course.txt
要求同一学生的多条数据合并为一条字典格式数据，形如：
[{“学号”: “2250889”, “姓名”: “廖玲艺”, “英文姓名”: “Liao Lingyi”, “性别”: “女”, “score”: [{“学期”: “2023上”, “英语”: 90.0, “高程”: 80.0}, {“学期”: “2023下”, “英语”: 93.0, “高程”: 93.0, “高数”: 99.0}]}, {“学号”: “2250951”, “姓名”: “陈麒安”, “英文姓名”: “Chen Qian”, “性别”: “男”, “score”: [{“学期”: “2023上”, “英语”: 88.0, “高程”: 99.0, “高数”: 98.0}, {“学期”: “2023下”, “英语”: 92.0, “高程”: 88.0}]}。。。。]
在转为json时，最好没有“物理”:“”,“高程”:“”,“摄影”:“”类似的空数据。学号不要带小数点。
'''

import json
import xlrd
from typing import Optional, List


def read_xls(sh: Optional[int] = 0, filename: Optional[str] = './score.xls'):

    xls = xlrd.open_workbook(filename)
    sheet = xls.sheets()[sh] # 使用sheet_by_index而不是sheets()[sh]
    names = sheet.row_values(0)  # 获取第一行的列名
    data = []
    for row_idx in range(1, sheet.nrows):
        data.append(sheet.row_values(row_idx))  # 遍历除标题行外的每一行
    return names, data  # 返回列名和数据

def table_merge(main_table: Optional[List[List]], foreign_table: Optional[List[List]]) -> List[List]:

        # 将main_table转换为没有重复行
    main_table = list(map(list, set(map(tuple, main_table))))
    main_dict = {item[0]: item for item in main_table}

    merge_data = []
    for item in foreign_table:
        number = item[0]
        main_info = main_dict.get(number)
        if main_info:
            # 合并数据，取main_info除第一个元素外的所有元素和foreign_table当前行的剩余元素
            merge_data.append(main_info + item[1:])

    return merge_data

def query_by_no(keys: Optional[List], datas: Optional[List], student_no: Optional[str]):
    query_datas = []
    for data in datas:
        if data[0] == student_no:  # 数据中存储学生学号的键是 'student_no'
            query_datas.append(data)

    if query_datas:
        query_ans = [{keys[i]: query_data[i] for i in range(len(keys))} for query_data in query_datas]
    else:
        print(f"Number {student_no} can't be found.")
        query_ans = {}

    return query_ans

def get_numbers(datas: Optional[list],number_pos: Optional[int] = 0):

    numbers = []
    for data in datas:
        numbers.append(data[number_pos])
    return list(set(numbers))


def excel_to_json(keys: Optional[list], datas: Optional[list], main_keys: Optional[list], score_keys: Optional[list],
                  output_filename: Optional[str] = 'course.txt'):

    numbers = get_numbers(datas)
    all_datas = []
    for number in numbers:
        query_data = query_by_no(keys, datas, number)
        query_dict = {}
        score_part = []

        # 填充主要字段
        for main_key in main_keys:
            example = query_data[0]
            query_dict[main_key] = example[main_key]

        # 填充分数字段
        for data in query_data:
            score_dict = {}
            for key in score_keys:
                if data[key] != ':':  # ':'无效
                    score_dict[key] = data[key]
            score_part.append(score_dict)
        query_dict['score'] = score_part  # 分数部分存储的键是'score'

        all_datas.append(query_dict)

    with open(output_filename, 'w', encoding='UTF-8') as file:
        json.dump(all_datas, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main_names, main_table = read_xls(1)
    foreign_names, foreign_table = read_xls(0)
    all_names = main_names + foreign_names[1:]
    merge_data = table_merge(main_table, foreign_table)
    excel_to_json(all_names, merge_data, main_names, foreign_names)
#2351114 朱俊泽 大数据科学与技术
'''
读入course.txt 的数据
输入学号和课程名，输出该学号对应课程的成绩。
请输入学号:2250951
请输入课程名称：高程
{'学号': '2250951', '姓名': '陈麒安', '英文姓名': 'Chen Qian', '性别': '男', 'score': [{'学期': '2023下', '高程': 88.0}, {'学期': '2023下', '高程': 88.0}]}
请输入学号:2250951
请输入课程名称：摄影
该学号对应的摄影成绩没找到
'''

from typing import Optional
import json
def read_json_file(filename: Optional[str] = 'course.txt'):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)#拿到json文件
    return data


def query_score(datas: Optional[list],number: Optional[str],course_name: Optional[str]):
    query_dict = {}
    for data in datas:
        if data['学号'] == number:#切分学号出来
            query_dict = data
            scores = query_dict['score']
            course_scores = []
            semester_key = '学期'
            for score in scores:#对比score
                if course_name in score:
                    course_scores.append({semester_key: score[semester_key],
                                          course_name: score[course_name]})
            if not course_scores:
                return None
            else:
                query_dict['score'] = course_scores
                return query_dict


if __name__ == '__main__':
    data = read_json_file()
    number = input('请输入学号:')
    course_name = input('请输入课程名称:')
    res = query_score(data, number, course_name)
    if res is None:
        print(f"该学号{number}对应的{course_name}成绩没找到")#没找到
    else :
        print(res)#找到
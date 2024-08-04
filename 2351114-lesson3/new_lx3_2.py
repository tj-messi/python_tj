
from typing import Optional
import json
def mock_read_json_file(filename: Optional[str] = 'course.txt'):
    # 这里我们使用一个模拟的字典来代替从文件读取的JSON数据
    # 实际应用中，这里应该是通过某种方式（非json库）从文件中提取的字典
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)  # 拿到json文件
    return data


def query_score(datas: Optional[list], number: Optional[str], course_name: Optional[str]):
    query_dict = None
    for data in datas:
        if data['学号'] == number:
            query_dict = data
            break
    if query_dict is None:
        return None

    scores = query_dict.get('score', [])
    course_scores = []
    for score in scores:
        if course_name in score:
            course_scores.append({"学期": score["学期"], course_name: score[course_name]})

    if not course_scores:
        return None
    else:
        query_dict['score'] = course_scores
        return query_dict


if __name__ == '__main__':
    data = mock_read_json_file()
    number = input('请输入学号:')
    course_name = input('请输入课程名称:')
    res = query_score(data, number, course_name)
    if res is None:
        print(f"该学号{number}对应的{course_name}成绩没找到")
    else:
        print(res)
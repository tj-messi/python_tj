#2351114 朱俊泽 大数据科学与技术
'''
在练习二基础上，实现 query_by_no(studenet_no),函数
要求使用自己的学号，返回结果要求构造为字典格式。
（有两条数据，只取其中1条即可）

输出示例：
{'学号': '2352045', '姓名': '闫童童', '英文姓名': 'Yan Tongtong', '性别': '女', '学期': '2023上', '英语': 92.0, '高程': 92.0, '物理': 88.5, '高数': '', '摄影': ''}
'''
import xlrd
import lx2_2
import lx2_1

def query_by_no(student_no) :
    arr=['学号','姓名','英文姓名','性别','学期','英语','高程','物理','高数','摄影']
    dic_s={}
    for i in range (len(li_merge)) :
        number=str(li_merge[i][0])
        if number == str(student_no) :
            for item in range(len(li_merge[i])) :
                dic_s[arr[item]] =li_merge[i][item]
    return dic_s




if __name__ == '__main__':
    t1_title, t1_data = lx2_1.read_xls(0)
    t2_title, t2_data = lx2_1.read_xls(1)
    li_merge = lx2_2.table_merge(t1_data, t2_data)
    print(query_by_no(2351114))
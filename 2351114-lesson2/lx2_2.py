#2351114 朱俊泽 大数据科学与技术
'''
在练习一基础上，实现 table_merge(li_1,li_2),函数返回为合并后list
Li_1 为第一个sheet内容，li_2为第二个sheet内容
合并后的结果列要求只有一列‘学号’
示例['2251935', '胡诗雨', '女', '数据科学与大数据技术', '2023上', 90.0, 80.0, '', '', '']
'''
import xlrd
import lx2_1

def table_merge(li_1,li_2):
    merged_data = []
    for i in range(len(li_1)):
        xuehao = str(li_1[i][0])#取出学号位
        for j in li_2:
            if xuehao==j[0] :#对比第二个表中如果学号相同就合上去
                merge_temp=j + li_1[i][1:]#单列
                merged_data.append(merge_temp)#二维（总表）
    return merged_data

if __name__ == '__main__':
    t1_title,t1_data=lx2_1.read_xls(0)
    t2_title,t2_data=lx2_1.read_xls(1)
    li_merge=table_merge(t1_data,t2_data)
    for i in li_merge:
        print(i)
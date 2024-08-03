#2351114 朱俊泽 大数据科学与技术
'''
针对cj.xls   编写一个read_xls(sh)函数，该函数以list of list 形式返回对应工作簿的数据内容，另外还以list形式返回第一行标题。
约定：第一行为标题，第一列为学号
Sh=0 读取第一个sheet,sh=1时，读取第二个sheet

读取excel文件的第三方库 Xlrd 使用简介参考
https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
'''

import xlrd


def read_xls(sh):
    file_path = 'score.xls'
    """  
    读取Excel文件中的一个工作表，并返回标题行和数据。  

    参数:  
    file_path (str): Excel文件的路径。  
    sh (int): 要读取的工作表的索引，索引从0开始。  

    返回:  
    tuple: 包含两个元素的元组，第一个元素是标题行（列表），第二个元素是数据（列表的列表）。  
    """
    # 打开Excel文件
    work_book = xlrd.open_workbook(file_path)
    # 通过索引获取工作表
    work_sheet = work_book.sheet_by_index(sh)

    # 获取总行数
    sh_rows = work_sheet.nrows
    # 读取第一行作为标题
    sh_title = work_sheet.row_values(0)
    # 初始化数据列表
    sh_data = []

    # 遍历除了标题行以外的所有行
    for row_index in range(1, sh_rows):
        sh_data.append(work_sheet.row_values(row_index))

    return sh_title, sh_data



if __name__ == '__main__':


    # 读取第一个工作表
    sh_title, sh_data = read_xls(0)
    if sh_title and sh_data:
        print(sh_title)
        for i in sh_data:#遍历sh-data也可以 for i in(len(sh_data))此时是遍历索引
            print(i)

    # 读取第二个工作表
    sh_title1, sh_data1 = read_xls( 1)
    if sh_title1 and sh_data1:
        print(sh_title1)
        for i in sh_data1:
            print(i)
    #根据老师给的网址--https://www.cnblogs.com/insane-Mr-Li/p/9092619.html
    #xlrd库应该只能实现对xls的读取，xlsx会出错，注意中文也可能出错

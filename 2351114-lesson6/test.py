import pandas as pd

# 读取 Excel 文件的 sheet1
def load_data(file_name):
    df = pd.read_excel(file_name, sheet_name='Sheet1')
    return df

# 根据学号查询目标行数
def query_student_by_id(df, student_id):
    result = df[df['学号'] == student_id]
    if result.empty:
        return f"学号 {student_id} 不存在"
    else:
        # 返回匹配行的索引和数据
        idx = result.index[0]
        return f"目标行数: {idx + 2}\n{result.to_string(index=False)}"  # +2 是因为 Excel 第1行为标题行

# 测试
if __name__ == "__main__":
    for i in range (30) :
        file_name = '2班审核用.xlsx'  # 替换为你的 Excel 文件名
        df = load_data(file_name)
        student_id = int(input("请输入学号查询目标行数: "))
        print(query_student_by_id(df, student_id))

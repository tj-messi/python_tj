#2351114 朱俊泽 大数据科学与技术
'''
编写st_lesson对象，该对象有属性
st_no    #学号 字符串
st_name   #姓名 字符串
st_py  #拼音姓名 字符串
st_sex   #性别  字符串
st_course_list:  #该生选课情况 一维列表：形如：[“物理”,”英语”,”高尔夫”]
st_schedule_list:  #该生课表 五行六列的二维列表 形如
[[“上课时间”，“周一”，“周二”，“周三”，“周四”，“周五”],
[“上午一二节”，“德语”，“深度学习,经济管理”，“德语”，“英语”，“英语”],
[“上午三四节”，“物理”，””，”物理,python语言“，”“，”数据结构”],
[“下午一二节”,“柔道”，“导论,太极拳”，“”，“”，“”],
[“下午三四节”，“”，“”，“”，“”，“电影欣赏,太极拳”]


该对象的构造函数__init__(self)  ：实现自动读取xuanke.xls, 将自己学号对应的数据赋值给st_no、st_name  、st_py  、st_sex   、st_course_list:  st_schedule_list


该对象有方法display_schedule(self)  屏幕print输出课表形如下
学号：X1X2X3X4X5X6X7 姓名：XXX 的课表
上课时间		周一		周二			周三		周四		周五
上午一二节		德语	深度学习,经济管理	德语		英语		英语
上午三四节		物理	物理			python语言	数据结构
下午一二节		柔道	导论,太极拳,
下午三四节”  										电影欣赏 		太极拳
注：自学一下字符串固定输出占位20字符，   因英文与汉字显示大小不统一造成不对齐问题可忽略。

该对象的第二个方法check_conflict()
输出自己对应的选课时间冲突情况。
输出示例
Your name的选课冲突有：[周一上午一二节['高数', '德语']][周三上午一二节['高数', '德语']][周五上午三四节['c语言', '数据结构']][周一下午一二节['英语', '网络基础', '柔道']][周三下午一二节['经济管理', '太极拳']][周四下午一二节['数据库', '高尔夫']][周五下午一二节['马哲', '游泳']]
'''
import pandas as pd

class st_lesson:
    def __init__(self, st_no):
        self.st_no = st_no
        self.st_name = ""
        self.st_py = ""
        self.st_sex = ""
        self.st_course_list = []
        self.st_schedule_list = [
            ["上课时间", "周一", "周二", "周三", "周四", "周五"],
            ["上午一二节", "", "", "", "", ""],
            ["上午三四节", "", "", "", "", ""],
            ["下午一二节", "", "", "", "", ""],
            ["下午三四节", "", "", "", "", ""]
        ]

        self.load_data_from_excel()

    def load_data_from_excel(self):
        # 读取表1
        df1 = pd.read_excel('xuanke.xls', sheet_name=0)
        student_data = df1[df1['学号'] == int(self.st_no)].iloc[0]

        self.st_name = student_data['姓名']
        self.st_py = student_data['英文姓名']
        self.st_sex = student_data['性别']

        # 读取表2
        df2 = pd.read_excel('xuanke.xls', sheet_name=1)
        student_courses = df2[df2['学号'] == int(self.st_no)].iloc[0]
        self.st_course_list = student_courses.index[student_courses == '√'].tolist()

        # 读取表3
        df3 = pd.read_excel('xuanke.xls', sheet_name=2)

        # 使用 iterrows() 来遍历所有行
        for _, row in df3.iterrows():
            time_slot = row['上课时间']
            index = self._get_time_index(time_slot)
            if index == -1:
                continue  # 如果时间索引无效，跳过

            for day in range(1, 6):  # 从周一到周五
                courses = row.iloc[day] # 使用 iloc 确保按位置获取
                if isinstance(courses, str):  # 确保读取到字符串
                    course_list = [course.strip() for course in courses.split(',')]  # 分割课程并去除空格
                    self.st_schedule_list[index][day] = ", ".join(course for course in course_list if course in self.st_course_list)

    def _get_time_index(self, time_slot):
        # 帮助方法，将上课时间映射到二维数组的索引
        mapping = {
            "上午一二节": 1,
            "上午三四节": 2,
            "下午一二节": 3,
            "下午三四节": 4
        }
        return mapping.get(time_slot, -1)

    def display_schedule(self):
        print(f"学号：{self.st_no:<20} 姓名：{self.st_name:<20} 的课表")

        # 打印表头信息（周几）
        header_row = self.st_schedule_list[0]
        print("".join(f"{str(cell):<20}" for cell in header_row))  # 课程时间标题行为20宽

        # 打印课程信息
        for row in self.st_schedule_list[1:]:  # 从第一行课程信息开始
            print("".join(f"{str(cell):<20}" for cell in row))  # 每个单元格宽度固定为20个字符，左对齐

    def check_conflict(self):
        conflicts = []
        for course in self.st_course_list:
            for i in range(1, len(self.st_schedule_list)):
                for j in range(1, len(self.st_schedule_list[i])):
                    current_courses = self.st_schedule_list[i][j]
                    if course in current_courses.split(', '):
                        # 找到对应的时间并记录
                        conflicts.append(f"[{self.st_schedule_list[0][j]}{self.st_schedule_list[i][0]}[{course}]]")
                    else:
                        continue
        if conflicts:
            print(f"{self.st_name}的选课冲突有：{' '.join(conflicts)}")
        else:
            print(f"{self.st_name}没有选课冲突")


# 示例使用
student = st_lesson('2351114')
student.display_schedule()
student.check_conflict()



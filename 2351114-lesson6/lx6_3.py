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


class StLesson:
    def __init__(self, st_no):
        self.st_no = st_no
        self.st_name = "XXX"
        self.st_py = "XXX"
        self.st_sex = "XXX"
        self.st_course_list = []
        self.schedule = pd.DataFrame(columns=["上课时间", "周一", "周二", "周三", "周四", "周五"])
        self.load_data_from_excel()

    def load_data_from_excel(self):
        df_info = pd.read_excel('xuanke.xls', sheet_name=0)  # 学生信息表
        df_selection = pd.read_excel('xuanke.xls', sheet_name=1)  # 选课情况表
        df_schedule = pd.read_excel('xuanke.xls', sheet_name=2)  # 课程时间表

        # 提取学生信息
        student_info = df_info[df_info['学号'] == int(self.st_no)]
        if not student_info.empty:
            self.st_name = student_info.iloc[0]['姓名']
            self.st_py = student_info.iloc[0]['英文姓名']  # 假设有这个字段
            self.st_sex = student_info.iloc[0]['性别']
        else:
            print(f"学号 {self.st_no} 未在学生信息表中找到。")
            return

        # 获取选课情况
        student_selection = df_selection[df_selection.iloc[:, 0] == int(self.st_no)]
        if not student_selection.empty:
            course_columns = df_selection.columns[1:]
            self.st_course_list = [course for course, selected in zip(course_columns, student_selection.iloc[0, 1:]) if selected == '√']
        else:
            print(f"学号 {self.st_no} 未在选课表中找到选课信息。")
            return

        # 从课程时间表中读取课表信息
        self.schedule = df_schedule

    def display_schedule(self):
        print(f"学号：{self.st_no} 姓名：{self.st_name} 的课表")
        for row in self.schedule.itertuples(index=False):
            print(" | ".join(str(item).ljust(20) for item in row))

    def mark_selected_courses(self):
        # 标记所选课程在时间表中的位置
        for course in self.st_course_list:
            for i in range(len(self.schedule)):
                # 找到课程在表三中的位置
                if course in self.schedule.columns:
                    j = self.schedule.columns.get_loc(course)  # 找到列索引
                    if self.schedule.iloc[i, j] == course:  # 确认该位置为课程
                        time_slot = self.schedule.iloc[i, 0]  # 获取对应的上课时间
                        print(f"课程 '{course}' 的上课时间：{time_slot} 在表上标记")

                        # 输出标记后的表格
                        self.schedule.iloc[i, j] = course  # 在课程位置加上课程名

        # 输出标记后的课程时间表
        print("\n标记后的课程时间表：")
        for row in self.schedule.itertuples(index=False):
            print(" | ".join(str(item).ljust(20) for item in row))


# 示例使用
student = StLesson('2351114')
student.display_schedule()
student.mark_selected_courses()

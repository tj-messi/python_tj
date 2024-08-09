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
        df = pd.read_excel("xuanke.xls")
        student_data = df[df['学号'] == self.st_no].iloc[0]
        self.st_name = student_data['姓名']
        self.st_py = student_data['拼音姓名']
        self.st_sex = student_data['性别']
        self.st_course_list = student_data['选课情况'].split(',')
        self.st_schedule_list = [
            ["上课时间", "周一", "周二", "周三", "周四", "周五"],
            ["上午一二节", *student_data['上午一二节'].split(',')],
            ["上午三四节", *student_data['上午三四节'].split(',')],
            ["下午一二节", *student_data['下午一二节'].split(',')],
            ["下午三四节", *student_data['下午三四节'].split(',')]
        ]

    def display_schedule(self):
        print(f"学号：{self.st_no} 姓名：{self.st_name} 的课表")
        for row in self.st_schedule_list:
            print("".join(f"{item:^20}" for item in row))

    def check_conflict(self):
        conflict_dict = {}
        for i in range(1, len(self.st_schedule_list)):
            for j in range(1, len(self.st_schedule_list[i])):
                courses = self.st_schedule_list[i][j].split(',')
                if len(courses) > 1:
                    time_slot = self.st_schedule_list[i][0] + self.st_schedule_list[0][j]
                    conflict_dict[time_slot] = courses

        if conflict_dict:
            print(f"{self.st_name}的选课冲突有：")
            for time_slot, courses in conflict_dict.items():
                print(f"[{time_slot}{courses}]", end="")
            print()
        else:
            print(f"{self.st_name}的选课没有冲突。")


# 示例使用
student = st_lesson("X1X2X3X4X5X6X7")
student.display_schedule()
student.check_conflict()

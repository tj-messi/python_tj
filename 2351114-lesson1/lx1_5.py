#2351114-朱俊泽-大数据科学与技术
'''
中文显示当天年月日和星期几
'''
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()

# 格式化输出当前日期（年月日）
current_date = now.strftime("%Y年%m月%d日")

# 获取当前是星期几（星期一到星期日）
weekday_name_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
weekday_index = now.weekday()  # weekday()函数返回0（星期一）到6（星期日）之间的整数
current_weekday = weekday_name_list[weekday_index]

# 打印结果
print(f"今天是：{current_date}，{current_weekday}")
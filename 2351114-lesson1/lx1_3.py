#2351114-朱俊泽-大数据科学与技术
'''
编写一个randstar()随机星形画线函数，效果如下图所示，要求位置，颜色，半径，笔粗细，线条数都为随机
'''
import turtle
import random

def randstar():
    # 创建屏幕
    screen = turtle.Screen()
    # 设置画笔
    pen = turtle.Turtle()
    pen.speed(5)  # 设置画笔速度
    for i in range (1,random.randint(5,20)):
        # 随机设置星形的颜色
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
        pen.color(random.choice(colors))

        # 随机设置星形的半径和笔粗细
        radius = random.randint(50, 200)
        pen.width(random.randint(1, 10))

        # 随机位置（这里假设屏幕足够大）
        pen.penup()
        pen.goto(random.randint(-300, 300), random.randint(-300, 300))
        pen.pendown()

        #简化星形绘制，这里使用多边形近似（例如六边形作为示例）
        # 注意：这不是真正的星形，但可以用多边形模拟
        num_points = random.randint(5, 20)  # 随机线条数（即多边形边数）
        angle = 360 / num_points

        for _ in range(num_points):
            pen.forward(radius)
            pen.backward(radius)
            pen.right(angle)

            # 结束
        pen.hideturtle()




if __name__ == '__main__':
    # 调用randstar函数
    randstar()
    # 保持窗口打开直到用户关闭
    turtle.done()

#2351114-朱俊泽-大数据科学与技术
'''
通过导入外部库，实现生成一张二维码图片，扫码将打开同济官网
'''
import qrcode
data = "https://www.tongji.edu.cn"
img = qrcode.make(data)
img.save("tju.png")





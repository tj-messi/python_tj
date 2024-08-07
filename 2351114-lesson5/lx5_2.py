# 2351114 朱俊泽 大数据科学与技术
'''
参考https://zhuanlan.zhihu.com/p/25556276
实现将一张照片卡通化

1.自拍一张照片，命名为学号.jpg,最终输出为  学号carton,jpg
2. 原始代码为指定文件夹批量卡通化，修改为仅处理当前文件夹的
一张照片
'''
import cv2
import numpy as np


def apply_cartoon_effect(img_path, output_path):
    img = cv2.imread(img_path)

    # 灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 应用高斯模糊
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.adaptiveThreshold(gray_blurred, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    cartoon = cv2.bitwise_and(edges, edges)
    cv2.imwrite(output_path, cartoon)


if __name__ == '__main__':
    img_path = '2351114.jpg'
    output_path = '2351114carton.jpg'
    apply_cartoon_effect(img_path, output_path)
    print(f"黑白卡通化图像已保存为 {output_path}")

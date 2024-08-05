#2351114 朱俊泽 大数据科学与技术
'''
编写一个tj_web对象
该对象属性：
tj_browser   :selenium.webdriver.Chrome()
First_page: https://www.tongji.edu.cn
wait_time:  等待多少秒，如3秒
该对象方法：
auto_click(txt_list)
依次自动点击txt_list对应的菜单项
将打开的页面截图，文件名为菜单名
将打开的页面保存为txt文件,utf-8编码
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class tj_web:
    def __init__(self, wait_time=3):
        self.tj_browser = webdriver.Chrome()
        self.First_page = 'https://www.tongji.edu.cn'
        self.wait_time = wait_time

    def auto_click(self, txt_list):
        self.tj_browser.get(self.First_page)
        for txt in txt_list:
            try:
                # 等待元素可见并点击
                element = WebDriverWait(self.tj_browser, self.wait_time).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, txt))
                )
                element.click()

                # 等待页面加载
                time.sleep(self.wait_time)

                # 截图
                screenshot_path = f"{txt}.png"
                self.tj_browser.save_screenshot(screenshot_path)

                # 保存页面为txt文件
                page_source = self.tj_browser.page_source
                with open(f"{txt}.txt", 'w', encoding='utf-8') as f:
                    f.write(page_source)
            except Exception as e:
                print(f"Error clicking {txt}: {e}")


# 示例使用
if __name__ == "__main__":
    tj = tj_web(wait_time=3)
    txt_list = ["学校概况", "同济新闻", "教育教学"]
    tj.auto_click(txt_list)
    tj.tj_browser.quit()

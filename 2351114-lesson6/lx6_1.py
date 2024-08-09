#2351114 朱俊泽 大数据科学与技术
"""
设计一个tj_web类
该类有以下属性：
tj_browser      #webdriver.Chrome()
First_page      #字符串值https://news.tongji.edu.cn/info/1003/88134.htm'

该类有以下方法：
auto_replace（） #自动打开first_page对应网页，并将标题里的覃海洋更换为自己的名字
speak_text(text) #自动朗读text
"""
import time
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By

class tj_web:
    def __init__(self):
        self.tj_browser = webdriver.Chrome()
        self.First_page = "https://news.tongji.edu.cn/info/1003/88134.htm"

    def auto_replace(self, new_name):
        # 打开指定网页
        self.tj_browser.get(self.First_page)
        time.sleep(2)
        try:
            elements = self.tj_browser.find_elements(By.XPATH, "//*[contains(text(), '覃海洋')]")
            for element in elements:
                original_text = element.text
                print("Original Text:", original_text)
                updated_text = original_text.replace("覃海洋", new_name)
                self.tj_browser.execute_script(f"arguments[0].innerText = '{updated_text}'", element)
                print("Updated Text:", updated_text)
        except Exception as e:
            print("Error finding or updating text:", e)

    def speak_text(self, text):
        #elements = self.tj_browser.find_elements(By.XPATH, "//*[contains(text(), '覃海洋')]")
        engine = pyttsx3.init()
        engine.say(text)  # 朗读文本
        engine.runAndWait()

    def close(self):
        self.tj_browser.quit()


# 示例使用
if __name__ == "__main__":
    web = tj_web()
    web.auto_replace("朱俊泽")
    web.speak_text("刷新亚洲纪录，同济学子朱俊泽与队友摘得巴黎奥运会男女混合4×100米混合泳接力决赛银牌")  # 朗读文本
    time.sleep(5)
    web.close()


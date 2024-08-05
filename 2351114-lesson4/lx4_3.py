#2351114 朱俊泽 大数据科学与技术
'''
编写一个tj_bbs对象
该对象属性：
bbs_browser   :selenium.webdriver.Chrome()
login_page: http://cyr985.net3v.club/bbs/login.asp
post_page:http://cyr985.net3v.club/bbs/topic.asp?id=4891&boardid=6&TB=1
wait_time:  等待多少秒，如3秒
该对象方法：
auto_login(username,password)   #实现自动登录
Auto_post(bbs_content)          #实现自动回一条贴
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class tj_bbs:
    def __init__(self, wait_time=3):
        self.bbs_browser = webdriver.Chrome()
        self.post_page = 'http://cyr985.net3v.club/bbs/topic.asp?id=4891&boardid=6&TB=1'
        self.wait_time = wait_time

    def auto_login(self, username, password):
        self.bbs_browser.get(self.post_page)
        try:
            # 等待“登录”按钮可见并点击
            login_button = WebDriverWait(self.bbs_browser, self.wait_time).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="登陆"]'))
            )
            login_button.click()
            # 等待用户名和密码输入框可见
            username_input = WebDriverWait(self.bbs_browser, self.wait_time).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//label[contains(text(), "请输入您的用户名")]/following-sibling::input'))
            )
            password_input = self.bbs_browser.find_element(By.XPATH,
                                                           '//label[contains(text(), "请输入您的密码")]/following-sibling::input')

            # 输入用户名和密码
            username_input.send_keys(username)
            password_input.send_keys(password)

            # 等待“登录”按钮可见并点击
            login_button = WebDriverWait(self.bbs_browser, self.wait_time).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="登陆"]'))
            )
            login_button.click()

            # 等待页面加载
            time.sleep(self.wait_time)
        except Exception as e:
            print(f"Error during login: {e}")

    def auto_post(self):
        try:
            # 等待回复框可见
            reply_box = WebDriverWait(self.bbs_browser, self.wait_time).until(
                EC.presence_of_element_located((By.NAME, 'content'))
            )

            # 输入回复内容
            reply_box.send_keys('2351114 zhu jun ze')

            # 点击“ok发表”按钮
            submit_button = self.bbs_browser.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="ok发表"]')
            submit_button.click()

            # 等待页面加载
            time.sleep(self.wait_time)
        except Exception as e:
            print(f"Error during posting: {e}")


# 示例使用
if __name__ == "__main__":
    bbs = tj_bbs(wait_time=3)
    bbs.auto_login('tj_messi', '1398212202')
    bbs.auto_post()
    bbs.bbs_browser.quit()

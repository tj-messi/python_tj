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


class TJ_BBS():
    bbs_browser = webdriver.Chrome()
    login_page = 'http://cyr985.net3v.club/bbs/login.asp'
    post_page = 'http://cyr985.net3v.club/bbs/topic.asp?id=4891&boardid=6&TB=1'
    wait_time = 5

    def auto_login(self, username: str, password: str):
        self.bbs_browser.get(self.login_page)
        time.sleep(self.wait_time)

        name_input = WebDriverWait(self.bbs_browser, self.wait_time).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        password_input = self.bbs_browser.find_element(By.NAME, 'Password')
        name_input.send_keys(username)
        password_input.send_keys(password)
        submit_button = self.bbs_browser.find_element(By.CLASS_NAME, 'login')
        submit_button.click()
        time.sleep(self.wait_time)

    def auto_post(self, bbs_content):
        self.bbs_browser.get(self.post_page)
        time.sleep(self.wait_time)
        reply_bt = self.bbs_browser.find_element(by=By.XPATH, value='//*[@id="edit"]')
        reply_bt.send_keys(bbs_content)
        time.sleep(self.wait_time)
        sub_bt = self.bbs_browser.find_element(by=By.XPATH, value='//*[@id="sayb"]')
        sub_bt.click()
        time.sleep(self.wait_time)
        pass


def main():
    tj = TJ_BBS()
    username = "tj_messi"  # 替换为实际的用户名
    password = "1398212202"  # 替换为实际的密码
    tj.auto_login(username, password)
    tj.auto_post("2351114 zhu jun ze")


if __name__ == "__main__":
    main()


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
import selenium
import time

class tj_web
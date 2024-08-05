from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口

# 设置ChromeDriver路径
chrome_driver_path = '/path/to/chromedriver'  # 请替换为你的ChromeDriver路径
service = Service(chrome_driver_path)

# 初始化WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# 目标URL
url = 'https://music.163.com/#/discover/toplist?id=3778678'  # 网易云音乐热歌榜URL

# 打开目标网页
driver.get(url)

# 切换到iframe
iframe = driver.find_element(By.ID, 'g_iframe')
driver.switch_to.frame(iframe)

# 等待页面加载
time.sleep(5)  # 根据实际情况调整等待时间

# 找到歌曲列表的容器
song_list = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')  # 请根据实际网页结构调整选择器

# 初始化数据列表
datalist = []

# 提取歌曲信息
for song in song_list:
    title = song.find_element(By.CSS_SELECTOR, 'span.txt a b').get_attribute('title').strip()  # 请根据实际网页结构调整选择器
    artist = song.find_element(By.CSS_SELECTOR, 'div.text').get_attribute('title').strip()  # 请根据实际网页结构调整选择器
    datalist.append({'title': title, 'artist': artist})

# 关闭WebDriver
driver.quit()

# 打印输出
for item in datalist:
    print(f"Title: {item['title']}, Artist: {item['artist']}")


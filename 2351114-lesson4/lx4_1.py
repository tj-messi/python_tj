#2351114 朱俊泽 大数据科学与技术
'''
参考https://blog.csdn.net/qq_40243365/article/details/83003450
将100首歌榜爬下存于datalist并print 输出
输出示例：
[[‘1’, ‘童话镇’, ‘容祖儿’], [‘2’, ‘在你身边的日子以小时计算’, ‘李莎旻子’], [‘3’, ‘Wake - (3D高燃版)’, ‘圈圈菌’],。。。。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# 打开浏览器
browser = webdriver.Chrome()
url = 'https://music.163.com/#/discover/toplist'
browser.get(url)

# 寻找logo文字
logo = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'logo'))
)
print(logo.text)

# 切换到iframe
iframe = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'g_iframe'))
)
browser.switch_to.frame(iframe)

# 寻找大容器
toplist = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'toplist'))
)

# 寻找tbody 通过标签名
tbody = toplist.find_elements(By.TAG_NAME, 'tbody')[0]

# 寻找所有tr
trs = tbody.find_elements(By.TAG_NAME, 'tr')

dataList = []
for each in trs:
    # 排名
    rank = each.find_elements(By.TAG_NAME, 'td')[0].find_elements(By.CLASS_NAME, 'num')[0].text
    musicName = each.find_elements(By.TAG_NAME, 'td')[1].find_elements(By.CLASS_NAME, 'txt')[0].\
        find_elements(By.TAG_NAME, 'b')[0].get_attribute('title')
    singer = each.find_elements(By.TAG_NAME, 'td')[3].find_elements(By.CLASS_NAME, 'text')[0].\
        get_attribute('title')
    dataList.append([rank, musicName, singer])

# 关闭浏览器
browser.quit()

# 打印数据
for item in dataList:
    print(f"Rank: {item[0]}, Title: {item[1]}, Artist: {item[2]}")

# 将数据写入Excel文件
wb = Workbook()
ws = wb.active
ws.title = '云音乐飙升榜'
ws.append(['排名', '歌名', '歌手'])
for data in dataList:
    ws.append(data)

wb.save("云音乐飙升榜.xlsx")


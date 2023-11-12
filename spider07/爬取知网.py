"""
案例：爬取知网
适用selenium驱动chromedriver，打开浏览器窗口
采集论文标题、作者、来源、发表日期、摘要
"""
# ① 引入库
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# ② 设置启动chromedirver启动路径,实例化浏览器窗口
service = webdriver.ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.maximize_window()  # 最大化窗口
# ③ 打开网址
browser.get(url='https://www.cnki.net/')
# ④ 输入并点击
browser.find_element(By.ID, 'txt_SearchText').send_keys('王者荣耀')
time.sleep(0.5)
browser.find_element(By.CLASS_NAME, 'search-btn').click()
time.sleep(2)
# ⑤ 提取页面信息
tr_list = browser.find_elements(By.XPATH, '//tbody/tr')
for tr in tr_list:
    title = tr.find_element(By.CLASS_NAME, 'fz14').text  # 论文标题
    authors = tr.find_elements(By.XPATH, 'td[@class="author"]/a')  # 论文作者
    authors = ','.join([author.text for author in authors])
    source = tr.find_element(By.XPATH, 'td[@class="source"]//a').text
    public_date = tr.find_element(By.CLASS_NAME, 'date').text
    print(title, authors, source, public_date)

# 关闭浏览器窗口
time.sleep(5)
browser.close()

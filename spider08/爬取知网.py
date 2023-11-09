"""
案例：知网
使用selenium+chromedriver
爬取知网《关键词》的论文信息：题目、作者、来源、简介，并保存
"""
# ① 引入库(time、selenium)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# ② 设置chromedriver启动路径，打开一个浏览器窗口
service = webdriver.ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.maximize_window()  # 最大化浏览器窗口
# ③ 打开网址(url)
browser.get('https://www.cnki.net/')
time.sleep(1.5)
# ④ 输入关键词  点击搜索
browser.find_element(By.ID, 'txt_SearchText').send_keys('王者荣耀')
time.sleep(0.5)
browser.find_element(By.CLASS_NAME, 'search-btn').click()
time.sleep(3)
# ⑤ 提取页面信息
tr_list = browser.find_elements(By.XPATH, '//tbody/tr')
for tr in tr_list:
    # 提取论文标题
    title = tr.find_element(By.CLASS_NAME, 'fz14').text
    # 提取论文作者
    authors = tr.find_elements(By.XPATH, 'td[@class="author"]/a')  # 回头在写
    authors = ','.join([author.text for author in authors])
    # 提取论文来源
    source = tr.find_element(By.XPATH, 'td[@class="source"]//a').text
    # 提取论文发表日期
    date = tr.find_element(By.XPATH, 'td[@class="date"]').text
    print(title, authors, source, date)
    time.sleep(0.2)
# 关闭浏览器
time.sleep(2)
browser.close()
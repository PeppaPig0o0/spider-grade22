"""
案例:知网
使用selenium驱动浏览器窗口，搜索关键词。
获取论文的标题、作者和简介。
"""
# ① 引入库(selenium库)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# ② 实例化一个浏览器对象/打开一个浏览器窗口
service = webdriver.ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.maximize_window()
# ③ 访问url
browser.get('https://www.cnki.net')
time.sleep(2)
# ④ 在搜索栏输入，并点击搜索
# browser.find_element(by=By.ID, value='txt_SearchText').send_keys('王者荣耀')
browser.find_element(By.ID, 'txt_SearchText').send_keys('英雄联盟')
time.sleep(0.5)
browser.find_element(By.CLASS_NAME, 'search-btn').click()
time.sleep(5)
# ⑤ 提取网页信息
tr_list = browser.find_elements(By.XPATH, '//*[@id="gridTable"]/div/div/table/tbody/tr')
for tr in tr_list:
    title = tr.find_element(By.CLASS_NAME, 'fz14').text  # 论文标题
    a_list = tr.find_elements(By.CLASS_NAME, 'KnowledgeNetLink')
    authors = ','.join([a.text for a in a_list])  # 论文作者
    source = tr.find_element(By.XPATH, '//td[@class="source"]/p/a').text  # 论文来源
    public_date = tr.find_element(By.CLASS_NAME, 'date').text  # 论文发表时间
    # ⑥ 打印结果
    print(title, authors, source, public_date)
time.sleep(5)
# 关闭浏览器窗口
browser.close()




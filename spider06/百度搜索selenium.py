"""
案例：百度搜索
使用selenium驱动chromedriver，打开一个浏览器窗口
访问百度，并搜索一个关键词
"""
# ① 引入库
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# ② 设置chromedriver启动路径，并实例化一个浏览器对象（窗口）
service = webdriver.ChromeService(executable_path='chromedriver11.exe')
browser = webdriver.Chrome(service=service)
# ③ 访问URL
browser.get('https://www.baidu.com/')
time.sleep(2)
# ④ 定位元素，并动作
browser.find_element(By.ID, 'kw').send_keys('python')
time.sleep(0.5)
browser.find_element(By.ID, 'su').click()
time.sleep(5)
# ⑤关闭浏览器窗口
browser.close()

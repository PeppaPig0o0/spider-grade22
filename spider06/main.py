"""

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
service = webdriver.ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.get('https://www.baidu.com/')
time.sleep(2)
browser.find_element(By.ID, 'kw').send_keys('王者荣耀')
time.sleep(0.5)
browser.find_element(By.ID, 'su').click()
time.sleep(5)
browser.close()

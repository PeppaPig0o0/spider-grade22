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
service = webdriver.ChromeService(executable_path='chromedriver.exe')
browser = webdriver.Chrome(service=service)
# ③ 访问URL
browser.get('https://www.baidu.com/')
time.sleep(2)
#
# # ④ 定位元素，并动作
# # 1.根据标签的 id属性 定位元素
# browser.find_element(By.ID, '值')
# # 2.根据标签的 class属性 定位元素
# browser.find_element(By.CLASS_NAME, 'class的值')
# # 3.根据标签的 name属性 定位元素
# browser.find_element(By.NAME, 'name值')
# # 4.根据 标签的名字 定位元素
# browser.find_element(By.TAG_NAME, '标签')
# # 5.根据 Xpath路径 定位元素
# browser.find_element(By.XPATH, 'Xpath路径')
# # 6.根据 CSS选择器 定位元素
# browser.find_element(By.CSS_SELECTOR, 'CSS选择器')
#
# a = browser.find_element(By.ID, '值')
# # 1.输入->input
# a.send_keys('朱雪萍')
# # 2.左键点击
# a.click()
# # 3.取文本内容
# a.text
# # 4.取属性值
# a.get_attribute('属性名')
# a.get_attribute('href')
# a.get_attribute('src')
#
# # 改变浏览器窗口大小
# browser.maximize_window()  # 最大化窗口
# browser.minimize_window()  # 最小化窗口
# browser.fullscreen_window()  # 全屏显示窗口
# # 根据尺寸设置窗口大小
# browser.set_window_size(width=800, height=1000)




browser.find_element(By.ID, 'kw').send_keys('python')
time.sleep(0.5)
browser.find_element(By.ID, 'su').click()
time.sleep(5)

# 窗口滚动
# browser.execute_script('window.scrollTo(左右滚动到, 上下滚动到)')
# 窗口滚动1
# browser.execute_script('window.scrollTo(0, 200)')


# 窗口滚动2
def scroll_to_position(y=0, x=0):
    for i in range(1, 11):
        browser.execute_script(f'window.scrollTo({(x/10)*i}, {(y/10)*i})')
        time.sleep(0.4)


scroll_to_position(3000)

# ⑤关闭浏览器窗口
browser.close()

"""
案例：爬取知网
采集论文标题、作者、来源、发表日期等
用selenium + chromedriver来驱动浏览器采集
"""
# ① 引入库
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse(element):
    """
    # 定义一个函数，解析一条数据
    # 接收一个元素对象(tr)，解析网页并打印
    # 返回：None
    """
    title_a = element.find_element(By.CLASS_NAME, 'fz14')
    title = title_a.text  # 标题
    authors = element.find_elements(By.XPATH, 'td[@class="author"]/a')
    authors = ','.join([author.text for author in authors])  # 作者
    source = element.find_element(By.XPATH, 'td[@class="source"]/p/a').text  # 来源
    public_date = element.find_element(By.CLASS_NAME, 'date').text  # 发表日期
    print(title, authors, source, public_date)


if __name__ == '__main__':
    # ② 设施chromedriver路径，并实例化一个浏览器窗口
    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    # ③ 打开网址url
    browser.get('https://www.cnki.net/')
    # ④ 输入关键词，点击放大镜搜索
    browser.find_element(By.ID, 'txt_SearchText').send_keys('红警')
    time.sleep(0.5)
    browser.find_element(By.CLASS_NAME, 'search-btn').click()
    time.sleep(5)
    # ⑤ 提取页面信息
    tr_list = browser.find_elements(By.XPATH, '//tbody/tr')
    for tr in tr_list:
        parse(tr)

    # 最后：关闭
    time.sleep(5)
    browser.quit()

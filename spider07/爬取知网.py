"""
案例：爬取知网
适用selenium驱动chromedriver，打开浏览器窗口
采集论文标题、作者、来源、发表日期、摘要
"""
# ① 引入库
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from spidersql import Conn


# 定义一个函数,解析一条数据
def parse_one(element):
    a_title = element.find_element(By.CLASS_NAME, 'fz14')  # 论文标题
    title = a_title.text
    authors = element.find_elements(By.XPATH, 'td[@class="author"]/a')  # 论文作者
    authors = ','.join([author.text for author in authors])
    source = element.find_element(By.XPATH, 'td[@class="source"]//a').text
    public_date = element.find_element(By.CLASS_NAME, 'date').text

    # ⑥ 点击标题->打开内容页，并切换窗口/标签页
    a_title.click()
    time.sleep(5)
    browser.switch_to.window(browser.window_handles[1])
    # ⑦ 提取内容页信息
    try:
        abstract = browser.find_element(By.CLASS_NAME, 'abstract-text').text  # 摘要
    except:
        abstract = '无'
    try:
        keywords = browser.find_elements(By.NAME, 'keyword')
        keywords = ','.join([k.text for k in keywords])  # 关键词
    except:
        keywords = '无'

    # ⑨ 打印结果，并保存到Mysql数据库
    print(title, authors, source, public_date, abstract, keywords)
    sql = f'''INSERT INTO zhiwang(title, authors, source, public_date, abstract, keywords) 
    VALUE('{title}', '{authors}', '{source}', '{public_date}', '{abstract}', '{keywords}') 
    '''
    db.cursor.execute(sql)
    db.conn.commit()

    # ⑧ 关闭内容页，切回列表页
    browser.close()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])


if __name__ == '__main__':
    # ② 设置启动chromedirver启动路径,实例化浏览器窗口
    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()  # 最大化窗口
    db = Conn()
    # ③ 打开网址
    browser.get(url='https://www.cnki.net/')
    # ④ 搜索：输入并点击
    browser.find_element(By.ID, 'txt_SearchText').send_keys('王者荣耀')
    time.sleep(0.5)
    browser.find_element(By.CLASS_NAME, 'search-btn').click()
    time.sleep(2)

    while True:
        time.sleep(5)
        # ⑤ 提取一页的页面信息
        tr_list = browser.find_elements(By.XPATH, '//tbody/tr')
        # 提取一条信息
        [parse_one(tr) for tr in tr_list]

        # 点击下一页
        try:
            browser.find_element(By.ID, 'PageNext').click()
        except exceptions.NoSuchElementException:
            break

    # 关闭浏览器窗口
    time.sleep(5)
    browser.close()

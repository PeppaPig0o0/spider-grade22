"""
案例：知网
使用selenium+chromedriver
爬取知网《关键词》的论文信息：题目、作者、来源、简介，并保存
"""
# ① 引入库(time、selenium)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from conn import Conn


# 定义一个函数,解析一条数据
def parse_one(element):
    # 提取论文标题
    a_title = element.find_element(By.CLASS_NAME, 'fz14')
    title = a_title.text
    # 提取论文作者
    authors = element.find_elements(By.XPATH, 'td[@class="author"]/a')  # 回头在写
    authors = ','.join([author.text for author in authors])
    # 提取论文来源
    source = element.find_element(By.XPATH, 'td[@class="source"]//a').text
    # 提取论文发表日期
    date = element.find_element(By.XPATH, 'td[@class="date"]').text
    # ⑥ 点击标题,切换新标签页
    a_title.click()
    time.sleep(5)
    browser.switch_to.window(browser.window_handles[1])
    # ⑦ 提取内容页中的摘要和关键词
    try:
        abstract = browser.find_element(By.CLASS_NAME, 'abstract-text').text
    except exceptions.NoSuchElementException:
        abstract = '无'
    try:
        keys = browser.find_elements(By.NAME, 'keyword')
        keys = ','.join([k.text for k in keys])
    except exceptions.NoSuchElementException:
        keys = '无'
    # ⑩ 存储到数据库zhiwang表中
    sql = f'''INSERT INTO 
        zhiwang(title, authors, source, public_date, abstract, keywords) 
        VALUES('{title}', '{authors}', '{source}', '{date}', '{abstract}', '{keys}')'''
    db.cursor.execute(sql)
    db.conn.commit()
    print('已保存', title, authors)
    # ⑧ 关闭内容页，并切换回原窗口
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)


if __name__ == '__main__':
    # ② 设置chromedriver启动路径，打开一个浏览器窗口
    service = webdriver.ChromeService(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()  # 最大化浏览器窗口
    # ③ 打开网址(url)
    browser.get('https://www.cnki.net/')
    time.sleep(1.5)
    db = Conn()  # 开启数据库链接
    # ④ 输入关键词  点击搜索
    browser.find_element(By.ID, 'txt_SearchText').send_keys('王者荣耀')
    time.sleep(0.5)
    browser.find_element(By.CLASS_NAME, 'search-btn').click()

    # ⑤ 提取页面信息
    while True:
        time.sleep(5)
        tr_list = browser.find_elements(By.XPATH, '//tbody/tr')
        for tr in tr_list:
            parse_one(tr)  # 解析一条数据

        # ⑨ 点击当前页后面那一页
        try:
            browser.find_element(By.ID, 'PageNext').click()
        except exceptions.NoSuchElementException:
            break
    # 关闭浏览器
    time.sleep(2)
    browser.close()
    print('采集完成')

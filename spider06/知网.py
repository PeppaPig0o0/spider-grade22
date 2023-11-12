"""
案例:知网
使用selenium驱动浏览器窗口，搜索关键词。
获取论文的标题、作者和简介。
"""
# ① 引入库(selenium库)
import time
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定义一个函数（提取一条信息:标题、作者、摘要、关键词等等）
def parse_one(element):
    a_title = element.find_element(By.CLASS_NAME, 'fz14')  # 论文标题
    title = a_title.text
    a_list = element.find_elements(By.CLASS_NAME, 'KnowledgeNetLink')
    authors = ','.join([a.text for a in a_list])  # 论文作者
    source = element.find_element(By.XPATH, '//td[@class="source"]/p/a').text  # 论文来源
    public_date = element.find_element(By.CLASS_NAME, 'date').text  # 论文发表时间
    # ⑥ 点击并切换到新标签页
    a_title.click()
    time.sleep(0.5)
    browser.switch_to.window(browser.window_handles[1])
    # ⑦ 提取内容页的信息
    time.sleep(5)
    abstract = browser.find_element(By.CLASS_NAME, 'abstract-text').text  # 摘要/正文快照
    keywords = browser.find_elements(By.NAME, 'keyword')
    keywords = ','.join([k.text for k in keywords])  # 关键词
    #  ⑧ 打印结果
    print(title, authors, source, public_date)
    print(abstract, keywords)
    browser.close()  # 关闭标签页
    # ⑨ 切换回原标签页
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)


if __name__ == '__main__':
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
    for i in range(1, 22):
        tr_list = browser.find_elements(By.XPATH, '//*[@id="gridTable"]/div/div/table/tbody/tr')
        for tr in tr_list[-1:]:
            parse_one(tr)  # 提取一条论文数据
        # 每页采集完成后，点击当前页面+1的按钮（a标签）
        try:
            browser.find_element(By.XPATH, f'//a[@data-curpage="{i+1}"]').click()
        except exceptions.NoSuchElementException:
            print('采集完成')
            break
        time.sleep(5)

    # 关闭浏览器窗口
    time.sleep(5)
    browser.close()




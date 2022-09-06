import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url_login = 'https://login.taobao.com/member/login.jhtml'

# 实例化浏览器选项：
option = webdriver.ChromeOptions()

# 添加选项配置：  # 但是用程序打开的网页的window.navigator.webdriver仍然是true。
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("detach", True)

# 去掉window.navigator.webdriver的特性
option.add_argument("disable-blink-features=AutomationControlled")

# 设置为无头浏览器：不会显示出操作浏览器的过程
#option.add_argument('--headless')


# 实例化浏览器对象
driver = webdriver.Chrome(options=option)

driver.get(url_login)

#登录
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="fm-login-id"]').send_keys('')#淘宝账号
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="fm-login-password"]').send_keys('')#淘宝密码
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[4]/button').click()
time.sleep(15)

#搜索商品
driver.find_element(By.XPATH, '//*[@id="q"]').send_keys('苹果13官方')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button').click()
time.sleep(1)

b = []
c = []
d = []

def get_price():
    prices = driver.find_elements(By.XPATH,'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]')
    for price in prices:
        x = price.find_element(By.XPATH, './/strong').text
        b.append(x)

def get_title():
    titles = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/div[2]/div[2]')
    for title in titles:
        x = title.find_element(By.XPATH, './/a').text
        c.append(x)

def get_location():
    locations = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/div[2]/div[3]')
    for location in locations:
        x = location.find_element(By.XPATH, './/div[2]').text
        d.append(x)


for i in range(10):  # 选择要爬取的页数
    get_price()
    time.sleep(5)
    get_title()
    time.sleep(2)
    get_location()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/ul/li[last()]/a/span[1]').click() #下一页
    time.sleep(5)


c={"price" : b,
   "title" : c,
   "location" : d}
data=pd.DataFrame(c)
data.to_csv('商品搜索结果.csv')

driver.quit()










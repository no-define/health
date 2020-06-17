import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 静默模式
chrome_options.add_argument('--window-size=1280x800')


config = configparser.RawConfigParser()
config.read('config.ini', encoding='UTF-8')


def login():
    # 登录
    driver.get('http://authserver.jit.edu.cn/authserver/login')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys(config['login']['username'])
    time.sleep(2)
    driver.find_element_by_id('password').send_keys(config['login']['password'])
    time.sleep(2)
    driver.find_element_by_css_selector("#login_form1 > div.form_list_button > input").click()
    time.sleep(3)
    wait = WebDriverWait(driver, 10)


def add_record():
    global driver
    driver.get('http://ehallapp.jit.edu.cn/emapflow/sys/lwReportEpidemic/index.do?amp_sec_version_=1#/newdailyReport')
    time.sleep(2)
    driver.refresh()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/article/section/div[2]/div[1]'))
        )

        # 新增
        driver.find_element_by_css_selector(
            'body > main > article > section > div.bh-mb-16 > div.bh-btn.bh-btn-primary').click()
        time.sleep(6)

        # 是否异常
        driver.find_element_by_xpath(
            '/html/body/div[11]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[17]/div/div/div/div[2]/div/div[3]').click()
        time.sleep(2)

        # 健康码颜色
        driver.find_element_by_xpath(
            '/html/body/div[11]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[5]/div/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[20]/div/div/div/div[2]/div/div[2]').click()
        time.sleep(2)

        # 14天是否去过南京以外
        driver.find_element_by_xpath(
            '/html/body/div[11]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[6]/div/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[2]/div/div[3]').click()
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/footer/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[28]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
    finally:
        driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome(options=chrome_options)
    login()
    add_record()

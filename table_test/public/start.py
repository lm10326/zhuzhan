#coding=utf-8
from selenium import webdriver
import time
'''配置浏览器和url'''
def choose(browser): #选择浏览器
    if browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='ie':
        driver=webdriver.Ie()
    elif browser=='chrome':
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Opera()
    return driver

def start(driver,url='http://192.168.150.70:8088/Eeeweb/'): #启动浏览器
    driver.get(url)
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("drhnyczzgood123")
    driver.find_element_by_class_name("emailCode").send_keys("1")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/dl/dd[4]/input").click()
    time.sleep(2)

if __name__ == '__main__':
    driver=choose('firefox')
    start(driver)
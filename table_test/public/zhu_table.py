#coding=utf-8
import time
import re
from windlight.table_test.public.get_heng import get_heng
def get_table(driver,xpath_page,xpath_table,n,m): #传参driver，共x页的xpath，table第一格的xpath,n为取多少条数据，m为表格一页有多少条数据
    time.sleep(2)
    # pagetext = driver.find_element_by_xpath('//*[@id="day"]/div/div[2]/div[4]/ul/li[2]/span').text
    pagetext = driver.find_element_by_xpath(xpath_page).text
    pagere = r"\d+"
    pageall = int(re.findall(pagere, pagetext)[0])
    list_heng = []
    num=(n//m)
    if pageall >=num+1:
        # print(pageall)
        for i in range(num):
            # print(i + 1)
            try:
                # list_heng.extend(get_heng(driver, '//*[@id="day"]/div/div[2]/div[3]/table/tbody/tr'))
                list_heng.extend(get_heng(driver, xpath_table))
            except Exception as e:
                print(e)
            driver.find_element_by_partial_link_text("下一页").click()
            time.sleep(2)
            # print(list_heng)
    else:
        print(pageall)
        for i in range(pageall):
            print(i + 1)
            try:
                list_heng.extend(get_heng(driver, xpath_table))
                # list_heng.extend(get_heng(driver, '//*[@id="day"]/div/div[2]/div[3]/table/tbody/tr'))
            except Exception as e:
                print(e)
            driver.find_element_by_partial_link_text("下一页").click()
            time.sleep(2)
            # print(list_heng)
    return list_heng
    # list_wen_yuan = get_col(list_heng, 4).copy()
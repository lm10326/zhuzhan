from selenium import webdriver
from windlight.table_test.public.start import start,choose
import time
from windlight.table_test.public.zhu_table import get_table
from windlight.table_test.public.get_col import del_list_n,deltup,rep_list_last_n,rep_list_rep,set_float
from windlight.table_test.public.get_mysql import get_mysql_h
from windlight.table_test.public.set_date import set_date
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_zonghe(self):
        driver = self.driver
        driver.maximize_window()
        start(driver, 'http://192.168.150.70:8088/Eeeweb/')
        time.sleep(3)
        driver.get("http://192.168.150.70:8088/Eeeweb/E3/index.html#/jdgf_scgl_znyc_qxgl")  # 综合曲线管理
        time.sleep(2)
        driver.find_element_by_id('area').clear()
        driver.find_element_by_id('area').send_keys('山东地区')
        driver.find_element_by_id('FarmId').clear()
        driver.find_element_by_id('FarmId').send_keys('（华润电力）威海东兴风电场')
        set_date(driver, '2017-09-01', '2017-09-30')
        driver.find_element_by_id('findBtn').click()
        time.sleep(3)
        list_heng=get_table(driver,'//*[@id="home"]/div/div[2]/div[4]/ul/li[2]/span','//*[@id="home"]/div/div[2]/div[3]/table/tbody/tr',100,20) #获取100条数据，每页20条数据
        list_web_first = del_list_n(list_heng, 1)  # 去除序号
        list_web=deltup(list_web_first,'')
        print("页面查询结果为:", list_web)

        sql="SELECT ia.time, ia.group_id, ia.power_real, ia.power_forecast_m, ia.masta_speed_C001 , ia.speed_forecast, ia.speed_70_00, ia.speed_70_05, ia.speed_70_06 FROM ia_nwp_fp_rp_cft ia, dr_cmt_farminfo farm WHERE 1 = 1 AND farm.farmorcordid = ia.farm_id AND ia.time >= '2017-09-01' AND ia.time <= '2017-09-30' AND ia.farm_id = 'EEE1001' LIMIT 0,100"
        list_sql_yuejun = get_mysql_h('192.168.150.92', sql, 2)  # 获取数据，保留4位有效小数
        list_set_nine_web = rep_list_rep(list_sql_yuejun, -99, '--', 1)  # 将-99的转成与页面一致的--
        print("sql查询出的结果为", list_set_nine_web)
        print("转换后的页面数据：",set_float(list_web, 1))
        print("转换的数据库数据：",set_float(list_set_nine_web, 1))
        self.assertEqual(set_float(list_web,1), set_float(list_set_nine_web,1))

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

from selenium import webdriver
from windlight.table_test.public.start import start,choose
import time
from windlight.table_test.public.zhu_table import get_table
from windlight.table_test.public.get_col import del_list_n,get_col_t,rep_list_last_n,rep_list_rep,rep_list_n,set_str,set_float
from windlight.table_test.public.get_mysql import get_mysql_h
from windlight.table_test.public.set_date import set_date
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_rijun(self):
        driver = self.driver
        driver.maximize_window()
        start(driver, 'http://192.168.150.70:8088/Eeeweb/')
        time.sleep(3)
        driver.get("http://192.168.150.70:8088/Eeeweb/E3/index.html#/jdgf_scgl_znyc_ycpc")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="myTab"]/li[2]/a').click()
        driver.find_element_by_id("FarmId").send_keys("（华润电力）威海东兴风电场")
        set_date(driver,"2017-06-01","2017-06-30")
        driver.find_element_by_id("findBtn").click()
        list_web=get_table(driver,'//*[@id="day"]/div/div[2]/div[4]/ul/li[2]/span','//*[@id="day"]/div/div[2]/div[3]/table/tbody/tr',100,20)
        # print(list_heng)
        print("页面查询结果为:", list_web)


        sql="SELECT data_date , IF(mse_accuracy_rate_m >= 0, FORMAT(mse_accuracy_rate_m * 100, 2), -99) AS mseAccuracyRateM , IF(mse_accuracy_rate_a3_00 >= 0, FORMAT(mse_accuracy_rate_a3_00 * 100, 2), -99) AS mseAccuracyRateA3DM , IF(mse_accuracy_rate_a3_05 >= 0, FORMAT(mse_accuracy_rate_a3_05 * 100, 2), -99) AS mseAccuracyRateA3NXBY , IF(mse_accuracy_rate_a3_06 >= 0, FORMAT(mse_accuracy_rate_a3_06 * 100, 2), -99) AS mseAccuracyRateA3DR , IF(mse_accuracy_rate_a3_e1 >= 0, FORMAT(mse_accuracy_rate_a3_e1 * 100, 2), -99) AS mseAccuracyRateA3E1 , IF(mse_accuracy_rate_a3_e2 >= 0, FORMAT(mse_accuracy_rate_a3_e2 * 100, 2), -99) AS mseAccuracyRateA3E2 , IF(mse_accuracy_rate_m_00 >= 0, FORMAT(mse_accuracy_rate_m_00 * 100, 2), -99) AS mseAccuracyRateMDM , IF(mse_accuracy_rate_m_05 >= 0, FORMAT(mse_accuracy_rate_m_05 * 100, 2), -99) AS mseAccuracyRateMNXBY , IF(mse_accuracy_rate_m_06 >= 0, FORMAT(mse_accuracy_rate_m_06 * 100, 2), -99) AS mseAccuracyRateMDR , IF(mse_accuracy_rate_m_e1 >= 0, FORMAT(mse_accuracy_rate_m_e1 * 100, 2), -99) AS mseAccuracyRateME1 , IF(mse_accuracy_rate_m_e2 >= 0, FORMAT(mse_accuracy_rate_m_e2 * 100, 2), -99) AS mseAccuracyRateME2 , IF(mse_accuracy_rate_05 >= 0, FORMAT(mse_accuracy_rate_05 * 100, 2), -99) AS mseAccuracyRateXBY , IF(mse_accuracy_rate_nowcast_1 >= 0, FORMAT(mse_accuracy_rate_nowcast_1 * 100, 2), -99) AS mseAccuracyRateN1 , IF(mse_accuracy_rate_nowcast_16 >= 0, FORMAT(mse_accuracy_rate_nowcast_16 * 100, 2), -99) AS mseAccuracyRateN16 FROM ia_forecast_deviation_analysis a INNER JOIN dr_cmt_farminfo b ON a.farm_id = b.farmorcordid WHERE 1 = 1 AND a.farm_id = 'EEE1001' AND data_date >= '2017-06-01' AND data_date <= '2017-06-30' AND SUBSTR(data_date, 1, 7) = ( SELECT SUBSTR(data_date, 1, 7) FROM ia_forecast_deviation_analysis WHERE farm_id = 'EEE1001' GROUP BY farm_id, SUBSTR(data_date, 1, 7) ORDER BY farm_id, SUBSTR(data_date, 1, 7) DESC LIMIT 1 ) ORDER BY a.data_date LIMIT 0,100"
        list_sql_yuejun = get_mysql_h('192.168.150.92', sql, 4)  # 获取数据，保留4位有效小数
        list_set_nine_web = rep_list_rep(list_sql_yuejun, '-99', '--', 1)  # 将-99的转成与页面一致的--
        print("sql查询出的结果为",list_set_nine_web)
        print("转换后的页面数据：",set_float(list_web,1))
        print("转换的数据库数据：",set_float(list_set_nine_web,1))
        self.assertEqual(set_float(list_web,1),set_float(list_set_nine_web,1))
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
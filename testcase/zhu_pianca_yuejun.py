from selenium import webdriver
from windlight.table_test.public.start import start,choose
import time
from windlight.table_test.public.zhu_table import get_table
from windlight.table_test.public.get_col import del_list_n,rep_list_last_n,rep_list_rep,rep_list_n,set_str,set_float
from windlight.table_test.public.get_mysql import get_mysql_h
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_yuejun(self):
        driver = self.driver
        driver.maximize_window()
        start(driver, 'http://192.168.150.70:8088/Eeeweb/')
        time.sleep(3)
        driver.get("http://192.168.150.70:8088/Eeeweb/E3/index.html#/jdgf_scgl_znyc_ycpc")
        time.sleep(3)
        driver.find_element_by_id("area").send_keys("山东地区")
        driver.find_element_by_id("findBtn").click()
        list_heng=get_table(driver,'//*[@id="month"]/div/div[5]/ul/li[2]/span','//*[@id="month"]/div/div[2]/table/tbody/tr',100,20) #获取100条数据，每页20条数据
        list_web=del_list_n(list_heng,1) #去除序号
        print("页面查询结果为:",list_web)

        sql="SELECT IF(ISNULL(( SELECT kname FROM dr_cmt_farminfo WHERE kid = b.pid AND ktype = '1' ))," \
            " '无', ( SELECT kname FROM dr_cmt_farminfo WHERE kid = b.pid AND ktype = '1' )) " \
            "AS province , farm_id, farm_name, project_type , IF(ISNULL(( SELECT deptname FROM tf_rbac_department WHERE deptid = b.fromcompany ))," \
            " '无', ( SELECT deptname FROM tf_rbac_department WHERE deptid = b.fromcompany )) AS owned_company , send_abnormal_days ," \
            " IF(mse_accuracy_rate_m >= 0, FORMAT(mse_accuracy_rate_m * 100, 2), -99) AS mse_accuracy_rate_m , IF(mse_accuracy_rate_nowcast_1 >= 0, " \
            "FORMAT(mse_accuracy_rate_nowcast_1 * 100, 2), -99) AS mse_accuracy_rate_nowcast_1 , IF(mse_accuracy_rate_nowcast_16 >= 0, FORMAT" \
            "(mse_accuracy_rate_nowcast_16 * 100, 2), -99) AS mse_accuracy_rate_nowcast_16 , IF(mse_accuracy_rate_a3_00 >= 0, FORMAT(mse_accuracy_rate_a3_00 * 100, 2), -99) " \
            "AS mse_accuracy_rate_a3_00 , IF(mse_accuracy_rate_a3_05 >= 0, FORMAT(mse_accuracy_rate_a3_05 * 100, 2), -99) AS mse_accuracy_rate_a3_05 ," \
            " IF(mse_accuracy_rate_a3_06 >= 0, FORMAT(mse_accuracy_rate_a3_06 * 100, 2), -99) AS mse_accuracy_rate_a3_06 , IF(mse_accuracy_rate_a3_e1 >= 0, " \
            "FORMAT(mse_accuracy_rate_a3_e1 * 100, 2), -99) AS mse_accuracy_rate_a3_e1 , IF(mse_accuracy_rate_a3_e2 >= 0, FORMAT(mse_accuracy_rate_a3_e2 * 100, 2), -99) " \
            "AS mse_accuracy_rate_a3_e2 , IF(mse_accuracy_rate_m_00 >= 0, FORMAT(mse_accuracy_rate_m_00 * 100, 2), -99) AS mse_accuracy_rate_m_00 , IF(mse_accuracy_rate_m_05 >= 0, " \
            "FORMAT(mse_accuracy_rate_m_05 * 100, 2), -99) AS mse_accuracy_rate_m_05 , IF(mse_accuracy_rate_m_06 >= 0, FORMAT(mse_accuracy_rate_m_06 * 100, 2), -99) " \
            "AS mse_accuracy_rate_m_06 , IF(mse_accuracy_rate_m_e1 >= 0, FORMAT(mse_accuracy_rate_m_e1 * 100, 2), -99) AS mse_accuracy_rate_m_e1 , IF(mse_accuracy_rate_m_e2 >= 0, " \
            "FORMAT(mse_accuracy_rate_m_e2 * 100, 2), -99) AS mse_accuracy_rate_m_e2 , IF(mse_accuracy_rate_05 >= 0, FORMAT(mse_accuracy_rate_05 * 100, 2), -99) AS mse_accuracy_rate_05 ," \
            " mse_assessment_score, mse_assessment_price, mse_assessment_memo FROM ia_forecast_deviation_analysis_month a INNER JOIN dr_cmt_farminfo b ON a.farm_id = b.farmorcordid WHERE 1 " \
            "= 1 AND province_key = 'SHANDONG' AND data_month = '2017-11' ORDER BY data_month, farm_id LIMIT 0,100"

        list_sql_yuejun=get_mysql_h('192.168.150.92',sql,4) #获取数据，保留4位有效小数
        list_set_nine_web = rep_list_rep(list_sql_yuejun, '-99', '--', 1) #将-99的转成与页面一致的--
        list_zong_none = rep_list_last_n(list_set_nine_web, 3, '--')# 将后三行空格转成--
        list_zong_feng = rep_list_n(list_zong_none, 4, "风测") #将第4列转成风测
        # print(list_zong_feng)
        print("sql查询出的结果为",list_zong_feng)
        print("转换后的页面数据：",set_float(list_web,1))
        print("转换的数据库数据：",set_float(list_zong_feng,1))
        self.assertEqual(set_float(list_web,1),set_float(list_zong_feng,1))
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
from selenium import webdriver
from windlight.table_test.public.start import start,choose
import time
from selenium.webdriver.support.ui import Select
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('chrome')
    def test_add(self):
        '''添加场站'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.150.70:8088/Eeeweb/')
        time.sleep(3)
        nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        driver.get("http://192.168.150.70:8088/Eeeweb/E3/index.html#/jdgf_dlhzm_sjzc_czgl")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="browser"]/li[1]/span/span').click()
        time.sleep(2)
        # time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/div[1]/div[1]/div/button[2]").click()
        time.sleep(2)
        kname="test"+nowtime
        farm_code="EEE"+nowtime
        driver.find_element_by_id("kname").send_keys(kname)  #场站名称
        Select(driver.find_element_by_id("province")).select_by_visible_text("辽宁省") #所属区域-省
        Select(driver.find_element_by_id("city")).select_by_visible_text("沈阳市") #所属区域-市
        Select(driver.find_element_by_id("rtype")).select_by_visible_text("风电") #场站类型
        driver.find_element_by_id("farmorcordid").send_keys(farm_code) #场站编号
        Select(driver.find_element_by_id("projectFrom")).select_by_visible_text("东润本部") #项目来源
        driver.find_element_by_id("danweis").send_keys("上海风力")
        # time.sleep(3)
        driver.find_element_by_xpath('//*[@id="Companys"]/li').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="input_dan"]/div[2]/ul/li/span/ul/li/span/span').click()# 所属公司
        driver.find_element_by_id("commissioningTime").send_keys("2017-12-23") #建模日期
        driver.find_element_by_xpath('//*[@id="addModal"]/div/div/div[2]/form/div[7]/label').click() #收起日历
        driver.find_element_by_id("realInstallCapacity").send_keys("23") #装机容量
        driver.find_element_by_id("longitude").send_keys("E101") #经度
        driver.find_element_by_id("latitude").send_keys("N23") #纬度
        driver.find_element_by_id("fan_number").send_keys("35") #风机/逆变器
        driver.find_element_by_id("atten").send_keys("联系人") #联系人
        driver.find_element_by_id("email").send_keys("11111@qq.com") #邮箱
        driver.find_element_by_id("telephone").send_keys("13556987412")#电话
        driver.find_element_by_xpath("//*[@id='addModal']/div/div/div[3]/button[2]").click() #提交
        time.sleep(2)
        # aa=driver.find_element_by_xpath('//*[@id="successModal"]/div/div/div[2]/p').text
        aa = driver.find_element_by_xpath('//p[@ng-bind="successMsg"]').text
        print(aa)
        self.assertEqual(aa,"提交成功！")
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

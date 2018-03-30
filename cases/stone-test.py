import os
import unittest
from appium import webdriver
import time
from selenium.webdriver.common.by import By


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ShiTouJinRong(unittest.TestCase):
    def setUp(self):
        # 定义启动设备需要的参数
        desired_caps = {}
        # 设备系统
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '5.1.1'
        # 设备名称
        desired_caps['deviceName'] = 'MX4_Pro'
        # 要测试的应用的地址
        # desired_caps['app'] = '<span style="color:#ff0000;background-color:rgb(255,0,0);">C:\\Users\\zl\\Desktop\\需求新增\\3月\\app-release-预生产.apk</span>'
        # 应用的包名
        desired_caps['appPackage'] = 'com.invstone.android'
        desired_caps['appActivity'] = '.AppStartActivity'
        # 使得支持Unicode字符(输入中文)
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        # 启动app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        wang = self.driver
        wang.implicitly_wait(60)

    # def tearDown(self):
    #     self.driver.quit()

    print("\n-----start test-----\n")

    def test_banner_swipe(self):
        for i in range(4):
            print(i)
            ad = self.driver.find_element_by_id('adgallery')
            ad.click()
            time.sleep(10)
            wv = self.driver.find_element_by_class_name('android.webkit.WebView').get_attribute('element')
            print(wv)
            en = wv.get_attribute('enabled')
            print('页面是否加载完成：',en)
            back = self.driver.find_element_by_id('iv_nav_back')
            back.click()
            self.driver.swipe(1500, 300, 50, 300)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShiTouJinRong)
    unittest.TextTestRunner(verbosity=2).run(suite)



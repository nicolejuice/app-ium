import os
import unittest
from appium import webdriver
import time
from selenium.webdriver.common.by import By


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ShiTouJinRongLogin(unittest.TestCase):
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
        desired_caps['appPackage'] = 'com.meizu.notepaper'
        desired_caps['appActivity'] = 'com.meizu.flyme.notepaper.app.NotePaperActivity'
        # 使得支持Unicode字符(输入中文)
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        # 启动app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        wang = self.driver
        wang.implicitly_wait(60)

    # def tearDown(self):
    #     self.driver.quit()


    def test_add_notes(self):
        print("-----start test-----")

        # 调用find_elements_by_XX, 返回的是一个list
        el = self.driver.find_element_by_class_name('android.widget.ImageView')
        el.click()
        time.sleep(3)

        textfield = self.driver.find_element_by_class_name('android.widget.EditText')
        t = time.strftime(r'%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        textfield.send_keys('测试记事本,time:',t)
        time.sleep(3)
        print(textfield.text)


        back = self.driver.find_element_by_id('mz_toolbar_nav_button')
        back.click()
        time.sleep(3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShiTouJinRongLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)



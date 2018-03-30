import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd(ChangeWorkingDirectory)#获取当前运行脚本的绝对路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):                             #setup主要实现测试前的初始化工作，而teardown则主要实现测试完成后的垃圾回收等工作
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'MX4_Pro'

        # 应用的包名, 在参数中如果添加了应用的安装路径，就可以不用写包名和启动的activity参数
        # desired_caps['app'] = PATH(
        #     'C:\\Users\zl\Desktop\ContactManager.apk'
        # )

        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'
        # 使得支持Unicode字符(输入中文)
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        el = self.driver.find_element_by_id("addContactButton")
        el.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("测试")
        textfields[1].send_keys("1888888888")
        textfields[2].send_keys("someone@appium.io")

        # 校验输入值
        self.assertEqual('测试', textfields[0].text)
        self.assertEqual('someone@appium.io', textfields[2].text)

        self.driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
        # 切换到alert弹窗
        alert = self.driver.switch_to.alert

        # no way to handle alerts in Android
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        self.driver.press_keycode(3)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
import os
import unittest
from appium import webdriver

class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Google Pixel XL'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'D:appdebug.apk'))
        desired_caps['appPackage'] = 'com.fatbit.yokartv9.buyer'
        desired_caps['appActivity'] = '.activity.SplashActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_ClickRefreshLink(self):
        loginButton = self.driver.find_element_by_class_name("android.widget.TextView")
        self.assertTrue(loginButton.is_displayed())
        loginButton.click()
        ## Right now we are just verify the displayed message on the Phone
        ## You can right code to handle that toast message and Verify that message

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)
__author__ = 'Yogesh Kumar'

import os
import unittest
from appLaunch import ContactAppTestAppium
from time import sleep
from appium import webdriver
from src.PageObject.Pages.HomeScreen import Home
from src.PageObject.Pages.SignInScreen import SignIn
from Tests.Config.settings import remote_driver_url, desired_caps

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(remote_driver_url, desired_caps)

    def test_login(self):
        driver = self.driver

        click_Signin = Home(driver)
        if click_Signin.getlogin().is_displayed():
            click_Signin.getlogin().click()
            sleep(2)

        enter_Username = SignIn(driver)
        enter_Username.setUserName("apptest09@dummyid.com")
        sleep(1)

        enter_Password = SignIn(driver)
        enter_Password.setPassword("Test@123")
        sleep(1)

        click_Signin_Button = SignIn(driver)
        click_Signin_Button.clickSignIn()
        sleep(20)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suite)
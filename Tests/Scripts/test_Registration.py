from Tests.Config.settings import remote_driver_url, desired_caps

__author__ = 'Yogesh Kumar'

import os
import unittest
from appLaunch import ContactAppTestAppium
from time import sleep
from appium import webdriver
from src.PageObject.Pages.HomeScreen import Home
from src.PageObject.Pages.CreateAccountScreen import CreateAccount

class Registration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(remote_driver_url, desired_caps)

    def test_signup(self):
        driver = self.driver

        click_Signup = Home(driver)
        if click_Signup.getsignup().is_displayed():
            click_Signup.getsignup().click()
            sleep(2)

        register_Buyer = CreateAccount(driver)
        register_Buyer.setName("test")
        register_Buyer.setUserName("apptest09")
        register_Buyer.setEmail("apptest09@dummyid.com")
        register_Buyer.setPassword("Test@123")
        register_Buyer.setConfirmPasswrod("Test@123")

        if register_Buyer.getAgree().is_displayed():
            register_Buyer.getAgree().click()

        if register_Buyer.getSignup().is_displayed():
            register_Buyer.getSignup().click()
            sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)
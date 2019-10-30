from src.PageObject.Pages.LoggedinHomeScreen import Loggedin_Home

__author__ = 'Yogesh Kumar'

import os
import unittest
from appLaunch import ContactAppTestAppium
from time import sleep
from appium import webdriver
from src.PageObject.Pages.HomeScreen import Home
from src.PageObject.Pages.SignInScreen import SignIn
from Tests.Config.settings import remote_driver_url, desired_caps

class OrderPlacement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(remote_driver_url, desired_caps)

    def test_orderplacement(self):
        driver = self.driver
        sleep(5)
        click_Signin = Home(driver)
        if click_Signin.getlogin().is_displayed():
            click_Signin.getlogin().click()
            sleep(2)

        enter_Username = SignIn(driver)
        enter_Username.setUserName("apptest09@dummyid.com")

        enter_Password = SignIn(driver)
        enter_Password.setPassword("Test@123")

        click_Signin_Button = SignIn(driver)
        click_Signin_Button.clickSignIn()
        sleep(20)

        #Logged_Buyer = Loggedin_Home(driver)
        #Logged_Buyer.clickMenu()
        #sleep(2)
        #Logged_Buyer.clickNotification()
        #sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)
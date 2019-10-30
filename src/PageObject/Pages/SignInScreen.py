__author__ = 'Yogesh Kumar'

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class SignIn(object):

    def __init__(self, driver):
        self.driver = driver

# SignIn page locators defining
        self.username = driver.find_element(By.ID, Locator.signin_Username)
        self.password = driver.find_element(By.ID, Locator.signin_Password)
        self.signinButton = driver.find_element(By.ID, Locator.signin_Signin_Button)

# you can return WebElement from method and call it, and useful method with parameter define here
    def setUserName(self, Name):
        self.username.clear()
        self.username.send_keys(Name)

    def setPassword(self, Password):
        self.password.clear()
        self.password.send_keys(Password)

    def clickSignIn(self):
        self.signinButton.click()
__author__ = 'Yogesh Kumar'

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class Home(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.login = driver.find_element(By.CLASS_NAME, Locator.login_Homescreen)
        self.signup = driver.find_element(By.XPATH, Locator.signup_Homescreen)

# you can return WebElement from method and call it, and useful method with parameter define here
    def getlogin(self):
        return self.login

    def getsignup(self):
        return self.signup
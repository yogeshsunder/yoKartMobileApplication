__author__ = 'Yogesh Kumar'

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class CreateAccount(object):

    def __init__(self, driver):
        self.driver = driver

#Create an Account screen locators defining
        self.name = driver.find_element(By.ID, Locator.register_Name)
        self.username = driver.find_element(By.ID, Locator.register_UserName)
        self.email = driver.find_element(By.ID, Locator.register_Email)
        self.password = driver.find_element(By.ID, Locator.register_Password)
        self.confirmPassword = driver.find_element(By.ID, Locator.register_ConfirmPassword)
        self.click_Agree = driver.find_element(By.ID, Locator.register_Agree)
        self.click_Signup = driver.find_element(By.ID, Locator.register_Signup_Button)

# you can return WebElement from method and call it, and useful method with parameter define here
    def setName(self, name):
        self.name.clear()
        self.name.send_keys(name)

    def setUserName(self, uname):
        self.username.clear()
        self.username.send_keys(uname)

    def setEmail(self, mail):
        self.email.clear()
        self.email.send_keys(mail)

    def setPassword(self, pwd):
        self.password.clear()
        self.password.send_keys(pwd)

    def setConfirmPasswrod(self, cpwd):
        self.confirmPassword.clear()
        self.confirmPassword.send_keys(cpwd)

    def getAgree(self):
        return self.click_Agree

    def getSignup(self):
        return self.click_Signup

__author__ = 'Yogesh Kumar'

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Locator

class Loggedin_Home(object):

    def __init__(self, driver):
        self.driver = driver

# home page locators defining
        self.menuIcon = driver.find_element(By.ID, Locator.loggedin_Menu)
        self.notificationIcon = driver.find_element(By.ID, Locator.loggedin_NotificationIcon)

# you can return WebElement from method and call it, and useful method with parameter define here
    def clickMenu(self):
        self.menuIcon.click()

    def clickNotification(self):
        self.notificationIcon.click()
"""
Global configs
"""
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "192.168.161.102:5555",
    "app": "D:appdebug.apk",
    "appPackage": "com.fatbit.yokartv9.buyer",
    "appActivity": ".activity.SplashActivity"
}

remote_driver_url = 'http://127.0.0.1:4723/wd/hub'
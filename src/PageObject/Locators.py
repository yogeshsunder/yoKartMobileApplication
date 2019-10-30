__author__ = 'Yogesh Kumar'

class Locator(object):

#home Screen locators
        login_Homescreen = "android.widget.TextView"
        signup_Homescreen = "//android.widget.TextView[@text='Sign up']"

#Sign In screen locators
        signin_Username = "com.fatbit.yokartv9.buyer:id/userName"
        signin_Password = "com.fatbit.yokartv9.buyer:id/password"
        signin_Signin_Button = "com.fatbit.yokartv9.buyer:id/signin"

#Create and Account screen locators
        register_Name = "com.fatbit.yokartv9.buyer:id/name"
        register_UserName = "com.fatbit.yokartv9.buyer:id/userName"
        register_Email = "com.fatbit.yokartv9.buyer:id/email"
        register_Password = "com.fatbit.yokartv9.buyer:id/password"
        register_ConfirmPassword = "com.fatbit.yokartv9.buyer:id/confirmpassword"
        register_Agree = "com.fatbit.yokartv9.buyer:id/cbAgree"
        register_Signup_Button = "com.fatbit.yokartv9.buyer:id/btnSignUp"

#Logged in Home Screen Locators
        loggedin_Menu = "com.fatbit.yokartv9.buyer:id/menu"
        loggedin_NotificationIcon = "com.fatbit.yokartv9.buyer:id/search_notification"
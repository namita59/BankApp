import time

import allure
from selenium.common import TimeoutException

from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator


class Test_SignIn_CLass:
    log = LogGenerator.loggen()

    @allure.feature('SignIn Verification')
    @allure.story('Validate Signin ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test verifies the Signin of the Bank application')
    @allure.link('https://bankapp.credence.in/', 'Bank Application')
    @allure.testcase('TESTCASE_003', 'tEST CASE lINK')
    def test_SignIn_003(self , setup , getDataForLoginValidation):
        self.log.info("test_SignIn_003 is started")
        self.driver = setup
        self.log.info("Browser is opening")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the Login")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the username-->" + getDataForLoginValidation[0])
        self.si.Enter_Username(getDataForLoginValidation[0])
        self.log.info("Entering the password-->" + getDataForLoginValidation[1])
        self.si.Enter_Password(getDataForLoginValidation[1])
        self.log.info("Clicking on login")
        self.si.CLickOn_LogIn_Button()
        self.log.info("Validating the User_Login")
        if self.si.Validate_Login() == "Login_pass" and getDataForLoginValidation[2] == "Login_pass":
            self.passTestcase()
            self.log.info("Clicking on logout")
            self.si.ClickOn_Logout()

        elif self.si.Validate_Login() == "Login_pass" and getDataForLoginValidation[2] == "Login_fail":
            self.failTcase()

        elif self.si.Validate_Login() == "Login_fail" and getDataForLoginValidation[2] == "Login_fail":
            self.passTestcase()

        elif self.si.Validate_Login() == "Login_fail" and getDataForLoginValidation[2] == "Login_pass":
            self.failTcase()

    def failTcase(self):
        self.log.info("test_SignIn_003 is Failed")
        self.log.info("Taking the Screenshot")
        self.driver.save_full_page_screenshot(".\\Screenshots\\test_SignIn_003_fail_png.png")
        assert False

    def passTestcase(self):
        self.log.info("test_SignIn_003 is Passed")
        self.log.info("Taking the Screenshot")
        self.driver.save_full_page_screenshot(".\\Screenshots\\test_SignIn_003_fail_png.png")
        assert True

        self.log.info("Closing the browser")
        self.log.info("test_BankApp_SignIn_003 is completed")
import time
import pytest
import allure
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class
@pytest.mark.usefixture("setup")
class Test_SignIn_CLass:
    log = LogGenerator.loggen()
    driver = None
    login_url = ReadConfig_Class.getLoginUrl()

    @pytest.mark.sanity
    @allure.feature('SignIn Verification')
    @allure.story('Validating Signin ')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test validates the Signin of the Bank application')
    @allure.link('https://bankapp.credence.in/', 'Bank Application')
    @allure.testcase('TESTCASE_003', 'TEST CASE LINK')
    def test_SignIn_003(self ,getDataForLoginValidation):
        username,password,expected_result = getDataForLoginValidation
        with allure.step('test_SignIn_003 is started'):
            self.log.info("test_SignIn_003 is started")
        with allure.step('Landing on the Login Page'):

            self.driver.get(self.login_url)
            self.log.info("Landed on the Login Page")
            si = User_Signin_Class(self.driver)
        with allure.step('Clicking on the Login'):
            self.log.info("Clicking on the Login")
            si.ClickOn_Login_Option()
        with allure.step('Entering the username'):
            self.log.info("Entering the username-->" + username)
            si.Enter_Username(username)
        with allure.step('Entering the password'):
            self.log.info("Entering the password-->" + password)
            si.Enter_Password(password)
        with allure.step('Clicking on login'):
            self.log.info("Clicking on login")
            si.CLickOn_LogIn_Button()
        with allure.step('Validating the User_Login'):
            self.log.info("Validating the User_Login")
            actual_result = si.Validate_Login()
            if actual_result == expected_result:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info("test_SignIn_003 is passed")
                    self.driver.save_screenshot(".\\AllureReports\\test_SignIn_003_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_SignIn_003_pass", attachment_type=allure.attachment_type.PNG)
                    assert True
                    self.log.info("Clicking on logout")
                    si.ClickOn_Logout()
            else:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info("test_SignIn_003 is failed")
                    self.driver.save_screenshot(".\\AllureReports\\test_SignIn_003_fail.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_SignIn_003_fail", attachment_type=allure.attachment_type.PNG)
                    assert False
        with allure.step('test_SignIn_003 is completed'):
            self.log.info("test_SignIn_003 is completed")
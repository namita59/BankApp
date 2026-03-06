from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class
import pytest
import allure

@pytest.mark.usefixture("setup")
class Test_User_Logout_Class:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()
    login_url = ReadConfig_Class.getLoginUrl()
    driver = None

    def test_User_logout_004(self):
        with allure.step('test_User_logout_004 is started'):
            self.log.info("test_User_logout_004 is started")
        with allure.step('Landing on the Login Page'):
            self.driver.get(self.login_url)
            self.log.info("landed on the Login Page")
            si = User_Signin_Class(self.driver)
        with allure.step('Clicking on the Login'):
            self.log.info("Clicking on the Login")
            si.ClickOn_Login_Option()
        with allure.step('Entering the username'):
            self.log.info("Entering the username-->" +self.Username)
            si.Enter_Username(self.Username)
        with allure.step('Entering the password'):
            self.log.info("Entering the password-->" + self.Password)
            si.Enter_Password(self.Password)
        with allure.step('Clicking on login'):
            self.log.info("Clicking on login")
            si.CLickOn_LogIn_Button()
        with allure.step('Clicking on Logout'):
            self.log.info("Clicking on Logout")
            si.ClickOn_Logout()
        with allure.step('Validating the User_Logout'):
            self.log.info("Validating the User_Logout")
            actual_result = si.Validate_Logout()
            expected_result = "Logout_pass"
            if actual_result == expected_result:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                    self.log.info("Test_user_logout004 is passed")
                    self.driver.save_screenshot(".\\AllureReports\\test_user_logout_004_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_user_logout_004_pass", attachment_type=allure.attachment_type.PNG)
                with allure.step('Expected Result: Test_user_logout_004 is passed'):
                    self.log.info("Test_user_logout004 is passed")
                    assert True
            else:
                with allure.step('taking screenshot'):
                    self.driver.save_screenshot(".\\Screenshots\\Test_user_logout_004_fail.png")
                    self.log.info("saved screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_user_logout_004_fail", attachment_type=allure.attachment_type.PNG)
                with allure.step('Expected Result: Test_user_logout004 is failed'):
                    self.log.info("Test_user_logout004 is failed")
                    assert False
        with allure.step('test_User_logout_004 is completed'):
            self.log.info("test_User_logout_004 is completed")
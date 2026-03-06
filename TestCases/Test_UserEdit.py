from selenium import webdriver
from PageObjects.UserMgmt_Edit_page import UserMgmt_Class
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.readConfigFile import ReadConfig_Class
from utilityPackage.loggerfile import LogGenerator
import pytest
import allure
@pytest.mark.usefixture("setup")
class Test_UserMgmt:
    Username = ReadConfig_Class.getUserNametoEdit()
    Password = ReadConfig_Class.getPassword()
    NewUsername =ReadConfig_Class.getNewUserName()
    NewPassword = ReadConfig_Class.getNewPassword()
    NewEmail = ReadConfig_Class.getNewEmail()
    NewPhoneNumber = ReadConfig_Class.getNewPhoneNumber()
    login_url = ReadConfig_Class.getLoginUrl()
    log = LogGenerator.loggen()
    driver = None

    @allure.feature('User Management')
    @allure.story('Valid Edit User')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test verifies the page title of the Bank application')
    @allure.link('https://bankapp.credence.in/' , 'Bank Application')
    @allure.testcase('TESTCASE_005','TEST CASE LINK')
    def test_EditUser_005(self):
        with allure.step('test_EditUser_005 is started'):
            self.log.info("test_EditUser_005 is started")
            self.driver.get(self.login_url)
        with allure.step('Opening the browser'):
            self.log.info("Opening the browser")
            si = User_Signin_Class(self.driver)
        with allure.step('Clicking on the Login'):
            self.log.info("Clicking on the Login")
            si.ClickOn_Login_Option()

        with allure.step('Entering the username'):
            self.log.info("Entering the username-->"+self.Username)
            si.Enter_Username(self.Username)

        with allure.step('Entering the password'):
            self.log.info("Entering the password-->"+self.Password)
            si.Enter_Password(self.Password)

        with allure.step('Clicking on login'):
            self.log.info("Clicking on login")
            si.CLickOn_LogIn_Button()
        with allure.step('Validating the User login'):
            self.log.info("Validating the User login")
            self.log.info("Opening the Dashboard page ")
            um = UserMgmt_Class(self.driver)
        with allure.step('Clicking on the User Management'):
            self.log.info("Clicking on the User Management")
            um.ClickOn_UserMgmt()
        with allure.step('Entering the username'):
            self.log.info("Entering the username-->"+self.Username)
            um.Enter_Username_for_Search(self.Username)
        with allure.step('Clicking on the search'):
            self.log.info("Clicking on the search")
            um.Clickon_Search()
        with allure.step('Entering the New_User_Name'):
            self.log.info("Entering the New_User_Name-->"+self.NewUsername)
            um.Enter_NewUsername(self.NewUsername)

        with allure.step('Entering the New_Password'):
            self.log.info("Entering the New_Password-->"+self.NewPassword)
            um.Enter_NewPassword(self.NewPassword)

        with allure.step('Entering the New_Email'):
            um.Enter_NewEmail(self.NewEmail)
            self.log.info("Entered the New_Email-->"+self.NewEmail)

        with allure.step('Entering the New_Phone_Number'):
            um.Enter_NewPhoneNumber(self.NewPhoneNumber)
            self.log.info("Entered the New_Phone_Number-->"+self.NewPhoneNumber)


        with allure.step('Clicking on Save_Changes'):
            um.Clickon_SaveChanges()
            self.log.info("Clicked on Save_Changes")

        with allure.step('Validating the User Edit'):
            self.log.info("Validating the User Edit")
            actual_result = um.Validate_EditUser()
            expected_result = "UserUpdated"
            if actual_result == expected_result:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                    self.log.info("test_EditUser_005 is passed")
                    self.driver.save_screenshot(".\\AllureReports\\test_EditUser_005_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_EditUser_005_pass", attachment_type=allure.attachment_type.PNG)
                    assert True
            else:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                    self.log.info("test_EditUser_005 is failed")
                    self.driver.save_screenshot(".\\AllureReports\\test_EditUser_005_fail.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_EditUser_005_fail", attachment_type=allure.attachment_type.PNG)
                    assert False
        with allure.step('test_EditUser_005 is completed'):
            self.log.info("test_EditUser_005 is completed")

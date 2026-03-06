import pytest
import allure

from utilityPackage.loggerfile import LogGenerator
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.readConfigFile import ReadConfig_Class
from PageObjects.Search_User_page import Search_User_Page
from utilityPackage.ExcelUtility import ExcelUtility_Class

@pytest.mark.usefixture("setup")
class Test_Search_User_Class:
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    log = LogGenerator.loggen()
    file_path = ".\\TestCases\\Testdata\\TestData.xlsx"
    driver = None
    login_url = ReadConfig_Class.getLoginUrl()
    @pytest.mark.sanity
    @allure.feature('Search User Verification')
    @allure.story('Validating Search User')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test validates the Search User of the Bank application')
    @allure.link('https://bankapp.credence.in/', 'Bank Application')
    @allure.testcase('TESTCASE_015', 'TEST CASE LINK')
    def test_Search_User_015(self):
        with allure.step('test_Search_User_015 is started'):
            self.log.info("test_Search_User_015 is started")
        with allure.step('Landing on the Login Page'):
            self.driver.get(self.login_url)
            si = User_Signin_Class(self.driver)
            self.log.info("Landed on the login Page")
        with allure.step('Clicking on the Login'):
            si.ClickOn_Login_Option()
            self.log.info("Clicked  on the Login")

        with allure.step('Entering the username'):
            si.Enter_Username(self.Username)
            self.log.info("Entering the username-->"+self.Username)

        with allure.step('Entering the password'):
            si.Enter_Password(self.Password)
            self.log.info("Entered the password-->"+self.Password)

        with allure.step('Clicking on login'):
            si.CLickOn_LogIn_Button()
            self.log.info("Clicked on login button")

        su = Search_User_Page(self.driver)
        with allure.step('Clicking on the User Management'):
            su.ClickOn_User_Mgmt()
            self.log.info("Clicking on the User Management")
        with allure.step('Clicking on the ViewAllUsers'):
            su.Click_On_ViewAllUsers()
            self.log.info("Clicked on the ViewAllUsers")

            self.log.info("number of row -->")
        with allure.step('Reading the number of rows'):
            row = ExcelUtility_Class.getRowCount(self.file_path, "userid")
            self.log.info(f"Total rows in Excel: {row}")
            self.log.info("iterating the file")
        for r in range(2, row + 1):
            user_id, ExpectedResult = [ExcelUtility_Class.readData(self.file_path, "userid", r, c)for c in range(2, 3)]
            actual_result = su.ValidateSearch_User(user_id)
            with allure.step(f'Writing the actual result :{actual_result}'):
                ExcelUtility_Class.writeData(self.file_path, "userid", r, 4, actual_result)
                self.log.info(f"Actual Result: {actual_result}")
            with allure.step(f'Writing the status :{"Pass" if actual_result == ExpectedResult else "Fail"}'):
                ExcelUtility_Class.writeData(self.file_path, "userid", r, 5, "Pass" if actual_result == ExpectedResult else "Fail")
                self.log.info(f"Status: {'Pass' if actual_result == ExpectedResult else 'Fail'}")
            if actual_result == ExpectedResult:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {ExpectedResult}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {ExpectedResult}')
                    self.log.info("test_Search_User_015 is passed")
                with allure.step('Taking screenshot'):
                    self.driver.save_screenshot(".\\AllureReports\\test_Search_User_015_pass.png")
                    self.log.info("Saved screenshot")
                with allure.step('Attaching screenshot in Allure Report'):
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Search_User_015_pass", attachment_type=allure.attachment_type.PNG)
                    self.log.info("Attached screenshot in Allure Report")
                with allure.step('Expected Result: Test_Search_User_015 is passed'):
                    self.log.info("Test_Search_User_015 is passed")
                    assert True

            else:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {ExpectedResult}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {ExpectedResult}')
                    self.log.info("test_Search_User_015 is failed")
                with allure.step('Taking screenshot'):
                    self.driver.save_screenshot(".\\AllureReports\\test_Search_User_015_fail.png")
                    self.log.info("saved screenshot")
                with allure.step('Attaching screenshot in Allure Report'):
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Search_User_015_fail", attachment_type=allure.attachment_type.PNG)
                    self.log.info("Attached screenshot in Allure Report")
                with allure.step('test_Search_User_015 is failed'):
                    self.log.info("test_Search_User_015 is failed")
                    assert False

            with allure.step('test_Search_User_015 is completed'):
                self.log.info("test_Search_User_015 is completed")

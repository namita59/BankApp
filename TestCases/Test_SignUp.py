import string
import allure
import random

import pytest

from PageObjects.SignUp_page import SignUp_Page_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

def generate_random_string(length):
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    user_email = f"{username}@fruitsmail.com"
    user_phoneno = f"+1{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    user_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - 1)) + '@'
    return username, user_password, user_email, user_phoneno

@pytest.mark.usefixture("setup")
class Test_SignUp_Class:
    log = LogGenerator.loggen()
    userName,userPassword,userEmail,userPhoneno =generate_random_string(10)
    login_url = ReadConfig_Class.getLoginUrl()
    driver = None
    @allure.feature('URL Verification')
    @allure.story('Verify Page Title')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('this test verifies the page title of the Bank application')
    @allure.link('https://bankapp.credence.in/' , 'Bank Application')
    @allure.testcase('TESTCASE_001' , 'tEST CASE lINK')
    def test_url_001(self , setup):
        with allure.step('test_url_001 is started'):
            self.log.info("test_url_001 is started")
            with allure.step('Landing on the Login Page'):
                self.driver.get(self.login_url)
                self.log.info("Landed on the Login Page")
            with allure.step('Verifying the Browser title'):
                self.log.info("Opening The Browser")
                self.log.info("Verifying the page title-->"+self.driver.title)
            with allure.step('Validating the Browser title'):
                if self.driver.title =="Bank Application":
                    self.driver.save_screenshot(".\\AllureReports\\test_url_001_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_url_001_pass", attachment_type=allure.attachment_type.PNG)
                    self.log.info("test_url_001 is failed")
                    assert True
                else:
                    self.log.info("Taking the screenshot")
                    self.driver.save_screenshot(".\\AllureReports\\test_url_001_fail.png")
                    self.log.info("saved screenshot")
                    allure.attach.file(".\\AllureReports\\test_url_001_fail.png", name="test_url_001_fail", attachment_type=allure.attachment_type.PNG)
                    self.log.info("test_url_001 is failed")
                    assert False
            with allure.step('test_url_001 is completed'):
                self.log.info('test_url_001 is completed')


    @allure.feature('Signup')
    @allure.story('Valid Signup')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test verifies the page title of the Bank application')
    @allure.link('https://bankapp.credence.in/' , 'Bank Application')
    @allure.testcase('TESTCASE_002','TEST CASE LINK')
    def test_SignUp_002(self):
        with allure.step('test_SignUp_002 is started'):
            self.log.info("test_SignUp_002 is started")
            with allure.step('Landing on the Login Page'):
                self.driver.get(self.login_url)
                self.log.info("Landed on the login Page")

            with allure.step('Clicking on signup link'):
                su = SignUp_Page_Class(self.driver)

            with allure.step('Clicking on signup link'):
                su.Clickon_SignUp()
                self.log.info("Clicked on SignUp button")

            with allure.step('Entering the username'):
                self.log.info("Entering the username--->"+self.userName)
                su.Enter_Username(self.userName)
            with allure.step('Entering the password'):
                self.log.info("Entering the password--->"+self.userPassword)
                su.Enter_Password(self.userPassword)
            with allure.step('Entering the password'):
                self.log.info("Enter the Email_id-->"+self.userEmail)
                su.Enter_Emailid(self.userEmail)
            with allure.step('Entering the phone number'):
                self.log.info("Enter the Phone_Number--->"+self.userPhoneno)
                su.Enter_Phoneno(self.userPhoneno)

            with allure.step('Clicking on Create user'):
                self.log.info("Clicking On Create User")
                su.CLickon_CreateUser()
            with allure.step('Validating User created'):
                self.log.info("Validating User_Created")
                expected_result = "SignUpPass"
                actual_result = su.Validate_UserCreated()
                if actual_result == expected_result:
                    with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                        self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                        self.log.info("test_SignUp_002 is passed")
                        self.driver.save_screenshot(".\\AllureReports\\test_SignUp_002_pass.png")
                        allure.attach.file(".\\AllureReports\\test_SignUp_002_pass.png", name="test_SignUp_002_pass", attachment_type=allure.attachment_type.PNG)
                        assert True
                else:
                    with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                        self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                        self.log.info("test_SignUp_002 is failed")
                        self.driver.save_screenshot(".\\AllureReports\\test_SignUp_002_fail.png")
                        allure.attach.file(".\\AllureReports\\test_SignUp_002_fail.png", name="test_SignUp_002_fail", attachment_type=allure.attachment_type.PNG)
                        assert False
            with allure.step('test_SignUp_002 is completed'):
                self.log.info("test_SignUp_002 is completed")

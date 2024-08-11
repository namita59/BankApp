import string
import allure
import random

import pytest

from PageObjects.SignUp_page import SignUp_Page_Class
from utilityPackage.loggerfile import LogGenerator


def generate_random_string(length):
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    user_email = f"{username}@fruitsmail.com"
    user_phoneno = f"+1{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    user_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - 1)) + '@'
    return username, user_password, user_email, user_phoneno


class Test_SignUp_Class:
    log = LogGenerator.loggen()
    userName,userPassword,userEmail,userPhoneno =generate_random_string(10)
    @allure.feature('URL Verification')
    @allure.story('Verify Page Title')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('this test verifies the page title of the Bank application')
    @allure.link('https://bankapp.credence.in/' , 'Bank Application')
    @allure.testcase('TESTCASE_001' , 'tEST CASE lINK')
    def test_url_001(self , setup):
        with allure.step('test_url_001 is started'):
            self.log.info("test_url_001 is started")
            self.driver = setup
            with allure.step('Verifying the Browser title'):
                self.log.info("Opening The Browser")
                self.log.info("Verifying the page title-->"+self.driver.title)
            with allure.step('Validating the Browser title'):
                if self.driver.title =="Bank Application":
                    screenshot = self.driver.get_screenshot_as_png()
                    allure.attach(screenshot, name="test_url_001_pass", attachment_type=allure.attachment_type.PNG)
                    self.log.info("test_url_001 is failed")
                    assert True
                else:
                    self.log.info("Taking the screenshot")
                    self.driver.save_full_page_screenshot(".\\AllureReports\\test_url_001_fail.png")
                    screenshot = self.driver.get_screenshot_as_png()
                    allure.attach(screenshot,name="test_url_001_fail",attachment_type=allure.attachment_type.PNG)
                    self.log.info("test_url_001 is failed")
                    assert False
            with allure.step('test_url_001 is completed'):
                self.log.info('test_url_001 is completed')


    @allure.feature('Signup')
    @allure.story('Valid Signup')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('TESTCASE_002','TEST CASE LINK')
    def test_SignUp_002(self,setup):
        with allure.step('test_SignUp_002 is started'):
            self.log.info("test_SignUp_002 is started")
            self.driver=setup
            with allure.step('Opening browser'):
                self.log.info("Opening the browser")
                self.su =SignUp_Page_Class(self.driver)
            with allure.step('Clicking on signup Button'):
                self.log.info("Clicking on SignUp button")
                self.su.Clickon_SignUp()
            with allure.step('Entering the username'):
                self.log.info("Entering the username--->"+self.userName)
                self.su.Enter_Username(self.userName)
            with allure.step('Entering the password'):
                self.log.info("Entering the password--->"+self.userPassword)
                self.su.Enter_Password(self.userPassword)
            with allure.step('Entering the password'):
                self.log.info("Enter the Email_id-->"+self.userEmail)
                self.su.Enter_Emailid(self.userEmail)
            with allure.step('Entering the phone number'):
                self.log.info("Enter the Phone_Number--->"+self.userPhoneno)
                self.su.Enter_Phoneno(self.userPhoneno)

            with allure.step('Clicking on Create user'):
                self.log.info("Clicking On Create User")
                self.su.CLickon_CreateUser()
            with allure.step('Validating User created'):
                self.log.info("Validating User_Created")
                if self.su.Validate_UserCreated() =="SignUpPass":
                    self.log.info("test_SignUp_002 is passed")
                    self.driver.save_screenshot(".\\AllureReports\\test_SignUp_002_pass_png")
                    screenshot = self.driver.get_screenshot_as_png()
                    allure.attach(screenshot, name="test_SignUp_002_pass", attachment_type=allure.attachment_type.PNG)
                    assert True
                else:
                    self.log.info("test_SignUp_002 is failed")
                    self.driver.save_screenshot(".\\AllureReports\\test_SignUp_002_fail.png")
                    screenshot = self.driver.get_screenshot_as_png()
                    allure.attach(screenshot, name="test_SignUp_002_fail", attachment_type=allure.attachment_type.PNG)
                    assert False
            with allure.step('closing the browser'):
                self.log.info("Closing the Browser")
            with allure.step('test_SignUp_002 is completed'):
                self.log.info("test_SignUp_002 is completed")

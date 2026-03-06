from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Cust_Mgmt_Create_page import Cust_Mgmt_Create_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class
import pytest
import allure

@pytest.mark.usefixtures("setup")
class Test_Custmgmt_Create_Class:
    UserName=ReadConfig_Class.getNewUserName()
    Password =ReadConfig_Class.getNewPassword()
    UserId_to_create =ReadConfig_Class.getUserid_to_Create_cust()
    log = LogGenerator.loggen()
    driver = None
    login_url = ReadConfig_Class.getLoginUrl()
    @pytest.mark.sanity
    @allure.feature('Customer Creation Verification')
    @allure.story('Validating Customer Creation')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('this test validates the Customer Creation of the Bank application')
    @allure.link('https://bankapp.credence.in/', 'Bank Application')
    @allure.testcase('TESTCASE_006', 'TEST CASE LINK')
    def test_Cust_Create_006(self,getDataForCustomerCreate):
        user_id,firstname,lastname,dob,address,city,state,zipcode = getDataForCustomerCreate

        with allure.step("test_Cust_Create_006 is started"):
            self.log.info("test_Cust_Create_006 is started")
        with allure.step("Landing on the Login Page"):
            self.driver.get(self.login_url)
            self.log.info("Landed on the Login Page")
            si = User_Signin_Class(self.driver)
        with allure.step("Clicking on the Login"):
            si.ClickOn_Login_Option()
            self.log.info("Clicked on the Login")
        with allure.step("Entering the username-->"+self.UserName):
            si.Enter_Username(self.UserName)
            self.log.info("Entered the username-->"+self.UserName)
        with allure.step("Entering the password-->"+self.Password):
            si.Enter_Password(self.Password)
            self.log.info("Entered the password-->"+self.Password)
            self.log.info("Clicking on Login button-->")
        with allure.step("Clicking on Login button"):
            si.CLickOn_LogIn_Button()
            self.log.info("Clicked on Login button")
            cm =Cust_Mgmt_Create_Class(self.driver)
        with allure.step("Clicking on the Customer mgmt option"):
            cm.ClickOn_CustMgmt_link()
            self.log.info("Clicked on the Customer mgmt option")
        with allure.step("Clicking on the create customer"):
            cm.Clickon_CreateCust_link()
            self.log.info("Clicked on the create customer")
        with allure.step("Entering  the user id of Existing Customer-->"+user_id):
            cm.Enter_UserId(user_id)
            self.log.info("Entered the user id of Existing Customer-->"+user_id)
        with allure.step("Entering Customer Firstname-->"+firstname):
            cm.Enter_Firstname(firstname)
            self.log.info("Entered Customer Firstname-->"+firstname)
        with allure.step("Entering Customer lastname-->"+lastname):
            cm.Enter_Lastname(lastname)
            self.log.info("Entered Customer lastname-->"+lastname)
        with allure.step("Entering ddate of birth of a customer-->"+dob):
            cm.Enter_Dob(dob)
            self.log.info("Entered ddate of birth of a customer-->"+dob)
        with allure.step("Entering the address of the customer-->"+address):
            cm.Enter_Add(address)
            self.log.info("Entered the address of the customer-->"+address)
        with allure.step("Entering the city-->"+city):
            cm.Enter_City(city)
            self.log.info("Entered the city-->"+city)
        with allure.step("Entering the state of the customer-->"+state):
            cm.Enter_State(state)
            self.log.info("Entered the state of the customer-->"+state)
        with allure.step("Entering the zipcode-->"+zipcode):
            cm.Enter_Zipcd(zipcode)
            self.log.info("Entered the zipcode-->"+zipcode)
        with allure.step("Clicking on the create customer"):
            cm.Clickon_Create_Cust_button()
            self.log.info("Clicked on the create customer")
        with allure.step("Validating the Customer Creation"):
            actual_result = cm.Validate_Cust_Created()
            expected_result = "Customer created successfully"
            if actual_result == expected_result:
                with allure.step(f'Actual Result: {actual_result} Expected Result: {expected_result}'):
                    self.log.info(f'Actual Result: {actual_result} Expected Result: {expected_result}')
                    self.log.info("test_Cust_Create_006 is passed")
                    self.driver.save_screenshot(".\\AllureReports\\test_Cust_Create_006_pass.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_Cust_Create_006_pass", attachment_type=allure.attachment_type.PNG)
                    assert True
            else:
                print("Unable to create customer")
                self.driver.save_screenshot(".\\AllureReports\\test_Cust_Create_006_fail.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_Cust_Create_006_fail", attachment_type=allure.attachment_type.PNG)
                self.log.info("test_Cust_Create_006 is failed")
                assert False

        with allure.step("test_Cust_Create_006 is completed"):
            self.log.info("test_Cust_Create_006 is Completed ")
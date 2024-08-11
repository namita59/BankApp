from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Cust_Mgmt_Create_page import Cust_Mgmt_Create_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class
import pytest


class Test_Custmgmt_Create_Class:
    UserName=ReadConfig_Class.getNewUserName()
    Password =ReadConfig_Class.getNewPassword()
    UserId_to_create =ReadConfig_Class.getUserid_to_Create_cust()
    log = LogGenerator.loggen()
    def test_Cust_Create_006(self,setup,getDataForCustomerCreate):
        self.log.info("test_Cust_Create_005 is started")
        self.driver =setup
        self.log.info("Opening browser")
        self.si = User_Signin_Class(self.driver)
        self.log.info("clicking on Login option")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the username-->"+self.UserName)
        self.si.Enter_Username(self.UserName)
        self.log.info("Entering the password-->"+self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on Login button-->")
        self.si.CLickOn_LogIn_Button()
        self.cm =Cust_Mgmt_Create_Class(self.driver)
        self.log.info("Clicking on the Customer mgmt option")
        self.cm.ClickOn_CustMgmt_link()
        self.log.info("Clicking on the create customer")
        self.cm.Clickon_CreateCust_link()
        self.log.info("Entering  the user id of Existing Customer-->"+self.UserId_to_create)
        self.cm.Enter_UserId(self.UserId_to_create)
        self.log.info("Entering Customer Firstname-->"+getDataForCustomerCreate[0])
        self.cm.Enter_Firstname(getDataForCustomerCreate[0])
        self.log.info("Entering Customer lastname-->"+getDataForCustomerCreate[1])
        self.cm.Enter_Lastname(getDataForCustomerCreate[1])
        self.log.info("Entering ddate of birth of a customer-->"+getDataForCustomerCreate[2])
        self.cm.Enter_Dob(getDataForCustomerCreate[2])
        self.log.info("Entering the address of the customer-->"+getDataForCustomerCreate[3])
        self.cm.Enter_Add(getDataForCustomerCreate[3])
        self.log.info("Entering the city-->"+getDataForCustomerCreate[4])
        self.cm.Enter_City(getDataForCustomerCreate[4])
        self.log.info("Entering the state of the customer-->"+getDataForCustomerCreate[5])
        self.cm.Enter_State(getDataForCustomerCreate[5])
        self.log.info("Entering the zipcode-->"+getDataForCustomerCreate[6])
        self.cm.Enter_Zipcd(getDataForCustomerCreate[6])
        self.log.info("clicking on the create customer")
        self.cm.Clickon_Create_Cust_button()
        self.log.info("Validate Create customer")
        if self.cm.Validate_Cust_Created()=="Customer created successfully":
            self.log.info("test_Cust_Create_005 is passed")
            print("customer Created")
            assert True
        else:
            print("Unable to create customer")
            self.driver.sav_screenshot(".\\Screenshots\\Test_Cust_Create_005")
            self.log.info("test_Cust_Create_005 is failed")
            assert False

        self.log.info("Closing the browser")
        self.log.info("test_Cust_Create_006 is Completed ")
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class
from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Cust_Mgmt_Edit_page import Cust_Mgmt_Edit_Class
from selenium import webdriver
class Test_BankApp_Cust_Edit_Class:
    log =LogGenerator.loggen()
    Cust_id = ReadConfig_Class.getCustomerId()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    NewFirstname =ReadConfig_Class.getCustNewFirstname()
    NewLastName = ReadConfig_Class.getCustNewLastname()
    NewDob = ReadConfig_Class.getCustNewDob()

    def test_Cust_Edit_007(self,setup,):
        self.log.info("test_Cust_Edit_006 is started")
        self.driver = setup
        self.log.info("Opening the Browser")
        self.si =User_Signin_Class(self.driver)
        self.log.info("Clicking on the Login link")
        self.si.ClickOn_Login_Option()
        self.log.info("Enter the user name-->"+self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Enter the Password-->"+self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the Login Button")
        self.si.CLickOn_LogIn_Button()
        self.log.info("Opening the Browser")
        self.eme = Cust_Mgmt_Edit_Class(self.driver)
        self.log.info("Clicking on the Customer Management")
        self.eme.ClickOn_CustMgmt_link()
        self.log.info("Entering the  Customer_id-->"+self.Cust_id)
        self.eme.Enter_Custid(self.Cust_id)
        self.log.info("Clicking on the search button ")
        self.eme.ClickOn_Search_Button()
        self.log.info("Entering the new firstname and clearing the old one-->"+self.NewFirstname)
        self.eme.Enter_FirstName(self.NewFirstname)
        self.log.info("Entering the new Lastname and clearing the old one--->"+self.NewLastName)
        self.eme.Enter_LastName(self.NewLastName)
        self.log.info("Entering the new DateOfBirth and clearing the old one--->"+self.NewDob)
        self.eme.Enter_DateOfBirth(self.NewDob)
        self.log.info("Clicking on the Save button")
        self.eme.ClickOn_Save_Button()
        self.log.info("Validating the Customer Updation")
        if self.eme.Validate_Cust_Edit()=="Customer updated successfully!":
            self.log.info("test_Cust_Edit_006 is passed")
            self.driver.save_screenshot(".\\Screenshots\\test_cust_edit_006_pass.png")
            assert True
        else:
            self.log.info("test_Cust_Edit_006 is Failed")
            self.driver.save_screenshot(".\\Screenshots\\test_cust_edit_006_Fail.png")
            assert False

        self.log.info("Closing the browser")
        self.log.info("test_Cust_Edit_007 is Completed ")

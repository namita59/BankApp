from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Cust_Mgmt_Edit_page import Cust_Mgmt_Edit_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_BankApp_Cust_Delete_Class:
    log = LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    Customer_id_del = ReadConfig_Class.getCustomerId_to_Del()
    def test_BankApp_Cust_del_008(self,setup):
        self.log.info("test_BankApp_Cust_del_007 is started")
        self.driver = setup
        self.log.info("Opening the browser to login user")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the login option")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering  the username-->"+self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password-->"+self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the login button")
        self.si.CLickOn_LogIn_Button()
        self.log.info("opening the browser to edit customer")
        self.cme = Cust_Mgmt_Edit_Class(self.driver)
        self.log.info("Clicking on the Customer management option")
        self.cme.ClickOn_CustMgmt_link()
        self.log.info("Entering the Customer id-->"+self.Customer_id_del)
        self.cme.Enter_Custid(self.Customer_id_del)
        self.log.info("Clicking on the search button")
        self.cme.ClickOn_Search_Button()
        self.log.info("Clicking on the delete button")
        self.cme.ClickOn_Delete_Button()
        self.log.info("Validating the customer delete")
        if self.cme.Validate_Cust_Delete() == "Customer deleted successfully":
            self.log.info("taking the Screenshots")
            self.driver.save_screenshot("\\Screenshots\\test_Cust_del_007_Pass.png")
            print("Customer has been deleted")
            self.log.info("test_Cust_del_007 is passed")
            assert True
        else:
            self.driver.save_screenshot("\\Screenshots\\test_Cust_del_007_Pass.png")
            self.log.info("test_BankApp_Cust_del_007 is failed")
            assert False
        self.log.info("test_Cust_del_007 is completed")

        self.log.info("Closing the browser")
        self.log.info("test_Cust_del_008 is Completed ")
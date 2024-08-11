from utilityPackage.loggerfile import LogGenerator
from PageObjects.Acc_Mgmt_Create_page import Account_Mgmt_Create_Page
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.readConfigFile import ReadConfig_Class
class Test_Account_Create_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()

    def test_Account_Create_009(self,setup,getDataForAccountCreate):
        self.log.info("test_Account_Create_009 is started")
        self.driver = setup
        self.log.info("opening the browser")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the login option")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the Username")
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password")
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the login button")
        self.si.CLickOn_LogIn_Button()
        self.acc =Account_Mgmt_Create_Page(self.driver)
        self.log.info("Clicking on the account mgmt ")
        self.acc.ClickOn_Acc_Mgmt()
        self.log.info("Clicking on the Create account link")
        self.acc.ClickOn_Create_Acc_Link()
        self.log.info("Entering the Customer id")
        self.acc.Enter_CustID(getDataForAccountCreate[0])
        self.log.info("selecting  the Account type ")
        self.acc.DropDown_Acc_Type(getDataForAccountCreate[1])
        self.log.info("Entering the balance")
        self.acc.Enter_Balance(getDataForAccountCreate[2])
        self.log.info("Clicking on the Create account button")
        self.acc.ClickOn_Create_Acc_Button()
        self.log.info("Validating account has been created")
        if self.acc.Validate_Create_Acc() =="Account created successfully":
            self.log.info("test_Account_Create_009 is paseed")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Account_Create_009_fail.png")
            self.log.info("test_Account_Create_009 is failed")
            assert False

        self.log.info("Closing the browser")
        self.log.info("test_Account_Create_009 is Completed ")
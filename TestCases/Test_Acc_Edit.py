from PageObjects.Acc_Mgmt_Edit_Page import Acc_Mgmt_to_Edit_Page
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Account_Edit_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    Accountid = ReadConfig_Class.getAccountId()
    AccountType = ReadConfig_Class.getNewAccountType()
    Balance = ReadConfig_Class.getNewBalance()

    def test_Account_Edit_010(self,setup):
        self.log.info("test_Account_Edit_010 is started ")
        self.driver = setup
        self.log.info("opening the browser")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the login option")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the Username-->"+self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password-->"+self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the login button")
        self.si.CLickOn_LogIn_Button()

        self.ace = Acc_Mgmt_to_Edit_Page(self.driver)
        self.log.info("Clicking on Account management link")
        self.ace.ClickOn_Acc_Mgmt_Link()
        self.log.info("Entering the account id-->"+self.Accountid)
        self.ace.Enter_AccountId(self.Accountid)
        self.log.info("Clicking on the search account button")
        self.ace.ClickOn_Search_Acc_Button()
        self.log.info("Clicking on the edit button")
        self.ace.ClickOn_Edit_Button()
        self.log.info("selecting the account type-->"+self.AccountType)
        self.ace.select_DropDown_Acc_Type(self.AccountType)
        self.log.info("entering the balance-->"+self.Balance)
        self.ace.Enter_Balance(self.Balance)
        self.log.info("Clicking on the Update account button")
        self.ace.ClickOn_Update_Account_Button()
        self.log.info("Validating account has been updated")
        if self.ace.Validate_Acc_Updated() =="Account updated successfully ":
            self.log.info("test_Account_Edit_010 is pass")
            return True
        else:
            self.log.info("test_Account_Edit_010 is fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Account_Edit_010_fail_png")
            return False

        self.log.info("Closing the browser")
        self.driver.Quit()
        self.log.info("test_Account_Edit_010 is Completed ")
from PageObjects.Acc_Mgmt_Edit_Page import Acc_Mgmt_to_Edit_Page
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Account_Delete_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    Accountid = ReadConfig_Class.getAccountId()

    def test_Account_Delete_011(self,setup):
        self.log.info("test_Account_Edit_011 is started ")
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
        self.log.info("Clicking on the delete button")
        self.ace.ClickOn_Delete_Button()
        self.log.info("Validating account has been updated")
        self.ace.Enter_AccountId(self.Accountid)
        self.ace.ClickOn_Search_Acc_Button()
        if self.ace.Validate_Acc_Deleted() =="No accounts found":
            self.log.info("test_Account_delete_011 is pass")
            return True
        else:
            self.log.info("test_Account_delete_011 is fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Account_delete_011_fail_png")
            return False

        self.log.info("Closing the browser")
        self.log.info("test_Account_delete_0011 is Completed ")
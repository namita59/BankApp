from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Fund_Tansfer_Mgmt_Edit_Page import Fund_transfer_Edit_page
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Fund_Transfer_Delete_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    Tranferid = ReadConfig_Class.getTransferId()
    def test_Fund_Transfer_Delete_014(self,setup):
        self.log.info("test_Fund_Transfer_Delete_014 is started")
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
        self.fte =Fund_transfer_Edit_page(self.driver)
        self.log.info("CLicking on the fund transfer mgmt link")
        self.fte.ClickOn_Fund_Tranfer_Mgmt_link()
        self.log.info("Entering the transfer id -->"+self.Tranferid)
        self.fte.Enter_TranferID(self.Tranferid)
        self.log.info("Clicking on the search transfer button")
        self.fte.ClickOn_Search_Transfer_Button()
        self.log.info("Clicking on the delete Transfer button")
        self.fte.ClickOn_Delete_Transfer_Button()
        self.log.info("Validating delete transfer is not applicable")
        if self.fte.Validate_Delete_Transfer() == "Cannot POST /delete-fundsTransfer":
            self.log.info("test_Fund_Transfer_Delete_014 is pass")
            assert True
        else:
            self.log.info("test_Fund_Transfer_Delete_014 is fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Fund_Transfer_Delete_014_fail.png")
            assert False

        self.log.info("Closing the browser")

        self.log.info("test_Fund_Transfer_Delete_014 is Completed ")
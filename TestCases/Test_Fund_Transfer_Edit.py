from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Fund_Tansfer_Mgmt_Edit_Page import Fund_transfer_Edit_page
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Fund_Transfer_Edit_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    Tranferid = ReadConfig_Class.getTransferId()
    Amount = ReadConfig_Class.getAmount()
    Description = ReadConfig_Class.getDescription()
    def test_Fund_Transfer_Edit_013(self,setup):
        self.log.info("test_Fund_Transfer_Edit_013 is started")
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
        self.log.info("Entering the Amount -->" + self.Amount)
        self.fte.Enter_Amnt(self.Amount)
        self.log.info("Entering the Description -->" + self.Description)
        self.fte.Enter_Descript(self.Description)
        self.log.info("Clicking on the Update transfer button")
        self.fte.ClickOn_UpDate_Transfer_Button()
        self.log.info("Validating the update transfer")
        if self.fte.Validate_Update_Transfer() =="Funds transfer updated successfully":
            self.log.info("test_Fund_Transfer_Edit_013 is pass")
            assert True
        else:
            self.log.info("test_Fund_Transfer_Edit_013 is fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Fund_Transfer_Edit_013_fail.png")
            assert False
        self.log.info("Closing the browser")

        self.log.info("test_Fund_Transfer_Edit_013 is Completed ")
from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Fund_Transfer_Mgmt_Create_Page import Fund_Transfer_Mgmt_To_Create_Page
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Fund_Transfer_Create_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()

    def test_Fund_Transfer_Create_012(self,setup,getDataForFundTransferCreate):
        self.log.info("test_Fund_Transfer_Create_012 is started")
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
        self.ftc =Fund_Transfer_Mgmt_To_Create_Page(self.driver)
        self.log.info("Clicking on the fund transfer link")
        self.ftc.ClickOn_Fund_Transer_Mgmt_Link()
        self.log.info("Clicking on the create transfer link")
        self.ftc.ClickOn_Create_Transfer_Link()
        self.log.info("Entering from account id-->"+getDataForFundTransferCreate[0])
        self.ftc.Enter_From_AccId(getDataForFundTransferCreate[0])
        self.log.info("Entering to account id -->"+getDataForFundTransferCreate[1])
        self.ftc.Enter_To_AccId(getDataForFundTransferCreate[1])
        self.log.info("Entering the amount -->"+getDataForFundTransferCreate[2])
        self.ftc.Enter_Amnt(getDataForFundTransferCreate[2])
        self.log.info("Entering the Description-->"+getDataForFundTransferCreate[3])
        self.ftc.Enter_Descript(getDataForFundTransferCreate[3])
        self.log.info("Clicking on the Transfer fund button")
        self.ftc.ClickOn_Transfer_Fund_Button()
        self.log.info("Validating the Fund transfer")
        if self.ftc.Validate_Fund_Transfer() =="Funds transferred successfully":
            self.log.info("test_Fund_Transfer_Create_012 is pass")
            assert True
        else:
            self.log.info("test_Fund_Transfer_Create_012 is fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Fund_Transfer_Create_012_fail.png")
            assert False

        self.log.info("Closing the browser")

        self.log.info("test_Fund_Transfer_Create_012 is Completed ")
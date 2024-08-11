from PageObjects.SignIn_Page import User_Signin_Class
from PageObjects.Bill_Payment_page import Bill_Pay_page
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_Bill_Payment_Create_Class:
    log =LogGenerator.loggen()
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()

    def test_Bill_Payment_Create_014(self,setup,getDataForBillPayment):
        self.log.info("test_Bill_Payment_014 is started")
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

        self.bp =Bill_Pay_page(self.driver)
        self.log.info("CLicking on the bill payment link")
        self.bp.ClickOn_BillPayment_LinK()
        self.log.info("Entering the Account id-->"+getDataForBillPayment[0])
        self.bp.Enter_AccountID(getDataForBillPayment[0])
        self.log.info("Entering the name of payee-->"+getDataForBillPayment[1])
        self.bp.Enter_PayeeName(getDataForBillPayment[1])
        self.log.info("Entering the amount -->"+getDataForBillPayment[2])
        self.bp.Enter_Amount(getDataForBillPayment[2])
        self.log.info("Entering the description-->"+getDataForBillPayment[3])
        self.bp.Enter_Descript(getDataForBillPayment[3])
        self.log.info("Clicking on the paybill button")
        self.bp.ClickOn_PayBill_Button()
        self.log.info("Validating the bill pay ")
        if self.bp.Validate_Billpay() == "Bill payment created successfully":
            self.log.info("test_Bill_Payment_Create_014 is pass ")
            assert True

        else:
            self.log.info("test_Bill_Payment_Create_014 is fail ")
            self.driver.save_screenshot(".\\Screenshots\\test_Bill_Payment_Create_014_fail.png")
            assert False

        self.log.info("Closing the browser")
        self.log.info("test_Bill_Payment_Create_014 is Completed ")
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.loggerfile import LogGenerator
from utilityPackage.readConfigFile import ReadConfig_Class

class Test_User_Logout_Class:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()
    log = LogGenerator.loggen()

    def test_User_logout_004(self,setup):
        self.log.info("test_SignOut_004 is started")
        self.driver = setup
        self.log.info("Browser is opening")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the Login")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the username-->" +self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password-->" + self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on login")
        self.si.CLickOn_LogIn_Button()
        self.log.info("Click on Logout")
        self.si.ClickOn_Logout()
        self.log.info("Validating the User_Logout")
        if self.si.Validate_Logout() == "SuccessfullyLogout":
            self.log.info("Test_user_logout004 is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\Test_user_logout_003_fail.png")
            self.log.info("Test_user_logout004 is failed")
            assert False

        self.log.info("Closing the browser")

        self.log.info("test_User_logout_004 is Completed ")
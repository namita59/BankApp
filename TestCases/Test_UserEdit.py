from selenium import webdriver
from PageObjects.UserMgmt_Edit_page import UserMgmt_Class
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.readConfigFile import ReadConfig_Class
from utilityPackage.loggerfile import LogGenerator
class Test_UserMgmt:
    Username = ReadConfig_Class.getUserNametoEdit()
    Password = ReadConfig_Class.getPassword()
    NewUsername =ReadConfig_Class.getNewUserName()
    NewPassword = ReadConfig_Class.getNewPassword()
    log = LogGenerator.loggen()

    def test_EditUser_005(self,setup):
        self.log.info("test_EditUser_004 is started ")
        self.log.info("Browser is opening")
        self.driver = setup
        self.log.info("Opening the Home page ")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the login")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the Username-->"+self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password-->"+self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the login button")
        self.si.CLickOn_LogIn_Button()
        self.log.info("Validating the User login")
        self.log.info("Opening the Dashboard page ")
        self.um = UserMgmt_Class(self.driver)
        self.log.info("Clicking on the User Management")
        self.um.Clickon_UserMgmt()
        self.log.info("Entering the username-->"+self.Username)
        self.um.Enter_Username_for_Search(self.Username)
        self.log.info("Clicking on the search")
        self.um.Clickon_Search()
        self.log.info("Erasing the old user name and Entering the New_User_Name-->"+self.NewUsername)
        self.um.Enter_NewUsername(self.NewUsername)
        self.log.info("Erasing the Old_password and Entering the New_Password-->"+self.NewPassword)
        self.um.Enter_NewPassword(self.NewPassword)
        self.log.info("Clicking on Save_Changes")
        self.um.Clickon_SaveChanges()
        self.log.info("Validating the User Edited or Not")
        if self.um.Validate_EditUser() == "UserUpdated":
            print("User_Edit_Pass")
            self.log.info("test_EditUser_004 is passed")
            assert True
        else:
            print("User_Edit_Failed")
            self.log.info("test_EditUser_004 is failed")
            self.driver.save_screenshot(".\\Screenshots\\test_EditUser_004_fail.png")
            assert False
        self.log.info("closing the browser")
        self.log.info("test_EditUser_004 is completed")

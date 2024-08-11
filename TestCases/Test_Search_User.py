# import time
#
# import pytest
#
import time

from utilityPackage.loggerfile import LogGenerator
from PageObjects.SignIn_Page import User_Signin_Class
from utilityPackage.readConfigFile import ReadConfig_Class
from PageObjects.Search_User_page import Search_User_Page
from utilityPackage import ExcelUtility
# class Test_Search_User:
#     Username = ReadConfig_Class.getNewUserName()
#     Password = ReadConfig_Class.getNewPassword()
#     log = LogGenerator.loggen()
#     file_path = ".\\TestCases\\Testdata\\TestData.xlsx"
#     List_status = []
#     def test_Search_User_015(self,setup):
#         self.log.info("test_Search_User_015 is started")
#         self.driver = setup
#         self.log.info("Opening the browser to login user")
#         self.si = User_Signin_Class(self.driver)
#         self.log.info("Clicking on the login option")
#         self.si.ClickOn_Login_Option()
#         self.log.info("Entering  the username-->" + self.Username)
#         self.si.Enter_Username(self.Username)
#         self.log.info("Entering the password-->" + self.Password)
#         self.si.Enter_Password(self.Password)
#         self.log.info("Clicking on the login button")
#         self.si.CLickOn_LogIn_Button()
#         self.su = Search_User_Page(self.driver)
#         self.log.info("Clicking on the user management")
#         self.su.ClickOn_User_Mgmt()
#         self.log.info("Clicking on the Viewallusers")
#         self.su.Click_On_ViewAllUsers()
#         self.log.info("number of row -->")
#         self.row =ExcelUtility.getRowCount(self.file_path,"Username")
#         self.log.info("iterating the file")
#         for r in range(2,self.row+1):
#             self.log.info("reading user id from Excel sheet-->")
#             self.UserID =ExcelUtility.readData(self.file_path,"Username",r,2)
#             self.log.info("reading expected result")
#             self.ExpectedResult = ExcelUtility.readData(self.file_path, "Username", r, 3)
#             time.sleep(5)
#             if self.UserID in self.su.Search_User() and self.ExpectedResult =="pass":
#                 self.actual = ExcelUtility.writeData(self.file_path, "Username", r, 4, "pass")
#                 self.List_status.append("pass")
#             else:
#                 self.actual=ExcelUtility.writeData(self.file_path, "Username", r, 4, "fail")
#                 self.List_status.append("fail")
#
#         if "fail" not in self.List_status:
#             assert True
#         else:
#             assert False
#
#
# import time
# from utilityPackage.loggerfile import LogGenerator
# from PageObjects.SignIn_Page import User_Signin_Class
# from utilityPackage.readConfigFile import ReadConfig_Class
# from PageObjects.Search_User_page import Search_User_Page
# from utilityPackage import ExcelUtility

class Test_Search_User:
    Username = ReadConfig_Class.getNewUserName()
    Password = ReadConfig_Class.getNewPassword()
    log = LogGenerator.loggen()
    file_path = ".\\TestCases\\Testdata\\TestData.xlsx"
    List_status = []

    def test_Search_User_015(self, setup):
        self.log.info("test_Search_User_015 is started")
        self.driver = setup
        self.log.info("Opening the browser to login user")
        self.si = User_Signin_Class(self.driver)
        self.log.info("Clicking on the login option")
        self.si.ClickOn_Login_Option()
        self.log.info("Entering the username-->" + self.Username)
        self.si.Enter_Username(self.Username)
        self.log.info("Entering the password-->" + self.Password)
        self.si.Enter_Password(self.Password)
        self.log.info("Clicking on the login button")
        self.si.CLickOn_LogIn_Button()
        self.su = Search_User_Page(self.driver)
        self.log.info("Clicking on the user management")
        self.su.ClickOn_User_Mgmt()
        self.log.info("Clicking on the Viewallusers")
        self.su.Click_On_ViewAllUsers()
        self.log.info("number of row -->")
        self.row = ExcelUtility.getRowCount(self.file_path, "userid")
        self.log.info(f"Total rows in Excel: {self.row}")
        self.log.info("iterating the file")

        for r in range(2, self.row + 1):
            self.log.info(f"Processing row {r}")
            self.log.info("reading user id from Excel sheet-->")
            user_id = str(ExcelUtility.readData(self.file_path, "userid", r, 2))
            self.log.info(f"User ID from Excel: {user_id}")
            self.log.info("reading expected result")
            self.ExpectedResult = ExcelUtility.readData(self.file_path, "userid", r, 3)
            self.log.info(f"Expected Result: {self.ExpectedResult}")
            time.sleep(5)
            actual_user_ids = self.su.Search_User()
            self.log.info(f"Actual User IDs: {actual_user_ids}")

            if user_id in actual_user_ids and self.ExpectedResult == "pass":
                self.log.info(f"User ID {user_id} found, writing 'pass'")
                ExcelUtility.writeData(self.file_path, "userid", r, 4, "pass")
                self.List_status.append("pass")
            else:
                self.log.info(f"User ID {user_id} not found or expected result is not 'pass', writing 'fail'")
                ExcelUtility.writeData(self.file_path, "userid", r, 4, "fail")
                self.List_status.append("fail")

        self.log.info(f"Final List Status: {self.List_status}")
        if "fail" not in self.List_status:
            assert True
        else:
            assert False
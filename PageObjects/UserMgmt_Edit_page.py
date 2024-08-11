import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserMgmt_Class:
    Clickon_UserMgmt_Xpath = (By.XPATH,"//a[normalize-space()='User Management']")
    Clickon_Search_Button_Xpath=(By.XPATH,"//button[@type='submit']")
    Clickon_SaveChnages_Button_Xpath = (By.XPATH,"//button[normalize-space()='Save Changes']")
    Text_Search_Username_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/form[1]/input[1]")
    Text_Username_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/form[1]/input[2]")
    Text_Password_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/form[1]/input[3]")
    Text_Phone_Number_Xpath =(By.XPATH,"/html[1]/body[1]/div[1]/form[1]/input[5]")
    Success_Validate_Xpath = (By.XPATH,"/html/body/div/div[2]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,40)

    def Clickon_UserMgmt(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_UserMgmt_Xpath)).click()

    def Enter_Username_for_Search(self,username):
        self.wait.until(EC.visibility_of_element_located(self.Text_Search_Username_Xpath)).send_keys(username)

    def Enter_NewUsername(self,newusername):
        username =self.wait.until(EC.visibility_of_element_located(self.Text_Username_Xpath))
        username.clear()
        username.send_keys(newusername)

    def Enter_NewPassword(self,newpassword):
        password = self.wait.until(EC.visibility_of_element_located(self.Text_Password_Xpath))
        password.clear()
        password.send_keys(newpassword)
    def Clickon_Search(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_Search_Button_Xpath)).click()

    def Clickon_SaveChanges(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_Search_Button_Xpath))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(*UserMgmt_Class.Clickon_SaveChnages_Button_Xpath).click()
    def Validate_EditUser(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Success_Validate_Xpath))
            print("UserUpdatedSucessfully")
            return "UserUpdated"
        except:
            print("UserUpdateUnsuccessful")
            return "UserUpdationFailed"

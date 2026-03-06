import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserMgmt_Class:
    clickon_usermgmt_xpath = (By.XPATH,"//a[normalize-space()='User Management']")
    clickon_search_button_xpath=(By.XPATH,"//button[@type='submit']")
    Clickon_savechanges_button_xpath = (By.XPATH,"//button[normalize-space()='Save Changes']")
    text_search_username_xpath = (By.ID,"searchUsername")
    text_username_xpath = (By.ID,"username")
    text_password_xpath = (By.ID,"password")
    text_email_xpath = (By.ID,"email")
    text_phone_number_xpath =(By.ID,"phone")
    success_validate_xpath = (By.XPATH,"/html/body/div/div[2]")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,40)

    def ClickOn_UserMgmt(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickon_usermgmt_xpath))
        element.click()

    def Enter_Username_for_Search(self,username):
        element = self.wait.until(EC.visibility_of_element_located(self.text_search_username_xpath))
        element.send_keys(username)

    def Enter_NewUsername(self,newusername):
        element =self.wait.until(EC.visibility_of_element_located(self.text_username_xpath))
        element.clear()
        element.send_keys(newusername)

    def Enter_NewPassword(self,newpassword):
        element = self.wait.until(EC.visibility_of_element_located(self.text_password_xpath))
        element.clear()
        element.send_keys(newpassword)
    def Enter_NewEmail(self,newemail):
        element = self.wait.until(EC.visibility_of_element_located(self.text_email_xpath))
        element.clear()
        element.send_keys(newemail)
    def Enter_NewPhoneNumber(self,newphonenumber):
        element = self.wait.until(EC.visibility_of_element_located(self.text_phone_number_xpath))
        element.clear()
        element.send_keys(newphonenumber)
    def Clickon_Search(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickon_search_button_xpath))
        element.click()

    def Clickon_SaveChanges(self):
        element =self.wait.until(EC.visibility_of_element_located(self.clickon_search_button_xpath))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        element.click()
    def Validate_EditUser(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.success_validate_xpath))
            print("UserUpdated Successfully")
            return "Pass"
        except:
            print("UserUpdateUnsuccessful")
            return "Failed"

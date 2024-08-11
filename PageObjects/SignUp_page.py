import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class SignUp_Page_Class:

    Clickon_SignUp_Xpath = (By.XPATH,"//a[normalize-space()='Sign Up']")
    Text_Username_Id= (By.ID,"username")
    Text_Password_Id=(By.ID,"password")
    Text_Email_Id = (By.ID,"email")
    Text_Phone_Id=(By.ID,"phone")
    ClickOn_CreateUser_Xpath=(By.XPATH,"//button[@type='submit']")
    Usercreated_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

    def Clickon_SignUp(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_SignUp_Xpath))
        self.driver.find_element(*SignUp_Page_Class.Clickon_SignUp_Xpath).click()

    def Enter_Username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.Text_Username_Id))
        self.driver.find_element(*SignUp_Page_Class.Text_Username_Id).send_keys(username)

    def Enter_Password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.Text_Password_Id))
        self.driver.find_element(*SignUp_Page_Class.Text_Password_Id).send_keys(password)

    def Enter_Emailid(self,emailid):
        self.wait.until(EC.visibility_of_element_located(self.Text_Email_Id))
        self.driver.find_element(*SignUp_Page_Class.Text_Email_Id).send_keys(emailid)

    def Enter_Phoneno(self,phoneno):
        self.wait.until(EC.visibility_of_element_located(self.Text_Phone_Id))
        self.driver.find_element(*SignUp_Page_Class.Text_Phone_Id).send_keys(phoneno)

    def CLickon_CreateUser(self):
        self.wait.until(EC.visibility_of_element_located(self.ClickOn_CreateUser_Xpath))
        self.driver.find_element(*SignUp_Page_Class.ClickOn_CreateUser_Xpath).click()

    time.sleep(2)
    def Validate_UserCreated(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Usercreated_Xpath))
            Success_message = self.driver.find_element(*SignUp_Page_Class.Usercreated_Xpath)

            if Success_message.text=="User created successfully":
                return "SignUpPass"
        except:
            print("user Creation Unsucessful")
            return "SignUpFail"


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.common.by import By
class User_Signin_Class:

    CLickOn_Login_Option_Xpath=(By.XPATH,"/html[1]/body[1]/div[1]/nav[1]/ul[1]/li[1]/a[1]")
    Text_Username_Id=(By.ID, 'username')
    Text_Password_Id=(By.ID,"password")
    CLickOn_LogIn_Button_Xpath = (By.XPATH,"//button[@type='submit']")
    Success_login_Xpath=(By.XPATH,"/html/body/div/h2")
    Clickon_Logout_button_Xpath=(By.XPATH,"//a[normalize-space()='Logout']")
    Success_logout_Xpath = (By.XPATH , "//h2[normalize-space()='Login']")
    def __init__(self,driver):

        self.driver = driver
        self.wait =WebDriverWait(self.driver,5)

    def ClickOn_Login_Option(self):
        self.wait.until(EC.visibility_of_element_located(self.CLickOn_Login_Option_Xpath)).click()


    def Enter_Username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.Text_Username_Id)).send_keys(username)


    def Enter_Password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.Text_Password_Id)).send_keys(password)


    def CLickOn_LogIn_Button(self):
        self.wait.until(EC.visibility_of_element_located(self.CLickOn_LogIn_Button_Xpath)).click()

    def Validate_Login(self):
        success =self.wait.until(EC.visibility_of_element_located(self.Success_login_Xpath)).text
        if success == "Dashboard":
            return "Login_pass"
        else:
            return "Login_fail"

    def ClickOn_Logout(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_Logout_button_Xpath)).click()


    def Validate_Logout(self):
        try:
            success_mess =self.wait.until( EC.visibility_of_element_located(self.Success_logout_Xpath)).text
            return success_mess
        except:
                pass
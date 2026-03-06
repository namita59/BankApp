
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.common.by import By
class User_Signin_Class:

    clickOn_login_link_xpath=(By.XPATH,"//a[contains(text(),'Login')]")
    text_username_id=(By.ID, 'username')
    text_password_id=(By.ID,"password")
    clickOn_login_button_xpath = (By.ID,"loginButton")
    success_login_xpath=(By.XPATH,"/html/body/div/h2")
    clickOn_logout_button_xpath=(By.XPATH,"//a[normalize-space()='Logout']")
    success_logout_xpath = (By.ID, "loginHeading")
    def __init__(self,driver):
        self.driver = driver
        self.wait =WebDriverWait(self.driver,5)

    def ClickOn_Login_Option(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickOn_login_link_xpath))
        element.click()


    def Enter_Username(self,username):
        element = self.wait.until(EC.visibility_of_element_located(self.text_username_id))
        element.send_keys(username)


    def Enter_Password(self,password):
        element = self.wait.until(EC.visibility_of_element_located(self.text_password_id))
        element.send_keys(password)


    def CLickOn_LogIn_Button(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickOn_login_button_xpath))
        element.click()

    def Validate_Login(self):
        success =self.wait.until(EC.visibility_of_element_located(self.success_login_xpath)).text
        if success == "Dashboard":
            return "Login_pass"
        else:
            return "Login_fail"

    def ClickOn_Logout(self):
        self.wait.until(EC.visibility_of_element_located(self.clickOn_logout_button_xpath)).click()

    def Validate_Logout(self):
        try:
            self.wait.until( EC.visibility_of_element_located(self.success_logout_xpath))
            return "Logout_pass"
        except:
            return "Logout_fail"
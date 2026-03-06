from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Cust_Mgmt_Create_Class:

    # ClickOn_ViewallUser_Xpath = (By.XPATH,"//a[normalize-space()='View All Users']")
    # UserId_to_Cust_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]")
    clickon_CustMgmt_Xpath =(By.XPATH,"//a[normalize-space()='Customer Management']")
    clickon_CreateCust_link_Xpath  =(By.XPATH,"//a[normalize-space()='Create Customer']")
    text_UserID_Xpath = (By.ID,"userId")
    text_FirstName_Xpath = (By.ID,"firstName")
    text_LastName_Xpath = (By.ID,"lastName")
    text_Dob_Xpath = (By.ID,"dateOfBirth")
    text_Add_Xpath = (By.ID,"address")
    text_City_Xpath = (By.ID,"city")
    text_State_Xpath =(By.ID,"state")
    text_Zipcode_Xpath = (By.ID,"zipCode")
    clickon_CreateCust_Button_Xpath = (By.ID,"createCustomerBtn")
    success_Message_Xpath = (By.XPATH,"//div[@class='success-message']")

    def __init__(self,driver):
        self.driver =driver
        self.wait = WebDriverWait(self.driver,5)

    # def ClickOn_ViewAlluser(self):
    #     self.wait.until(EC.visibility_of_element_located(self.ClickOn_ViewallUser_Xpath)).click()
    #
    # def ClickOn_to_getUserid(self):
    #     self.userid =self.wait.until(EC.visibility_of_element_located(self.UserId_to_Cust_Xpath)).text
    #     return self.userid

    def ClickOn_CustMgmt_link(self):
        element = self.wait.until(EC.element_to_be_clickable(self.clickon_CustMgmt_Xpath))
        element.click()


    def Clickon_CreateCust_link(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickon_CreateCust_link_Xpath))
        element.click()


    def Enter_Firstname(self,firstname):
        element = self.wait.until(EC.visibility_of_element_located(self.text_FirstName_Xpath))
        element.send_keys(firstname)


    def Enter_Lastname(self,lastname):
        element = self.wait.until(EC.visibility_of_element_located(self.text_LastName_Xpath))
        element.send_keys(lastname)

    def Enter_UserId(self,userid):
        element = self.wait.until(EC.visibility_of_element_located(self.text_UserID_Xpath))
        element.send_keys(userid)

    def Enter_Dob(self,DOB):
        element = self.wait.until(EC.visibility_of_element_located(self.text_Dob_Xpath))
        self.driver.execute_script("arguments[0].value = arguments[1];", element, DOB)

    def Enter_Add(self,address):
        element = self.wait.until(EC.visibility_of_element_located(self.text_Add_Xpath))
        element.send_keys(address)

    def Enter_City(self,city):
        element = self.wait.until(EC.visibility_of_element_located(self.text_City_Xpath))
        element.send_keys(city)

    def Enter_State(self,state):
        element = self.wait.until(EC.visibility_of_element_located(self.text_State_Xpath))
        element.send_keys(state)

    def Enter_Zipcd(self,zipcode):
        element = self.wait.until(EC.visibility_of_element_located(self.text_Zipcode_Xpath))
        element.send_keys(zipcode)

    def Clickon_Create_Cust_button(self):
        element = self.wait.until(EC.visibility_of_element_located(self.clickon_CreateCust_Button_Xpath))
        element.click()

    def Validate_Cust_Created(self):
        try:
            success = self.wait.until(EC.visibility_of_element_located(self.success_Message_Xpath)).text
            return success
        except:
            return "UnabletoCreatedCustomer"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Cust_Mgmt_Create_Class:

    # ClickOn_ViewallUser_Xpath = (By.XPATH,"//a[normalize-space()='View All Users']")
    # UserId_to_Cust_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]")
    Clickon_CustMgmt_Xpath =(By.XPATH,"//a[normalize-space()='Customer Management']")
    Clickon_CreateCust_link_Xpath =(By.XPATH,"//a[normalize-space()='Create Customer']")
    Text_UserID_Xpath = (By.XPATH,"//input[@id='userId']")
    Text_FirstName_Xpath = (By.XPATH,"//input[@id='firstName']")
    Text_LastName_Xpath = (By.XPATH,"//input[@id='lastName']")
    Text_Dob_Xpath = (By.XPATH,"//input[@id='dateOfBirth']")
    Text_Add_Xpath = (By.XPATH,"//input[@id='address']")
    Text_City_Xpath = (By.XPATH,"//input[@id='city']")
    Text_State_Xpath =(By.XPATH,"//input[@id='state']")
    Text_Zipcode_Xpath = (By.XPATH,"//input[@id='zipCode']")
    Clickon_CreateCust_Button_Xpath = (By.XPATH,"//button[@type='submit']")
    Success_Message_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]")

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
        self.wait.until(EC.element_to_be_clickable(self.Clickon_CustMgmt_Xpath)).click()


    def Clickon_CreateCust_link(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_CreateCust_link_Xpath)).click()


    def Enter_Firstname(self,firstname):
        self.wait.until(EC.visibility_of_element_located(self.Text_FirstName_Xpath)).send_keys(firstname)


    def Enter_Lastname(self,lastname):
        self.wait.until(EC.visibility_of_element_located(self.Text_LastName_Xpath)).send_keys(lastname)

    def Enter_UserId(self,userid):
        self.wait.until(EC.visibility_of_element_located(self.Text_UserID_Xpath)).send_keys(userid)

    def Enter_Dob(self,DOB):
        self.wait.until(EC.visibility_of_element_located(self.Text_Dob_Xpath)).send_keys(DOB)

    def Enter_Add(self,address):
        self.wait.until(EC.visibility_of_element_located(self.Text_Add_Xpath)).send_keys(address)

    def Enter_City(self,city):
        self.wait.until(EC.visibility_of_element_located(self.Text_City_Xpath)).send_keys(city)

    def Enter_State(self,state):
        self.wait.until(EC.visibility_of_element_located(self.Text_State_Xpath)).send_keys(state)

    def Enter_Zipcd(self,zipcode):
        self.wait.until(EC.visibility_of_element_located(self.Text_Zipcode_Xpath)).send_keys(zipcode)

    def Clickon_Create_Cust_button(self):
        self.wait.until(EC.visibility_of_element_located(self.Clickon_CreateCust_Button_Xpath)).click()

    def Validate_Cust_Created(self):
        try:
            Success = self.wait.until(EC.visibility_of_element_located(self.Success_Message_Xpath)).text
            return Success
        except:
            return "UnabletoCreatedCustomer"
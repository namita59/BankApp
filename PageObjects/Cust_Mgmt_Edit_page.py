
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Cust_Mgmt_Edit_Class:
    Text_Custid_Xpath = (By.XPATH , "//input[@id='customerId']")
    ClickOn_Search_Cust_Xpath=(By.XPATH , "/html[1]/body[1]/div[1]/form[1]/button[1]")
    Text_UserId_Xpath = (By.XPATH , "//input[@id='userId']")
    Text_FirstName_Xpath =(By.XPATH , "//input[@id='firstName']")
    Text_LastName_Xpath = (By.XPATH , "//input[@id='lastName']")
    Text_Dob_Xpath = (By.XPATH , "//input[@id='dateOfBirth']")
    Clickon_CustMgmt_Xpath = (By.XPATH , "//a[normalize-space()='Customer Management']")
    ClickOn_Save_Xpath = (By.XPATH , "//button[normalize-space()='Save Changes']")
    ClickOn_Delte_Xpath =(By.XPATH , "//button[normalize-space()='Delete Customer']")
    Edit_Success_Messgae_Xpath = (By.XPATH , "//div[@class='success-message']")
    Delete_Success_Message_Xapth = (By.XPATH , "/html[1]/body[1]/div[1]/div[2]")

    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver , 20)

    def ClickOn_CustMgmt_link(self):
        self.wait.until(EC.element_to_be_clickable(self.Clickon_CustMgmt_Xpath)).click()

    def Enter_Custid(self , customerid):
        self.wait.until(EC.visibility_of_element_located(self.Text_Custid_Xpath)).send_keys(customerid)

    def ClickOn_Search_Button(self):
        self.wait.until(EC.element_to_be_clickable(self.ClickOn_Search_Cust_Xpath)).click()

    def Enter_Userid(self , newuserid):
        self.userid = self.wait.until(EC.visibility_of_element_located(self.Text_UserId_Xpath))
        self.userid.clear()
        self.userid.send_keys(newuserid)

    def Enter_FirstName(self , firstname):
        self.Firstname = self.wait.until(EC.visibility_of_element_located(self.Text_FirstName_Xpath))
        self.Firstname.clear()
        self.Firstname.send_keys(firstname)

    def Enter_LastName(self , lastname):
        Lastname = self.wait.until(EC.visibility_of_element_located(self.Text_LastName_Xpath))
        Lastname.clear()
        Lastname.send_keys(lastname)

    def Enter_DateOfBirth(self , dob):
        DateOfBirth = self.wait.until(EC.visibility_of_element_located(self.Text_Dob_Xpath))
        DateOfBirth.clear()
        DateOfBirth.send_keys(dob)

    def ClickOn_Save_Button(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.wait.until(EC.visibility_of_element_located(self.ClickOn_Save_Xpath)).click()

    def ClickOn_Delete_Button(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.ClickOn_Delte_Xpath)).click()

    def Validate_Cust_Edit(self):
        try :
            SuccessMessage = self.wait.until(EC.visibility_of_element_located(self.Edit_Success_Messgae_Xpath)).text
            print(SuccessMessage)
            return SuccessMessage
        except:
            print("Unable to Edit Customer")
            return "Unable to Edit Customer"

    def Validate_Cust_Delete(self):
        try:
            SuccessMessage = self.wait.until(EC.visibility_of_element_located(self.Delete_Success_Message_Xapth)).text
            print(SuccessMessage)
            return SuccessMessage
        except:
            print("Unable to Delete Customer")
            return "UnabletoDeleteCustomer"


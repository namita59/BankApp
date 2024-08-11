from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Account_Mgmt_Create_Page:
    ClickOn_Acc_Mgmt_Link_Xpath = (By.XPATH , "//a[normalize-space()='Account Management']")
    ClickOn_Create_Acc_Link_Xpath = (By.XPATH , "//a[normalize-space()='Create Account']")
    Text_CustID_Xpath = (By.XPATH , "//input[@id='customerId']")
    DropDown_Acc_Type_Xpath = (By.XPATH , "//select[@id='accountTypeId']")
    Text_Balance_Xpath = (By.XPATH , "//input[@id='balance']")
    ClickOn_Create_ACC_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    Success_Message_Xpath = (By.XPATH , "//div[@class='success-message']")

    def __init__(self,driver):
        self.driver = driver

    def ClickOn_Acc_Mgmt(self):
        self.driver.find_element(*Account_Mgmt_Create_Page.ClickOn_Acc_Mgmt_Link_Xpath).click()

    def ClickOn_Create_Acc_Link(self):
        self.driver.find_element(*Account_Mgmt_Create_Page.ClickOn_Create_Acc_Link_Xpath).click()

    def Enter_CustID(self,customerid):
        self.driver.find_element(*Account_Mgmt_Create_Page.Text_CustID_Xpath).send_keys(customerid)

    def DropDown_Acc_Type(self,account_type):
        Acc_Type = Select(self.driver.find_element(*Account_Mgmt_Create_Page.DropDown_Acc_Type_Xpath))
        self.type = account_type
        if self.type=="Saving Account":
            Acc_Type.select_by_visible_text('Saving Account')
        else :
            Acc_Type.select_by_visible_text('Current Account')

    def Enter_Balance(self,balance):
        self.driver.find_element(*Account_Mgmt_Create_Page.Text_Balance_Xpath).send_keys(balance)

    def ClickOn_Create_Acc_Button(self):
        self.driver.find_element(*Account_Mgmt_Create_Page.ClickOn_Create_ACC_Button_Xpath).click()

    def Validate_Create_Acc(self):
        try:
            success_mess = self.driver.find_element(*Account_Mgmt_Create_Page.Success_Message_Xpath).text
            return success_mess
        except:
            pass

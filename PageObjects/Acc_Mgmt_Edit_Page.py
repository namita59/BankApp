from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Acc_Mgmt_to_Edit_Page:
    ClickOn_Acc_Mgmt_link_Xpath = (By.XPATH , "//a[normalize-space()='Account Management']")
    Text_AccId_Xpath = (By.XPATH , "//input[@id='accountId']")
    ClickOn_SearchAcc_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    ClickOn_Edit_Button_Xpath = (By.XPATH , "//a[@class='btn']")
    DropDown_Acc_Type_Xpath = (By.XPATH, "//select[@id='accountTypeId']")
    Text_Balance_Xpath = (By.XPATH, "//input[@id='balance']")
    ClickOn_Update_Acc_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    Success_Mess_toUpdate_Xpath = (By.XPATH , "//div[@class='success-message']")
    ClickOn_Delete_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    Suceess_Mess_ToDelete_Xpath = (By.XPATH , "//div[@class='error-message']")

    def __init__(self , driver):
        self.driver = driver

    def ClickOn_Acc_Mgmt_Link(self):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.ClickOn_Acc_Mgmt_link_Xpath).click()

    def Enter_AccountId(self,accountid):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.Text_AccId_Xpath).send_keys(accountid)

    def ClickOn_Search_Acc_Button(self):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.ClickOn_SearchAcc_Button_Xpath).click()

    def ClickOn_Edit_Button(self):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.ClickOn_Edit_Button_Xpath).click()

    def select_DropDown_Acc_Type(self,account_type):
        Acc_Type = Select(self.driver.find_element(*Acc_Mgmt_to_Edit_Page.DropDown_Acc_Type_Xpath))
        self.type = account_type
        if self.type=="Saving Account":
            Acc_Type.select_by_visible_text('Saving Account')
        else :
            Acc_Type.select_by_visible_text('Current Account')

    def Enter_Balance(self,balance):
        Balance =self.driver.find_element(*Acc_Mgmt_to_Edit_Page.Text_Balance_Xpath)
        Balance.clear()
        Balance.send_keys(balance)
    def ClickOn_Update_Account_Button(self):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.ClickOn_Update_Acc_Button_Xpath).click()

    def ClickOn_Delete_Button(self):
        self.driver.find_element(*Acc_Mgmt_to_Edit_Page.ClickOn_Delete_Button_Xpath).click()

    def Validate_Acc_Updated(self):
        try:
            succes_mess = self.driver.find_element(*Acc_Mgmt_to_Edit_Page.Success_Mess_Xpath).text
            return succes_mess
        except:
            pass

    def Validate_Acc_Deleted(self):
        try:
            succ_mess = self.driver.find_element(*Acc_Mgmt_to_Edit_Page.Suceess_Mess_ToDelete_Xpath).text
            return succ_mess
        except:
            pass

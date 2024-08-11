from selenium.webdriver.common.by import By
class Fund_transfer_Edit_page:
    ClickOn_Fund_Tranfer_Mgmt_link_Xpath=(By.XPATH , "//a[normalize-space()='Funds Transfer Management']")
    Text_Transferid_Xpath = (By.XPATH , "//input[@id='transferId']")
    ClickOn_Search_Transfer_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    Text_Amnt_Xpath = (By.XPATH , "//input[@id='amount']")
    Text_Descript_Xpath = (By.XPATH , "//input[@id='description']")
    ClickOn_UpDate_Transfer_Button_Xpath = (By.XPATH , "//button[normalize-space()='Update Transfer']")
    ClickOn_Delete_Transfer_Button_Xpath =(By.XPATH , "//button[normalize-space()='Delete Transfer']")
    Success_msg_Update_Transfer_Xpath =(By.XPATH , "//div[@class='success-message']")
    Success_msg_Delete_Tranfer_Xpath = (By.XPATH , "//pre[normalize-space()='Cannot POST /delete-fundsTransfer']")


    def __init__(self , driver):
        self.driver = driver

    def ClickOn_Fund_Tranfer_Mgmt_link(self):
        self.driver.find_element(*Fund_transfer_Edit_page.ClickOn_Fund_Tranfer_Mgmt_link_Xpath).click()

    def Enter_TranferID(self,tranferid):
        self.driver.find_element(*Fund_transfer_Edit_page.Text_Transferid_Xpath).send_keys(tranferid)

    def ClickOn_Search_Transfer_Button(self):
        self.driver.find_element(*Fund_transfer_Edit_page.ClickOn_Search_Transfer_Button_Xpath).click()

    def Enter_Amnt(self , amount):
        self.driver.find_element(*Fund_transfer_Edit_page.Text_Amnt_Xpath).send_keys(amount)

    def Enter_Descript(self,description):
        self.driver.find_element(*Fund_transfer_Edit_page.Text_Descript_Xpath).send_keys(description)

    def ClickOn_UpDate_Transfer_Button(self):
        self.driver.find_element(*Fund_transfer_Edit_page.ClickOn_UpDate_Transfer_Button_Xpath).click()

    def ClickOn_Delete_Transfer_Button(self):
        self.driver.find_element(*Fund_transfer_Edit_page.ClickOn_Delete_Transfer_Button_Xpath).click()


    def Validate_Update_Transfer(self):
        try:
            success_msg = self.driver.find_element(*Fund_transfer_Edit_page.Success_msg_Update_Transfer_Xpath).text
            return success_msg
        except:
            pass

    def Validate_Delete_Transfer(self):
        try:
            success_msg = self.driver.find_element(*Fund_transfer_Edit_page.Success_msg_Delete_Tranfer_Xpath).text
            return success_msg
        except:
            pass

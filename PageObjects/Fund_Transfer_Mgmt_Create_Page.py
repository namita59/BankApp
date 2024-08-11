from selenium.webdriver.common.by import By

class Fund_Transfer_Mgmt_To_Create_Page:
    ClickOn_Fund_Transer_Mgmt_Xapth = (By.XPATH,"//a[normalize-space()='Funds Transfer Management']")
    ClickOn_Create_Transfer_Xpath  = (By.XPATH , "//a[normalize-space()='Create Transfer']")
    Text_From_AccId_Xpath = (By.XPATH , "//input[@id='fromAccountId']")
    Text_To_AccId_Xpath = (By.XPATH , "//input[@id='toAccountId']")
    Text_Amnt_Xpath = (By.XPATH , "//input[@id='amount']")
    Text_Descrip_Xpath = (By.XPATH , "//input[@id='description']")
    ClickOn_Tansfer_Fund_Button_Xpath = (By.XPATH , "//button[@type='submit']")
    Success_Msg_Xpath = (By.XPATH ,"//div[@class='success-message']")

    def __init__(self,driver):
        self.driver = driver

    def ClickOn_Fund_Transer_Mgmt_Link(self):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.ClickOn_Fund_Transer_Mgmt_Xapth).click()

    def ClickOn_Create_Transfer_Link(self):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.ClickOn_Create_Transfer_Xpath).click()

    def Enter_From_AccId(self,FromAcc_id):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.Text_From_AccId_Xpath).send_keys(FromAcc_id)

    def Enter_To_AccId(self,ToAcc_id):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.Text_To_AccId_Xpath).send_keys(ToAcc_id)

    def Enter_Amnt(self,amount):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.Text_Amnt_Xpath).send_keys(amount)

    def Enter_Descript(self,description):
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.Text_Descrip_Xpath).send_keys(description)

    def ClickOn_Transfer_Fund_Button(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.ClickOn_Tansfer_Fund_Button_Xpath).click()

    def Validate_Fund_Transfer(self):
        try:
            sucess_msg = self.driver.find_element(*Fund_Transfer_Mgmt_To_Create_Page.Success_Msg_Xpath).text
            return sucess_msg
        except:
            pass

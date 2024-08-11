from selenium.webdriver.common.by import By
class Bill_Pay_page:
   ClickOn_Bill_Payment_Link_Xpath = (By.XPATH , "//a[normalize-space()='Bill Payments']")
   Text_AccountId_Xpath = (By.XPATH , "//input[@id='accountId']")
   Text_Payee_Name =(By.XPATH , "//input[@id='payeeName']")
   Text_Amnt_Xpath = (By.XPATH , "//input[@id='amount']")
   Text_Desciption =(By.XPATH , "//input[@id='description']")
   ClickOn_PayBill_Button_Xpath = (By.XPATH , "//button[@type='submit']")
   Success_Msg_Xpath = (By.XPATH , "//div[@class='success-message']")

   def __init__(self,driver):
       self.driver = driver

   def ClickOn_BillPayment_LinK(self):
       self.driver.find_element(*Bill_Pay_page.ClickOn_Bill_Payment_Link_Xpath).click()

   def Enter_AccountID(self, accountid):
       self.driver.find_element(*Bill_Pay_page.Text_AccountId_Xpath).send_keys(accountid)

   def Enter_PayeeName(self, Payeename):
       self.driver.find_element(*Bill_Pay_page.Text_Payee_Name).send_keys(Payeename)

   def Enter_Amount(self, amount):
       self.driver.find_element(*Bill_Pay_page.Text_Amnt_Xpath).send_keys(amount)

   def Enter_Descript(self, description):
       self.driver.find_element(*Bill_Pay_page.Text_Desciption).send_keys(description)

   def ClickOn_PayBill_Button(self):
       self.driver.find_element(*Bill_Pay_page.ClickOn_PayBill_Button_Xpath).click()

   def Validate_Billpay(self):
       try:
           success_msg = self.driver.find_element(*Bill_Pay_page.Success_Msg_Xpath).text
           return success_msg
       except:
           pass



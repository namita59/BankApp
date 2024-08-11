
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Search_User_Page:
    Click_On_User_Mgmt_Xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    Click_On_ViewAllUsers_Xpath = (By.XPATH, "//a[normalize-space()='View All Users']")
    Search_User_Xpath = (By.XPATH, "/html/body/div/table/tbody/tr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def ClickOn_User_Mgmt(self):
        self.wait.until(EC.visibility_of_element_located(self.Click_On_User_Mgmt_Xpath)).click()

    def Click_On_ViewAllUsers(self):
        self.wait.until(EC.visibility_of_element_located(self.Click_On_ViewAllUsers_Xpath)).click()

    def Search_User(self):
        user_ids = []
        # Find all rows in the table
        rows = self.driver.find_elements(*self.Search_User_Xpath)
        # Iterate through each row and get the first cell
        for row in rows:
            first_cell = row.find_element(By.XPATH, "./td[1]").text
            user_ids.append(first_cell)
        return user_ids
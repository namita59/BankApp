
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Search_User_Page:
    click_on_user_mgmt_xpath = (By.XPATH, "//a[normalize-space()='User Management']")
    click_on_view_all_users_xpath = (By.XPATH, "//a[normalize-space()='View All Users']")
    search_user_xpath = (By.XPATH, "/html/body/div/table/tbody/tr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def ClickOn_User_Mgmt(self):
        self.wait.until(EC.visibility_of_element_located(self.click_on_user_mgmt_xpath)).click()

    def Click_On_ViewAllUsers(self):
        self.wait.until(EC.visibility_of_element_located(self.click_on_view_all_users_xpath)).click()

    def ValidateSearch_User(self, user_id):

        rows = self.driver.find_elements(*self.search_user_xpath)
        # Iterate through each row and get the first cell
        for row in rows:
            first_cell = row.find_element(By.XPATH, "./td[1]").text
            if first_cell == user_id:
                return True
        return False
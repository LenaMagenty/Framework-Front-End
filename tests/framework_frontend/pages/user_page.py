from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserPage(BasePage):
    PAGE_NAME = 'User Page'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(),'Not Found')]")

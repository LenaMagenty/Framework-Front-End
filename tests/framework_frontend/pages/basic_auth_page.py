from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']"
                                    "//p[contains(text(),'Congratulations!')]")
    PAGE_NAME = "BasicAuthPage"

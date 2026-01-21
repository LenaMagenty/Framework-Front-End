from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewWindowPage(BasePage):
    PAGE_NAME = 'NewWindowPage'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h3[contains(text(),'New Window')]")

    def get_title(self) -> str:
        return self.browser.driver.title

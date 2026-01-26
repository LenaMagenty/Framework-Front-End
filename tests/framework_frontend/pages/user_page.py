from pages.base_page import BasePage
from elements.web_element import WebElement


class UserPage(BasePage):
    PAGE_NAME = 'UserPage'

    UNIQUE_ELEMENT_LOC = "//*[contains(text(),'Not Found')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Not Found text'
        )

from pages.base_page import BasePage
from elements.web_element import WebElement


class NewWindowPage(BasePage):
    PAGE_NAME = 'NewWindowPage'

    UNIQUE_ELEMENT_LOC = "//h3[contains(text(),'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='New Window header'
        )

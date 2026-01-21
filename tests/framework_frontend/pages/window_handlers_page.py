from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement


class WindowHandlersPage(BasePage):
    PAGE_NAME = 'WindowHandlersPage'

    CLICK_HERE_LINK_LOC = (By.XPATH, "//a[contains(text(),'Click Here')]")

    UNIQUE_ELEMENT_LOC = CLICK_HERE_LINK_LOC

    def click_click_here_link(self) -> None:
        BaseElement(
            browser=self.browser,
            locator=self.CLICK_HERE_LINK_LOC,
            description="Click Here link"
        ).click()

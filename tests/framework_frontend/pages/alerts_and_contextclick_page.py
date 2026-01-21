from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement


class AlertsContextCLickPage(BasePage):
    PAGE_NAME = 'AlertsContextCLickPage'
    AREA_LOC = (By.ID, 'hot-spot')
    UNIQUE_ELEMENT_LOC = AREA_LOC


    def context_click_area(self) -> None:
        area = BaseElement(
            browser=self.browser,
            locator=self.AREA_LOC,
            description='Context click area'
        ).wait_for_presence()

        self.browser.context_click(area)


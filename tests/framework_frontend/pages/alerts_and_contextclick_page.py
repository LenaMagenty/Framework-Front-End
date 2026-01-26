from pages.base_page import BasePage
from elements.web_element import WebElement


class AlertsContextClickPage(BasePage):
    PAGE_NAME = 'AlertsContextClickPage'

    AREA_LOC = 'hot-spot'
    UNIQUE_ELEMENT_LOC = AREA_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.area = WebElement(
            browser=self.browser,
            locator=self.AREA_LOC,
            description='Context click area'
        )

        self.unique_element = self.area

    def context_click_area(self) -> None:
        self.area.context_click()

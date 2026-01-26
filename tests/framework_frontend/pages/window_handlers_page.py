from pages.base_page import BasePage
from elements.button import Button


class WindowHandlersPage(BasePage):
    PAGE_NAME = 'WindowHandlersPage'

    CLICK_HERE_LINK_LOC = "//a[contains(text(),'Click Here')]"
    UNIQUE_ELEMENT_LOC = CLICK_HERE_LINK_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.click_here_link = Button(
            browser=self.browser,
            locator=self.CLICK_HERE_LINK_LOC,
            description='Click Here link'
        )
        self.unique_element = self.click_here_link

    def click_click_here_link(self) -> None:
        self.click_here_link.click()

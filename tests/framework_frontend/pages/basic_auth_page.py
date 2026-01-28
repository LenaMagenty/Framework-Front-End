from pages.base_page import BasePage
from elements.label import Label


class BasicAuthPage(BasePage):
    PAGE_NAME = "BasicAuthPage"

    UNIQUE_ELEMENT_LOC = "//*[@id='content']//p[contains(text(),'Congratulations!')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.success_message = Label(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description="Basic auth success message"
        )
        self.unique_element = self.success_message

    def get_success_message_text(self) -> str:
        return self.success_message.get_text()

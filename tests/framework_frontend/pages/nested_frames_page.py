from pages.base_page import BasePage
from elements.web_element import WebElement
from logger.logger import Logger


class NestedFramesPage(BasePage):
    PAGE_NAME = 'NestedFramesPage'

    PARENT_IFRAME_LOC = 'frame1'  # ID
    PARENT_TEXT_LOC = "//body[contains(normalize-space(.), 'Parent frame')]"

    CHILD_IFRAME_LOC = "//iframe[@srcdoc]"
    CHILD_TEXT_LOC = "//p[normalize-space()='Child Iframe']"

    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//h1[normalize-space()='Nested Frames']"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Nested Frames header'
        )

        self.parent_iframe = WebElement(
            browser=self.browser,
            locator=self.PARENT_IFRAME_LOC,
            description='Parent iframe'
        )
        self.parent_text = WebElement(
            browser=self.browser,
            locator=self.PARENT_TEXT_LOC,
            description='Parent frame text'
        )

        self.child_iframe = WebElement(
            browser=self.browser,
            locator=self.CHILD_IFRAME_LOC,
            description='Child iframe'
        )
        self.child_text = WebElement(
            browser=self.browser,
            locator=self.CHILD_TEXT_LOC,
            description='Child iframe text'
        )

    def check_parent_text_visible(self) -> None:
        Logger.info(f'{self}: check Parent frame text is visible')

        self.browser.switch_to_frame(self.parent_iframe)
        self.parent_text.wait_for_visible()
        self.browser.switch_to_default_content()

    def check_child_text_visible(self) -> None:
        Logger.info(f'{self}: check Child iframe text is visible')

        self.browser.switch_to_frame(self.parent_iframe)
        self.browser.switch_to_frame(self.child_iframe)

        self.child_text.wait_for_visible()
        self.browser.switch_to_default_content()

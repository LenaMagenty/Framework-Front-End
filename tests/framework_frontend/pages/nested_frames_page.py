from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement
from logger.logger import Logger


class NestedFramesPage(BasePage):
    PAGE_NAME = 'NestedFramesPage'

    PARENT_IFRAME_LOC = (By.ID, 'frame1')
    PARENT_TEXT_LOC = (By.XPATH, "//body[contains(normalize-space(.), 'Parent frame')]")
    CHILD_IFRAME_LOC = (
        By.XPATH,
        "//iframe[@srcdoc='<p>Child Iframe</p>']"
    )
    CHILD_TEXT_LOC = (
        By.XPATH,
        "//p[normalize-space()='Child Iframe']"
    )

    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@id='framesWrapper']//h1[normalize-space()='Nested Frames']"
    )

    def __init__(self, browser):
        super().__init__(browser)

        self.parent_iframe = BaseElement(self.browser, self.PARENT_IFRAME_LOC, 'Parent iframe')
        self.parent_text = BaseElement(self.browser, self.PARENT_TEXT_LOC, 'Parent frame text')

        self.child_iframe = BaseElement(self.browser, self.CHILD_IFRAME_LOC, 'Child iframe')
        self.child_text = BaseElement(self.browser, self.CHILD_TEXT_LOC, 'Child iframe text')

    def parent_text_is_visible(self) -> None:
        Logger.info(f'{self}: check Parent frame text is visible')

        self.browser.switch_to_frame(self.parent_iframe)
        self.parent_text.wait_for_visible()
        self.browser.switch_to_default_content()

    def child_text_is_visible(self) -> None:
        Logger.info(f'{self}: check Child Iframe text is visible')

        self.browser.switch_to_frame(self.parent_iframe)

        iframe_web_element = self.child_iframe.wait_for_presence()
        self.browser.switch_to_iframe(iframe_web_element)
        self.child_text.wait_for_visible()
        self.browser.switch_to_default_content()

from browser.browser import Browser
from logger.logger import Logger
from elements.base_element import BaseElement


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    PAGE_NAME = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.unique_element = BaseElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description=f'{self.PAGE_NAME} unique element')

    def wait_for_open(self) -> None:
        Logger.info(f'{self}: wait for open')
        self.unique_element.wait_for_presence()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self.PAGE_NAME}]'

    def __repr__(self) -> str:
        return str(self)

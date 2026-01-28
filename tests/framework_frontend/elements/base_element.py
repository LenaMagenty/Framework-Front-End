from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

from browser.browser import Browser
from logger.logger import Logger


class BaseElement:
    def __init__(
            self,
            browser: Browser,
            locator: str | tuple,
            description: str = None
    ):
        self.browser = browser

        if isinstance(locator, str):
            if "/" in locator:
                self.locator = (By.XPATH, locator)
            else:
                self.locator = (By.ID, locator)
        else:
            self.locator = locator

        self.description = description if description else str(locator)
        self.waits = self.browser.waits

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def wait_for_presence(self):
        return self.waits.wait_for_presence(self.locator)

    def wait_for_clickable(self):
        return self.waits.wait_for_clickable(self.locator)

    def wait_for_visible(self):
        return self.waits.wait_for_visible(self.locator)

    def is_exists(self) -> bool:
        return self.waits.is_present(self.locator)

    def is_visible(self) -> bool:
        return self.waits.is_visible(self.locator)

    def click(self) -> None:
        element = self.wait_for_clickable()
        Logger.info(f"{self}: click")
        try:
            element.click()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_click(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();",
            element
        )

    def get_text(self) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get text")
        try:
            text = element.text
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: text = \"{text}\"")
        return text

    def get_attribute(self, name: str) -> str:
        element = self.wait_for_presence()
        Logger.info(f"{self}: get attribute \"{name}\"")
        try:
            value = element.get_attribute(name)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        Logger.info(f"{self}: attribute {name} = \"{value}\"")
        return value

    def move_to_element(self) -> None:
        Logger.info(f"{self}: move to element")
        self.browser.actions._move_to_element(self)

    def context_click(self) -> None:
        Logger.info(f"{self}: context click")
        self.browser.actions._context_click(self)

    def click_and_hold(self) -> None:
        Logger.info(f"{self}: click and hold")
        self.browser.actions._click_and_hold(self)

    def drag_and_drop_to(self, target) -> None:
        Logger.info(f"{self}: drag and drop to {target}")
        self.browser.actions._drag_and_drop(self, target)

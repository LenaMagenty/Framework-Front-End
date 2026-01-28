from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger.logger import Logger


class Waits:
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(browser.driver, browser.default_timeout)

    def wait_for_presence(self, locator):
        Logger.info(f'{self}: wait for presence {locator}')
        try:
            return self._wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            raise

    def wait_for_visible(self, locator):
        Logger.info(f'{self}: wait for visible {locator}')
        try:
            return self._wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            raise

    def wait_for_clickable(self, locator):
        Logger.info(f'Waits: wait for clickable {locator}')
        return self._wait.until(EC.element_to_be_clickable(locator))

    def is_present(self, locator) -> bool:
        try:
            self.wait_for_presence(locator)
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator) -> bool:
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False

    def __str__(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return str(self)

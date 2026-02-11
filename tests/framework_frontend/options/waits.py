from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger.logger import Logger


class Waits:
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(browser.driver, browser.default_timeout)

    def wait_for_presence(self, locator: tuple[str, str]):
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
        Logger.info(f'{self}: wait for clickable {locator}')
        try:
            return self._wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            raise

    def wait_for_frame_and_switch(self, locator: tuple[str, str]):
        Logger.info(f'{self}: wait for frame and switch {locator}')
        try:
            return self._wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            raise

    def is_present(self, locator, timeout: float | None = None) -> bool:
        Logger.info(f'{self}: check present {locator}')
        wait = self._wait if timeout is None else WebDriverWait(self._browser.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            return False

    def is_visible(self, locator) -> bool:
        Logger.info(f'{self}: check visible {locator}')
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            return False

    def is_present_quick(self, locator, timeout: float = 0.3) -> bool:
        Logger.info(f'{self}: check present quick {locator}, timeout={timeout}')
        try:
            WebDriverWait(self._browser.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException as err:
            Logger.error(f'{self}: {err}')
            return False

    def __str__(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return str(self)

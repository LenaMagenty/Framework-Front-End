from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger.logger import Logger


class Waits:
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(
            browser.driver,
            browser.default_timeout
        )

    def wait_for_presence(self, locator):
        Logger.info(f'{self}: wait for presence {locator}')
        return self._wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        Logger.info(f'{self}: wait for clickable {locator}')
        return self._wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        Logger.info(f'{self}: wait for visible {locator}')
        return self._wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert_present(self):
        Logger.info(f'{self}: wait for alert present')
        return self._wait.until(EC.alert_is_present())

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return str(self)

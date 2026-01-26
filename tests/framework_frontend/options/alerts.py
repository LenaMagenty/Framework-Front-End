from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoAlertPresentException

from logger.logger import Logger


class Alerts:
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(
            browser.driver,
            browser.default_timeout
        )

    def _alert(self):
        Logger.info(f'{self}: wait alert present')
        self._wait.until(EC.alert_is_present())
        Logger.info(f'{self}: switch to alert')
        return self._browser.driver.switch_to.alert

    def cancel(self) -> None:
        self._alert().dismiss()

    def confirm(self) -> None:
        self._alert().accept()

    def get_text(self) -> str:
        return self._alert().text

    def send_keys(self, text: str) -> None:
        self._alert().send_keys(text)

    def write_text_and_confirm(self, text: str) -> None:
        alert = self._alert()
        alert.send_keys(text)
        alert.accept()

    def is_present(self) -> bool:
        try:
            self._browser.driver.switch_to.alert.text
            return True
        except NoAlertPresentException:
            return False

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return str(self)

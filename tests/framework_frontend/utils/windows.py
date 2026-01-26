from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Windows:
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(
            browser.driver,
            browser.default_timeout
        )

    def get_current_handle(self) -> str:
        return self._browser.driver.current_window_handle

    def get_all_handles(self) -> list[str]:
        return self._browser.driver.window_handles

    def switch_to(self, handle: str) -> None:
        self._browser.driver.switch_to.window(handle)

    def close_current(self) -> None:
        self._browser.driver.close()

    def wait_new_window(self, old_handles: list[str]) -> str:
        old_set = set(old_handles)

        self._wait.until(
            EC.number_of_windows_to_be(len(old_set) + 1)
        )

        current = set(self._browser.driver.window_handles)
        new_handle = (current - old_set).pop()
        return new_handle

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return str(self)

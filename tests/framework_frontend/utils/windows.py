from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class Windows:
    def __init__(self, driver: WebDriver, timeout: int):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, timeout=timeout)

    def get_current_handle(self) -> str:
        return self._driver.current_window_handle

    def get_all_handles(self) -> list[str]:
        return self._driver.window_handles

    def switch_to(self, handle: str) -> None:
        self._driver.switch_to.window(handle)

    def close_current(self) -> None:
        self._driver.close()

    def wait_new_window(self, old_handles: list[str]) -> str:
        old_set = set(old_handles)

        def _new_handle_appeared(driver) -> str | bool:
            current = set(driver.window_handles)
            diff = current - old_set
            if diff:
                return diff.pop()
            return False

        return self._wait.until(_new_handle_appeared)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return str(self)

import base64
import logging

from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from browser.browser_factory import BrowserFactory, AvailableDriverName
from options.alerts import Alerts
from options.action_chains import ActionChains
from options.waits import Waits
from utils.windows import Windows
from logger.logger import Logger
from config.config_reader import ConfigReader


class Browser:
    def __init__(
            self,
            driver: WebDriver | None = None,
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] | None = None
    ):
        config = ConfigReader()
        timeouts = config.get('timeouts')
        default_timeout = timeouts['default']

        if driver is not None:
            self._driver = driver
        else:
            self._driver = BrowserFactory.get_driver(
                driver_name=driver_name,
                options=options
            )

        self._driver.set_page_load_timeout(timeouts['page_load'])

        self.main_handle = None

        self.waits = Waits(driver=self._driver, timeout=default_timeout)
        self.alerts = Alerts(driver=self._driver, timeout=default_timeout)
        self.actions = ActionChains(driver=self._driver)
        self.windows = Windows(driver=self._driver, timeout=default_timeout)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    @property
    def switch_to(self):
        return self._driver.switch_to

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def get(self, url: str) -> None:
        Logger.info(f'{self}: get "{url}"')
        try:
            self._driver.get(url)
        except WebDriverException as err:
            logging.error(f'{self}: {err}')
            raise
        self.main_handle = self._driver.current_window_handle

    def back(self) -> None:
        Logger.info(f'{self}: back')
        self._driver.back()

    def set_basic_auth(self, username: str, password: str) -> None:
        Logger.info(f'{self}: set basic auth header')
        token = base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')

        self._driver.execute_cdp_cmd('Network.enable', {})
        self._driver.execute_cdp_cmd(
            'Network.setExtraHTTPHeaders',
            {'headers': {'Authorization': f'Basic {token}'}}
        )

    def refresh(self) -> None:
        Logger.info(f'{self}: refresh')
        self._driver.refresh()

    def close(self) -> None:
        Logger.info(
            f'{self}: close window handle = '
            f'"{self._driver.current_window_handle}"'
        )
        self._driver.close()

    def quit(self) -> None:
        Logger.info(f'{self}: quit')
        try:
            self._driver.quit()
        except WebDriverException as err:
            logging.error(f'{self}: {err}')
            raise

    def make_dump(self, file_path: str) -> None:
        Logger.info(f'{self}: make dump "{file_path}"')
        self._driver.save_screenshot(file_path)

    def execute_script(self, script: str, *args):
        Logger.info(f'{self}: execute script = "{script}" with args = "{args}"')
        return self._driver.execute_script(script, *args)

    def confirm_alert(self) -> None:
        Logger.info(f'{self}: confirm alert')
        self.alerts.confirm()

    def cancel_alert(self) -> None:
        Logger.info(f'{self}: cancel alert')
        self.alerts.cancel()

    def get_alert_text(self) -> str:
        Logger.info(f'{self}: get alert text')
        return self.alerts.get_text()

    def send_keys_alert(self, text: str) -> None:
        Logger.info(f'{self}: send keys to alert "{text}"')
        self.alerts.send_keys(text)

    def write_text_and_confirm_alert(self, text: str) -> None:
        Logger.info(f'{self}: write text and confirm alert "{text}"')
        self.alerts.write_text_and_confirm(text)

    def alert_is_present(self) -> bool:
        Logger.info(f'{self}: alert is present')
        return self.alerts.is_present()

    def switch_to_frame(self, frame):
        Logger.info(f'{self}: switch to frame')
        return self.driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_iframe(self, iframe) -> None:
        Logger.info(f'{self}: switch to iframe')
        self.driver.switch_to.frame(iframe)

    def switch_to_default_content(self):
        Logger.info(f'{self}: switch to default content')
        self.driver.switch_to.default_content()

    def drag_and_drop(self, source, target) -> None:
        Logger.info(f'{self}: drag and drop')
        self.actions.drag_and_drop(source, target)

    def drag_by_offset(self, element, x_offset: int, y_offset: int = 0) -> None:
        Logger.info(f'{self}: drag by offset')
        self.actions.drag_by_offset(element, x_offset, y_offset)

    def context_click(self, element) -> None:
        Logger.info(f'{self}: context click')
        self.actions.context_click(element)

    def click_and_hold(self, element) -> None:
        Logger.info(f'{self}: click and hold')
        self.actions.click_and_hold(element)

    def move_to_element(self, element) -> None:
        Logger.info(f'{self}: move to element {element}')
        self.actions.move_to_element(element)

    def get_current_window_handle(self) -> str:
        Logger.info(f'{self}: get current window handle')
        return self.windows.get_current_handle()

    def get_all_window_handles(self) -> list[str]:
        Logger.info(f'{self}: get all window handles')
        return self.windows.get_all_handles()

    def switch_to_window(self, handle: str) -> None:
        Logger.info(f'{self}: switch to window "{handle}"')
        self.windows.switch_to(handle)

    def wait_new_window_handle(self, old_handles: list[str]) -> str:
        Logger.info(f'{self}: wait new window handle')
        return self.windows.wait_new_window(old_handles)

    def close_current_window(self) -> None:
        Logger.info(f'{self}: close current window')
        self.windows.close_current()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self._driver.session_id}]'

    def __repr__(self) -> str:
        return str(self)

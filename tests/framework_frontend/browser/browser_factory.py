import platform
from enum import StrEnum
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from logger.logger import Logger


class AvailableDriverName(StrEnum):
    CHROME = 'chrome'


class BrowserFactory:

    @staticmethod
    def get_driver(
            driver_name: AvailableDriverName = AvailableDriverName.CHROME,
            options: list[str] | None = None
    ) -> WebDriver:

        if options is None:
            options = []

        Logger.info(
            f"Start webdriver '{driver_name}' with options '{options}'"
        )

        if driver_name != AvailableDriverName.CHROME:
            raise NotImplementedError(
                f"Driver '{driver_name}' not implemented."
            )

        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability('pageLoadStrategy', 'eager')

        if platform.system() == "Linux":
            chrome_options.add_argument("--headless=new")

        for option in options:
            chrome_options.add_argument(option)

        return webdriver.Chrome(options=chrome_options)

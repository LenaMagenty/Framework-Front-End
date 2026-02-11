import os
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

        remote_url = os.getenv('SELENIUM_REMOTE_URL')

        Logger.info(
            f"Start webdriver '{driver_name}' with options '{options}'"
        )

        if remote_url:
            Logger.info(
                f"Use remote webdriver. Remote URL: '{remote_url}'"
            )

        if driver_name == AvailableDriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.set_capability('pageLoadStrategy', 'eager')

            for option in options:
                chrome_options.add_argument(option)

            if remote_url:
                driver = webdriver.Remote(
                    command_executor=remote_url,
                    options=chrome_options
                )
            else:
                driver = webdriver.Chrome(options=chrome_options)

        else:
            raise NotImplementedError(
                f"Driver '{driver_name}' not implemented."
            )

        return driver

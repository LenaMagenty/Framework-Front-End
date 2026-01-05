from selenium import webdriver
from tests.test_steam_search.config.config_reader import ConfigReader


class DriverSingleton:
    _driver = None

    @classmethod
    def get_driver(cls):
        config = ConfigReader()
        if cls._driver is None:
            options = webdriver.ChromeOptions()
            for arg in config.get('chrome_options'):
                options.add_argument(arg)
            cls._driver = webdriver.Chrome(options=options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

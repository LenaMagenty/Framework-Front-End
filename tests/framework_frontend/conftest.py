import pytest

from config.config_reader import ConfigReader
from browser.browser import Browser
from browser.browser_factory import BrowserFactory, AvailableDriverName



@pytest.fixture(scope='function')
def config():
    return ConfigReader()


@pytest.fixture
def driver(config):
    driver = BrowserFactory.get_driver(
        driver_name=AvailableDriverName.CHROME,
        options=config.get('chrome_options')
    )
    yield driver
    driver.quit()


@pytest.fixture
def browser(driver):
    return Browser(driver)

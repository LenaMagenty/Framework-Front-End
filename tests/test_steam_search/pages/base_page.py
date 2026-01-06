from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader
from driver.driver import DriverSingleton


class BasePage:
    config = ConfigReader()
    UNIQUE_ELEMENT = None

    def __init__(self):
        self.driver = DriverSingleton.get_driver()
        self.wait = WebDriverWait(self.driver, self.config.get('timeout'))

    def wait_opened(self):
        self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT))

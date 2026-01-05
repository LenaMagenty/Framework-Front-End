from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader


class BasePage:
    config = ConfigReader()
    UNIQUE_ELEMENT = None
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.config.get('timeout'))

    def assert_opened(self):
        assert self.wait.until(EC.visibility_of_element_located(self.UNIQUE_ELEMENT))
        return self

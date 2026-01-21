from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage
from elements.base_element import BaseElement
from logger.logger import Logger


class DynamicContentPage(BasePage):
    PAGE_NAME = 'DynamicContentPage'

    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='example']//h3[normalize-space()='Dynamic Content']"
    )

    IMAGES_LOC = (
        By.XPATH,
        "//div[@id='content']//div[contains(@class,'large-2')]//img"
    )

    def __init__(self, browser):
        super().__init__(browser)

        self.images = BaseElement(
            browser=self.browser,
            locator=self.IMAGES_LOC,
            description='Dynamic content images'
        )

    def get_images_src(self) -> list[str]:
        Logger.info(f'{self}: get images src')
        self.images.wait_for_presence()
        elements = self.browser.driver.find_elements(*self.IMAGES_LOC)
        return [img.get_attribute('src') for img in elements]

    def refresh_until_any_two_images_match(self) -> None:
        Logger.info(f'{self}: refresh until any two images match')

        attempt = 0
        while True:
            attempt += 1
            images_src = self.get_images_src()

            if len(images_src) != len(set(images_src)):
                Logger.info(
                    f'{self}: duplicate images found (attempt={attempt})'
                )
                return

            Logger.info(
                f'{self}: no duplicates yet (attempt={attempt}), refresh'
            )
            self.browser.refresh()
            self.wait_for_open()


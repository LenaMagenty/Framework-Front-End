from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger


class DynamicContentPage(BasePage):
    PAGE_NAME = 'DynamicContentPage'

    UNIQUE_ELEMENT_LOC = "//div[contains(@class,'example')]//h3[normalize-space()='Dynamic Content']"
    IMAGES_LOC = "//*[@id='content']//div[contains(@class,'large-2')]//img"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_header = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Dynamic Content header'
        )
        self.unique_element = self.unique_header

        self.images = MultiWebElement(
            browser=self.browser,
            formattable_xpath=f'({self.IMAGES_LOC})[{{}}]',
            description='Dynamic content image'
        )

    def get_images_src(self) -> list[str]:
        Logger.info(f'{self}: get images src')

        src_list: list[str] = []
        for image in self.images:
            src_list.append(image.get_attribute('src'))

        return src_list

    def refresh_until_any_two_images_match(self) -> None:
        Logger.info(f'{self}: refresh until any two images match')

        attempt = 0
        while True:
            attempt += 1
            images_src = self.get_images_src()

            if len(images_src) != len(set(images_src)):
                Logger.info(f'{self}: duplicate images found (attempt={attempt})')
                return

            Logger.info(f'{self}: no duplicates yet (attempt={attempt}), refresh')
            self.browser.refresh()
            self.wait_for_open()

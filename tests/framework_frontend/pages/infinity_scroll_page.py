from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger


class InfinityScrollPage(BasePage):
    PAGE_NAME = 'InfinityScrollPage'

    PARAGRAPHS_MULTI_WEB_EL_LOC = "//div[{}][contains(@class,'jscroll-added')]//br"

    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='content']//h3[normalize-space()='Infinite Scroll']")

    def __init__(self, browser):
        super().__init__(browser=browser)

        self.paragraphs = MultiWebElement(
            browser=self.browser,
            formattable_xpath=self.PARAGRAPHS_MULTI_WEB_EL_LOC,
            description='Paragraphs'
        )

    def scroll_to_bottom(self) -> None:
        Logger.info(f'{self}: scroll to bottom')
        self.browser.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        )

    def get_paragraphs_count(self) -> int:
        Logger.info(f'{self}: get paragraphs count')

        count = 0
        for _ in self.paragraphs:
            count += 1

        Logger.info(f'{self}: paragraphs count = "{count}"')
        return count

    def wait_next_paragraph(self, expected_index: int) -> None:
        Logger.info(f'{self}: wait paragraph #{expected_index}')

        for index, _ in enumerate(self.paragraphs, start=1):
            if index == expected_index:
                return

    def scroll_until_paragraphs_count(self, target: int) -> None:
        Logger.info(f'{self}: scroll until paragraphs count == {target}')

        # не считаем current вообще
        for expected_index in range(1, target + 1):
            # ждём, что этот индекс существует (если уже есть — пройдёт быстро)
            self.wait_next_paragraph(expected_index)

            # если это не последний — триггерим подгрузку следующего
            if expected_index < target:
                self.scroll_to_bottom()

        Logger.info(f'{self}: reached paragraphs count {target}')

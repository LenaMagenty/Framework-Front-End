from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger


class InfinityScrollPage(BasePage):
    PAGE_NAME = 'InfinityScrollPage'

    UNIQUE_ELEMENT_LOC = "//div[@id='content']//h3[normalize-space()='Infinite Scroll']"
    PARAGRAPHS_LOC = "//div[@id='content']//div[contains(@class,'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser=browser)

        self.unique_header = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Infinite Scroll header'
        )
        self.unique_element = self.unique_header

        self.paragraphs = MultiWebElement(
            browser=self.browser,
            formattable_xpath=f'({self.PARAGRAPHS_LOC})[{{}}]',
            description='Paragraph'
        )

    def scroll_to_bottom(self) -> None:
        Logger.info(f'{self}: scroll to bottom')
        self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

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

        for expected_index in range(1, target + 1):
            self.wait_next_paragraph(expected_index)

            if expected_index < target:
                self.scroll_to_bottom()

        Logger.info(f'{self}: reached paragraphs count {target}')

from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger


class InfinityScrollPage(BasePage):
    PAGE_NAME = 'InfinityScrollPage'

    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3[normalize-space()='Infinite Scroll']"
    PARAGRAPHS_LOC = "//*[@id='content']//div[contains(@class,'jscroll-added')]"

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

    def get_paragraphs_count(self) -> int:
        count = 0
        for _ in self.paragraphs:
            count += 1
        return count

    def scroll_until_paragraphs_count(self, target: int) -> None:
        Logger.info(f'{self}: scroll until paragraphs count == {target}')

        current = self.get_paragraphs_count()
        steps = 0

        while current < target:
            steps += 1

            next_index = current + 1

            self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            self.paragraphs[next_index].wait_for_presence()

            current = self.get_paragraphs_count()
        self.paragraphs[target].wait_for_presence()

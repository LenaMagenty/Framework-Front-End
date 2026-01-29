from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


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
        index = 1

        while True:
            element = self.paragraphs[index]
            if not self.browser.waits.is_present_quick(element.locator, timeout=0.3):
                count = index - 1
                Logger.info(f'{self}: paragraphs count = {count}')
                return count
            index += 1

    def wait_until_paragraph_appears(self, index: int) -> None:
        Logger.info(f'{self}: wait until paragraph #{index} appears')

        wait = WebDriverWait(self.browser.driver, self.browser.default_timeout)

        try:
            wait.until(lambda _driver: self.browser.waits.is_present_quick(
                self.paragraphs[index].locator,
                timeout=0.3
            ))
        except TimeoutException:
            raise TimeoutException(f'{self}: paragraph #{index} did not appear')

    def scroll_until_paragraphs_count(self, target: int) -> None:
        Logger.info(f'{self}: scroll until paragraphs count == {target}')

        current = self.get_paragraphs_count()
        steps = 0

        while current < target:
            steps += 1
            next_index = current + 1

            Logger.info(f'{self}: scroll step {steps}, current={current}')

            if self.browser.waits.is_present_quick(self.paragraphs[next_index].locator, timeout=0.1):
                current = next_index
                continue

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            self.wait_until_paragraph_appears(next_index)
            current = next_index

        self.paragraphs[target].wait_for_presence()
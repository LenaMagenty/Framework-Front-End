from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger


class HoversPage(BasePage):
    PAGE_NAME = 'HoversPage'

    CONTENT_LOC = 'content'  # ID
    USER_CARD_XPATH = "//div[@id='content']//div[contains(@class,'figure')]"
    USER_NAME_XPATH = "//div[@id='content']//div[contains(@class,'figure')]//h5"
    USER_PROFILE_LINK_XPATH = "//div[@id='content']//div[contains(@class,'figure')]//a"

    UNIQUE_ELEMENT_LOC = CONTENT_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.content = WebElement(
            browser=self.browser,
            locator=self.CONTENT_LOC,
            description='Hovers content'
        )
        self.unique_element = self.content

        self.user_cards = MultiWebElement(
            browser=self.browser,
            formattable_xpath=f'({self.USER_CARD_XPATH})[{{}}]',
            description='User card'
        )

        self.user_names = MultiWebElement(
            browser=self.browser,
            formattable_xpath=f'({self.USER_NAME_XPATH})[{{}}]',
            description='User name'
        )

        self.user_profile_links = MultiWebElement(
            browser=self.browser,
            formattable_xpath=f'({self.USER_PROFILE_LINK_XPATH})[{{}}]',
            description='User profile link'
        )

    def get_users_count(self) -> int:
        Logger.info(f'{self}: get users count')
        count = 0
        for _ in self.user_cards:
            count += 1
        return count

    def hover_user_by_index(self, index: int) -> None:
        Logger.info(f'{self}: hover user #{index}')
        WebElement(
            browser=self.browser,
            locator=self.user_cards.formattable_xpath.format(index),
            description=f'User card #{index}'
        ).move_to_element()

    def get_user_name_by_index(self, index: int) -> str:
        Logger.info(f'{self}: get user name #{index}')
        self.hover_user_by_index(index)
        return WebElement(
            browser=self.browser,
            locator=self.user_names.formattable_xpath.format(index),
            description=f'User name #{index}'
        ).get_text()

    def get_user_number_by_index(self, index: int) -> str:
        Logger.info(f'{self}: get user number #{index}')
        name_text = self.get_user_name_by_index(index)
        user_part = name_text.split(':')[-1].strip()
        return ''.join(ch for ch in user_part if ch.isdigit())

    def open_user_profile_by_index(self, index: int) -> None:
        Logger.info(f'{self}: open user profile #{index}')
        self.hover_user_by_index(index)
        WebElement(
            browser=self.browser,
            locator=self.user_profile_links.formattable_xpath.format(index),
            description=f'User profile link #{index}'
        ).click()

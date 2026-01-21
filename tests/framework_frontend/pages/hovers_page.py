from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement
from logger.logger import Logger


class HoversPage(BasePage):
    PAGE_NAME = 'HoversPage'

    UNIQUE_ELEMENT_LOC = (By.ID, 'content')
    USER_CARD_XPATH = "//div[@id='content']//div[contains(@class,'figure')]"
    USER_PAGE_UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(),'Not Found')")

    def get_users_count(self) -> int:
        Logger.info(f'{self}: get users count')
        return len(
            self.browser.driver.find_elements(By.XPATH, self.USER_CARD_XPATH)
        )

    def _user_card(self, index: int) -> BaseElement:
        return BaseElement(
            browser=self.browser,
            locator=(By.XPATH, f'({self.USER_CARD_XPATH})[{index}]'),
            description=f'{self.PAGE_NAME} user card #{index}'
        )

    def _user_name(self, index: int) -> BaseElement:
        return BaseElement(
            browser=self.browser,
            locator=(By.XPATH, f'({self.USER_CARD_XPATH})[{index}]//h5'),
            description=f'{self.PAGE_NAME} user name #{index}'
        )

    def _user_profile_link(self, index: int) -> BaseElement:
        return BaseElement(
            browser=self.browser,
            locator=(By.XPATH, f'({self.USER_CARD_XPATH})[{index}]//a'),
            description=f'{self.PAGE_NAME} user profile link #{index}'
        )

    def hover_user_by_index(self, index: int) -> None:
        Logger.info(f'{self}: hover user #{index}')
        card = self._user_card(index).wait_for_presence()
        self.browser.move_to_element(card)

    def get_user_name_by_index(self, index: int) -> str:
        Logger.info(f'{self}: get user name #{index}')
        self.hover_user_by_index(index)
        return self._user_name(index).wait_for_presence().text

    def get_user_number_by_index(self, index: int) -> str:
        Logger.info(f'{self}: get user number #{index}')
        name_text = self.get_user_name_by_index(index)
        user_part = name_text.split(':')[-1].strip()
        return ''.join(ch for ch in user_part if ch.isdigit())

    def open_user_profile_by_index(self, index: int) -> None:
        Logger.info(f'{self}: open user profile #{index}')
        self.hover_user_by_index(index)
        self._user_profile_link(index).wait_for_presence().click()

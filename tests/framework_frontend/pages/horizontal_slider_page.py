import random
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from elements.base_element import BaseElement
from logger.logger import Logger


class HorizontalSliderPage(BasePage):
    PAGE_NAME = 'HorizontalSliderPage'

    SLIDER_LOC = (By.XPATH, "//input[@type='range']")
    SLIDER_RANGE = (By.ID, 'range')
    UNIQUE_ELEMENT_LOC = SLIDER_LOC

    STEP = Decimal('0.5')

    def _slider(self) -> BaseElement:
        return BaseElement(self.browser, self.SLIDER_LOC, 'Horizontal slider')

    def _range(self) -> BaseElement:
        return BaseElement(self.browser, self.SLIDER_RANGE, 'Slider value')

    def set_random_value_with_keys(self) -> Decimal:
        slider = self._slider().wait_for_presence()
        self.browser.execute_script('arguments[0].focus();', slider)

        presses = random.randint(1, 10)
        expected_value = self.STEP * presses

        Logger.info(
            f'{self}: slider random presses = {presses}, '
            f'expected value = {expected_value}'
        )

        for _ in range(presses):
            slider.send_keys(Keys.ARROW_RIGHT)

        return expected_value

    def get_value(self) -> Decimal:
        return Decimal(self._range().get_text())

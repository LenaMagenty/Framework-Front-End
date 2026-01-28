from decimal import Decimal
import random
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from logger.logger import Logger


class HorizontalSliderPage(BasePage):
    PAGE_NAME = 'HorizontalSliderPage'

    SLIDER_LOC = "//input[@type='range']"
    RANGE_LOC = 'range'
    UNIQUE_ELEMENT_LOC = SLIDER_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.slider = Input(
            browser=self.browser,
            locator=self.SLIDER_LOC,
            description='Horizontal slider'
        )
        self.range_value = Label(
            browser=self.browser,
            locator=self.RANGE_LOC,
            description='Slider value'
        )

        self.unique_element = self.slider


    def set_slider_value_in_range(
            self,
            min_value: Decimal,
            max_value: Decimal,
            step: Decimal
    ) -> Decimal:
        Logger.info(
            f'Set slider value in range: min={min_value}, max={max_value}, step={step}'
        )

        steps_count = int((max_value - min_value) / step)
        possible_values = [
            min_value + step * i
            for i in range(1, steps_count)
        ]

        target_value = random.choice(possible_values)

        current_value = Decimal(self.range_value.get_text())
        presses = int((target_value - current_value) / step)

        if presses > 0:
            self.slider.send_keys(Keys.ARROW_RIGHT * presses, clear=False)
        elif presses < 0:
            self.slider.send_keys(Keys.ARROW_LEFT * abs(presses), clear=False)

        Logger.info(
            f'Slider target = {target_value}, actual = {self.range_value.get_text()}'
        )

        return target_value

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

    def set_slider_value(
            self,
            target_value: Decimal,
            step: Decimal
    ) -> None:
        Logger.info(
            f'Set slider to value: target={target_value}, step={step}'
        )

        current_value = Decimal(self.range_value.get_text())
        presses = int((target_value - current_value) / step)

        if presses > 0:
            self.slider.send_keys(Keys.ARROW_RIGHT * presses, clear=False)
        else:
            self.slider.send_keys(Keys.ARROW_LEFT * abs(presses), clear=False)

        Logger.info(
            f'Slider actual value = {self.range_value.get_text()}'
        )

from decimal import Decimal
import random

from pages.horizontal_slider_page import HorizontalSliderPage
from config.config_reader import ConfigReader
from logger.logger import Logger


def test_horizontal_slider(browser):
    config = ConfigReader()
    browser.get(config.get('horizontal_slider_url'))

    page = HorizontalSliderPage(browser)
    page.wait_for_open()

    min_value = Decimal('0')
    max_value = Decimal('5')
    step = Decimal('0.5')

    steps_count = int((max_value - min_value) / step)
    possible_values = [
        min_value + step * i
        for i in range(1, steps_count)
    ]

    expected = random.choice(possible_values)

    Logger.info(f'Set random value on horizontal slider: {expected}')

    page.set_slider_value(
        target_value=expected,
        step=step
    )

    actual = Decimal(page.range_value.get_text())

    assert actual == expected, (
        f'Ожидали "{expected}", но получили "{actual}"'
    )

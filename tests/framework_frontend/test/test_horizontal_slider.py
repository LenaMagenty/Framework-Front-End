from decimal import Decimal

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

    Logger.info('Set random value on horizontal slider')
    expected = page.set_slider_value_in_range(
        min_value=min_value,
        max_value=max_value,
        step=step
    )

    actual = Decimal(page.range_value.get_text())

    assert actual == expected, f'Ожидали "{expected}", но получили "{actual}"'

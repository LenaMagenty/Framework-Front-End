from pages.horizontal_slider_page import HorizontalSliderPage
from config.config_reader import ConfigReader
from logger.logger import Logger


def test_horizontal_slider(browser):
    config = ConfigReader()
    browser.get(config.get('horizontal_slider_url'))

    page = HorizontalSliderPage(browser)
    page.wait_for_open()

    expected = page.set_random_value_with_keys()
    actual = page.get_value()

    Logger.info(
        f'TEST: expected slider value = {expected}, actual slider value = {actual}'
    )

    assert actual == expected, f'Ожидали "{expected}", но получили "{actual}"'

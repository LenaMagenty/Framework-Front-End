from config.config_reader import ConfigReader
from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(browser):
    config = ConfigReader()
    browser.get(config.get('dynamic_content_url'))

    page = DynamicContentPage(browser=browser)
    page.wait_for_open()

    page.refresh_until_any_two_images_match()

    images_src = page.get_images_src()

    assert len(images_src) != len(set(images_src)), (
        'Любые два изображения из трёх должны совпадать'
    )

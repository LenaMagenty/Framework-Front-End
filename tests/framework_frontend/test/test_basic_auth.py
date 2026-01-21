from config.config_reader import ConfigReader
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(browser):
    config = ConfigReader()

    auth = config.get('auth')
    browser.set_basic_auth(
        username=auth['username'],
        password=auth['password']
    )

    browser.get(config.get('basic_auth_url'))

    page = BasicAuthPage(browser)
    page.wait_for_open()

    assert page.UNIQUE_ELEMENT_LOC is not None, (
        "Авторизация не пройдена, страница не открылась"
    )

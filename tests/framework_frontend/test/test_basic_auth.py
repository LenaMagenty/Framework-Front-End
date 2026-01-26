from utils.url_helper import UrlHelper

from config.config_reader import ConfigReader
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(browser):
    config = ConfigReader()
    auth = config.get("auth")

    browser.get(
        UrlHelper.with_basic_auth(
            config.get('basic_auth_url'),
            auth['username'],
            auth['password']
        )
    )

    page = BasicAuthPage(browser)
    page.wait_for_open()

    assert "Congratulations" in page.get_success_message_text(), (
        "Авторизация не пройдена"
    )

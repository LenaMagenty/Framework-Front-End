from config.config_reader import ConfigReader
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(browser):
    config = ConfigReader()

    browser.get(config.get("basic_auth_url"))

    page = BasicAuthPage(browser)
    page.wait_for_open()

    assert "Congratulations" in page.get_success_message_text(), (
        "Авторизация не пройдена"
    )

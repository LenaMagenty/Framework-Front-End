from pages.alerts_and_contextclick_page import AlertsContextCLickPage
from config.config_reader import ConfigReader


def test_alerts_and_context_click(browser):
    config = ConfigReader()
    browser.get(config.get('context_click_url'))

    page = AlertsContextCLickPage(browser)
    page.wait_for_open()

    page.context_click_area()
    assert browser.alerts.get_text() == 'You selected a context menu'
    browser.alerts.confirm()
    assert browser.alerts.is_present() is False

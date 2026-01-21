from faker import Faker

from pages.alerts_page import AlertsPage
from config.config_reader import ConfigReader


def test_alerts(browser):
    faker = Faker()

    config = ConfigReader()
    browser.get(config.get('alerts_url'))

    page = AlertsPage(browser)
    page.wait_for_open()

    # JS Alert
    page.click_js_alert()
    assert browser.alerts.get_text() == 'I am a JS Alert'
    browser.alerts.confirm()
    assert page.get_result_text() == 'You successfully clicked an alert'

    # JS Confirm
    page.click_js_confirm()
    assert browser.alerts.get_text() == 'I am a JS Confirm'
    browser.alerts.confirm()
    assert page.get_result_text() == 'You clicked: Ok'

    # JS Prompt
    text = faker.pystr(min_chars=5, max_chars=15)

    page.click_js_prompt()
    assert browser.alerts.get_text() == 'I am a JS prompt'
    browser.alerts.write_text_and_confirm(text)
    assert page.get_result_text() == f'You entered: {text}'

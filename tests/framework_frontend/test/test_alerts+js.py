from faker import Faker
from pages.alerts_page import AlertsPage
from config.config_reader import ConfigReader


def test_alerts_js (browser):
    faker = Faker()

    config = ConfigReader()
    browser.get(config.get('alerts_url'))

    page = AlertsPage(browser)
    page.wait_for_open()

    # JS Alert
    page.open_js_alert_via_script()
    assert browser.alerts.get_text() == 'I am a JS Alert'
    browser.alerts.confirm()
    assert page.get_result_text() == 'You successfully clicked an alert'

    # JS Confirm
    page.open_js_confirm_via_script()
    assert browser.alerts.get_text() == 'I am a JS Confirm'
    browser.alerts.confirm()
    assert page.get_result_text() == 'You clicked: Ok'

    # JS Prompt
    text = faker.pystr(min_chars=5, max_chars=15)
    page.open_js_prompt_via_script()
    assert browser.alerts.get_text() == 'I am a JS prompt'
    browser.alerts.write_text_and_confirm(text)
    assert page.get_result_text() == f'You entered: {text}'

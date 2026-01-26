from faker import Faker

from config.config_reader import ConfigReader
from pages.alerts_page import AlertsPage


def test_alerts_js(browser):
    faker = Faker()

    config = ConfigReader()
    browser.get(config.get("alerts_url"))

    page = AlertsPage(browser)
    page.wait_for_open()

    # JS Alert
    browser.execute_script("jsAlert();")

    actual_alert_text = browser.alerts.get_text()
    expected_alert_text = "I am a JS Alert"
    assert actual_alert_text == expected_alert_text, (
        f"Текст JS Alert не соответствует ожидаемому. "
        f"Ожидалось: '{expected_alert_text}', фактически: '{actual_alert_text}'"
    )

    browser.alerts.confirm()

    actual_result_text = page.get_result_text()
    expected_result_text = "You successfully clicked an alert"
    assert actual_result_text == expected_result_text, (
        f"Текст результата после подтверждения JS Alert не соответствует ожидаемому. "
        f"Ожидалось: '{expected_result_text}', фактически: '{actual_result_text}'"
    )

    # JS Confirm
    browser.execute_script("jsConfirm();")

    actual_alert_text = browser.alerts.get_text()
    expected_alert_text = "I am a JS Confirm"
    assert actual_alert_text == expected_alert_text, (
        f"Текст JS Confirm не соответствует ожидаемому. "
        f"Ожидалось: '{expected_alert_text}', фактически: '{actual_alert_text}'"
    )

    browser.alerts.confirm()

    actual_result_text = page.get_result_text()
    expected_result_text = "You clicked: Ok"
    assert actual_result_text == expected_result_text, (
        f"Текст результата после подтверждения JS Confirm не соответствует ожидаемому. "
        f"Ожидалось: '{expected_result_text}', фактически: '{actual_result_text}'"
    )

    # JS Prompt
    text = faker.pystr(min_chars=5, max_chars=15)
    browser.execute_script("jsPrompt();")

    actual_alert_text = browser.alerts.get_text()
    expected_alert_text = "I am a JS prompt"
    assert actual_alert_text == expected_alert_text, (
        f"Текст JS Prompt не соответствует ожидаемому. "
        f"Ожидалось: '{expected_alert_text}', фактически: '{actual_alert_text}'"
    )

    browser.alerts.write_text_and_confirm(text)

    actual_result_text = page.get_result_text()
    expected_result_text = f"You entered: {text}"
    assert actual_result_text == expected_result_text, (
        f"Текст результата после ввода значения в JS Prompt не соответствует ожидаемому. "
        f"Ожидалось: '{expected_result_text}', фактически: '{actual_result_text}'"
    )

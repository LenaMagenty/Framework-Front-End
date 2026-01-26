from pages.alerts_and_contextclick_page import AlertsContextClickPage
from config.config_reader import ConfigReader


def test_alerts_and_context_click(browser):
    config = ConfigReader()
    browser.get(config.get("context_click_url"))

    page = AlertsContextClickPage(browser)
    page.wait_for_open()

    page.context_click_area()

    actual_alert_text = browser.alerts.get_text()
    expected_alert_text = "You selected a context menu"
    assert actual_alert_text == expected_alert_text, (
        f"Текст Alert после контекстного клика не соответствует ожидаемому. "
        f"Ожидалось: '{expected_alert_text}', фактически: '{actual_alert_text}'"
    )

    browser.alerts.confirm()

    alert_is_present = browser.alerts.is_present()
    assert not alert_is_present, (
        f"Alert не закрылся после подтверждения. "
        f"Ожидалось: отсутствие Alert, фактически: Alert присутствует"
    )

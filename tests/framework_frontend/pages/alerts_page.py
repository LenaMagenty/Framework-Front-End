from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement


class AlertsPage(BasePage):
    PAGE_NAME = 'AlertsPage'

    JS_ALERT_BUTTON = (By.XPATH, "//button[@onclick='jsAlert()']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[@onclick='jsConfirm()']")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[@onclick='jsPrompt()']")
    RESULT_TEXT = (By.ID, 'result')

    UNIQUE_ELEMENT_LOC = JS_ALERT_BUTTON

    def click_js_alert(self) -> None:
        BaseElement(self.browser, self.JS_ALERT_BUTTON,
                    'Click for JS Alert').click()

    def click_js_confirm(self) -> None:
        BaseElement(self.browser, self.JS_CONFIRM_BUTTON,
                    'Click for JS Confirm').click()

    def click_js_prompt(self) -> None:
        BaseElement(self.browser, self.JS_PROMPT_BUTTON,
                    'Click for JS Prompt').click()

    def get_result_text(self) -> str:
        return BaseElement(self.browser, self.RESULT_TEXT,
                           'Result').get_text()

    def open_js_alert_via_script(self) -> None:
        self.browser.execute_script('jsAlert();')

    def open_js_confirm_via_script(self) -> None:
        self.browser.execute_script('jsConfirm();')

    def open_js_prompt_via_script(self) -> None:
        self.browser.execute_script('jsPrompt();')

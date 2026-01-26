from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label


class AlertsPage(BasePage):
    PAGE_NAME = 'AlertsPage'

    JS_ALERT_BUTTON_LOC = "//button[@onclick='jsAlert()']"
    JS_CONFIRM_BUTTON_LOC = "//button[@onclick='jsConfirm()']"
    JS_PROMPT_BUTTON_LOC = "//button[@onclick='jsPrompt()']"
    RESULT_TEXT_LOC = 'result'

    UNIQUE_ELEMENT_LOC = JS_ALERT_BUTTON_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.js_alert_button = Button(
            browser=self.browser,
            locator=self.JS_ALERT_BUTTON_LOC,
            description='Click for JS Alert'
        )

        self.js_confirm_button = Button(
            browser=self.browser,
            locator=self.JS_CONFIRM_BUTTON_LOC,
            description='Click for JS Confirm'
        )

        self.js_prompt_button = Button(
            browser=self.browser,
            locator=self.JS_PROMPT_BUTTON_LOC,
            description='Click for JS Prompt'
        )

        self.result_text = Label(
            browser=self.browser,
            locator=self.RESULT_TEXT_LOC,
            description='Result'
        )

        self.unique_element = self.js_alert_button

    def click_js_alert(self) -> None:
        self.js_alert_button.click()

    def click_js_confirm(self) -> None:
        self.js_confirm_button.click()

    def click_js_prompt(self) -> None:
        self.js_prompt_button.click()

    def get_result_text(self) -> str:
        return self.result_text.get_text()

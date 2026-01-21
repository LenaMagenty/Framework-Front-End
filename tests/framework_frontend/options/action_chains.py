from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains as SeleniumActionChains


class ActionChains:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def drag_and_drop(self, source, target) -> None:
        SeleniumActionChains(self._driver).drag_and_drop(source, target).perform()

    def context_click(self, element) -> None:
        SeleniumActionChains(self._driver).context_click(element).perform()

    def click_and_hold(self, element) -> None:
        SeleniumActionChains(self._driver).click_and_hold(element).perform()

    def drag_by_offset(self, element, x_offset: int, y_offset: int = 0) -> None:
        (
            SeleniumActionChains(self._driver)
            .click_and_hold(element)
            .move_by_offset(x_offset, y_offset)
            .release()
            .perform()
        )

    def move_to_element(self, element) -> None:
        SeleniumActionChains(self._driver).move_to_element(element).perform()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return str(self)

from selenium.webdriver.common.action_chains import ActionChains as SeleniumActionChains


class ActionChains:
    def __init__(self, browser) -> None:
        self._browser = browser

    def drag_and_drop(self, source, target) -> None:
        source_el = source.wait_for_presence()
        target_el = target.wait_for_presence()

        SeleniumActionChains(self._browser.driver) \
            .drag_and_drop(source_el, target_el) \
            .perform()

    def context_click(self, element) -> None:
        web_element = element.wait_for_presence()

        SeleniumActionChains(self._browser.driver) \
            .context_click(web_element) \
            .perform()

    def click_and_hold(self, element) -> None:
        web_element = element.wait_for_presence()

        SeleniumActionChains(self._browser.driver) \
            .click_and_hold(web_element) \
            .perform()

    def move_to_element(self, element) -> None:
        web_element = element.wait_for_presence()

        SeleniumActionChains(self._browser.driver) \
            .move_to_element(web_element) \
            .perform()

    def __str__(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return str(self)

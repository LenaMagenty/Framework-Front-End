from typing_extensions import Self

from browser.browser import Browser
from elements.web_element import WebElement


class MultiWebElement:
    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
    ) -> None:
        self.index = 1

        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.description = description if description else self.formattable_xpath.format('i:')

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = WebElement(
            self.browser,
            self.formattable_xpath.format(self.index),
            f'{self.description}[{self.index}]',
        )

        if not current_element.is_exists():
            raise StopIteration

        self.index += 1
        return current_element

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self.description}]'

    def __repr__(self) -> str:
        return str(self)

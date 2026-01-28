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
        self._iter_index = 1

        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.description = description if description else self.formattable_xpath.format('i:')

    def __iter__(self) -> Self:
        self._iter_index = 1
        return self

    def __next__(self) -> WebElement:
        element = self[self._iter_index]
        if not element.is_exists():
            raise StopIteration

        self._iter_index += 1
        return element

    def __getitem__(self, index: int) -> WebElement:
        if not isinstance(index, int):
            raise TypeError(f'Index must be int, got {type(index).__name__}')
        if index < 1:
            raise ValueError(f'Index must be >= 1, got {index}')

        return WebElement(
            browser=self.browser,
            locator=self.formattable_xpath.format(index),
            description=f'{self.description} #{index}',
        )

    def __str__(self) -> str:
        return f'{self.__class__.__name__}[{self.description}]'

    def __repr__(self) -> str:
        return str(self)

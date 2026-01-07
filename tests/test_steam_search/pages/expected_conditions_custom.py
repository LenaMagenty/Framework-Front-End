from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class ElementInResultRow:
    def __init__(self, rows_locator, row_index, inner_locator):
        self.rows_locator = rows_locator
        self.row_index = row_index
        self.inner_locator = inner_locator

    def __call__(self, driver):
        try:
            rows = driver.find_elements(*self.rows_locator)
            if len(rows) <= self.row_index:
                return False

            row = rows[self.row_index]
            return row.find_element(*self.inner_locator)

        except (NoSuchElementException, StaleElementReferenceException):
            return False

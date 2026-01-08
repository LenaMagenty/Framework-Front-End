from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.expected_conditions_custom import ElementInResultRow
from selenium.webdriver.support.ui import WebDriverWait


class SearchResultsPage(BasePage):
    SORT_TRIGGER = (By.XPATH, "//*[@id='sort_by_trigger']")
    PRICE_DESC_OPTION = (By.XPATH, "//*[@id='Price_DESC']")
    SORT_VALUE_INPUT = (By.XPATH, "//*[@id='sort_by']")
    RESULTS_CONTAINER = (By.XPATH, "//*[@id='search_resultsRows']")
    RESULT_ROWS = (By.XPATH, "//*[@id='search_resultsRows']//a[contains(@class,'search_result_row')]")
    TITLE_IN_ROW = (By.XPATH, ".//span[@class='title']")
    SEARCH_RESULT_OPACITY = (
        By.XPATH, "//*[@id='search_result_container' and contains(@style, 'opacity')]"
    )
    PRICE_BLOCK_IN_ROW = (
        By.XPATH, ".//div[contains(@class,'discount_block search_discount_block') "
                  "and @data-price-final]"
    )
    UNIQUE_ELEMENT = SORT_TRIGGER

    def wait_loaded(self, n: int = 1):
        self.wait.until(EC.visibility_of_element_located(self.RESULTS_CONTAINER))
        self.wait.until(lambda d: len(d.find_elements(*self.RESULT_ROWS)) >= n)
        return self

    def sort_by_highest_price(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_TRIGGER)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_DESC_OPTION)).click()

        fast_wait = WebDriverWait(self.driver, 2, poll_frequency=0.05)
        fast_wait.until(EC.presence_of_element_located(self.SEARCH_RESULT_OPACITY))
        self.wait.until(EC.invisibility_of_element_located(self.SEARCH_RESULT_OPACITY))

        self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ROWS))

        return self

    def get_first_n_items(self, n):
        self.wait_loaded(n)

        items: list[tuple[str, int]] = []

        for i in range(n):
            title = self.wait.until(
                ElementInResultRow(self.RESULT_ROWS, i, self.TITLE_IN_ROW)
            ).text.strip()

            price_block = self.wait.until(
                ElementInResultRow(self.RESULT_ROWS, i, self.PRICE_BLOCK_IN_ROW)
            )
            price_final = int(price_block.get_attribute('data-price-final'))

            items.append((title, price_final))

        return items

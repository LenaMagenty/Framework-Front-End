from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchResultsPage(BasePage):
    SORT_TRIGGER = (By.ID, 'sort_by_trigger')
    PRICE_DESC_OPTION = (By.ID, 'Price_DESC')
    SORT_VALUE_INPUT = (By.ID, 'sort_by')
    RESULTS_CONTAINER = (By.ID, 'search_resultsRows')
    RESULT_ROWS = (
        By.XPATH,
        "//*[@id='search_resultsRows']//"
        "a[contains(@class,'search_result_row')]"
    )
    TITLE_IN_ROW = (By.XPATH, ".//span[@class='title']")
    SEARCH_RESULT_OPACITY = (
        By.XPATH,
        "//*[@id='search_result_container' "
        "and contains(@style, 'opacity')]"
    )
    PRICE_BLOCK_IN_ROW = (
        By.XPATH,
        ".//div[contains(@class,'discount_block') "
        "and contains(@class,'search_discount_block') "
        "and @data-price-final] "
        "| .//div[contains(@class,'search_price_discount_combined') "
        "and @data-price-final][not(.//div[contains(@class,'discount_block') "
        "and contains(@class,'search_discount_block') "
        "and @data-price-final])]"
    )
    UNIQUE_ELEMENT = SORT_TRIGGER

    def sort_by_highest_price(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_TRIGGER)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_DESC_OPTION)).click()

        fast_wait = WebDriverWait(self.driver, 15, poll_frequency=0.05)
        fast_wait.until(EC.presence_of_element_located(self.SEARCH_RESULT_OPACITY))
        self.wait.until(EC.invisibility_of_element_located(self.SEARCH_RESULT_OPACITY))

        self.wait.until(EC.presence_of_all_elements_located(self.RESULT_ROWS))

        return self

    def get_first_n_items(self, n):
        self.wait.until(EC.visibility_of_element_located(self.RESULTS_CONTAINER))
        self.wait.until(lambda d: len(d.find_elements(*self.RESULT_ROWS)) >= n)

        titles = self.wait.until(
            EC.presence_of_all_elements_located(self.TITLE_IN_ROW)
        )
        prices = self.wait.until(
            EC.presence_of_all_elements_located(self.PRICE_BLOCK_IN_ROW)
        )

        items: list[tuple[str, int]] = []

        for i in range(n):
            title = titles[i].text.strip()
            price_final = int(prices[i].get_attribute('data-price-final'))
            items.append((title, price_final))

        return items

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(BasePage):
    SORT_TRIGGER = (By.XPATH, "//*[@id='sort_by_trigger']")
    PRICE_DESC_OPTION = (By.XPATH, "//*[@id='Price_DESC']")
    SORT_VALUE_INPUT = (By.XPATH, "//*[@id='sort_by']")
    RESULTS_CONTAINER = (By.XPATH, "//*[@id='search_resultsRows']")
    RESULT_ROWS = (By.XPATH, "//*[@id='search_resultsRows']//a[contains(@class,'search_result_row')]")
    TITLE_IN_ROW = (By.XPATH, ".//span[@class='title']")
    PRICE_BLOCK_IN_ROW = (
        By.XPATH,
        ".//div[contains(@class,'search_price_discount_combined') and @data-price-final]"
    )

    def wait_loaded(self, n: int = 1):
        self.wait.until(EC.visibility_of_element_located(self.RESULTS_CONTAINER))
        self.wait.until(lambda d: len(d.find_elements(*self.RESULT_ROWS)) >= n)
        return self

    def sort_by_highest_price(self):
        """
        Если пользователь видит, что игры перемешались,
        то он думает, что произошла сортировка.
        То есть пользователь замечает, что в очередности игр что-то поменялось,
        потому что список игр "дёрнулся".
        Следовательно, мы берём для надёжности хотя бы первые 10 игр и проверяем,
        что после клика на кнопку сортировки, хотя бы одна игра из этих 10 устарела в DOM.
        """

        self.wait_loaded(10)

        rows_before = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULT_ROWS)
        )[:10]

        self.wait.until(EC.element_to_be_clickable(self.SORT_TRIGGER)).click()
        self.wait.until(EC.element_to_be_clickable(self.PRICE_DESC_OPTION)).click()

        self.wait.until(lambda d: any(EC.staleness_of(row)(d) for row in rows_before))

        # Также пользователь видит что поменялась надпись на кнопке сортировки.
        self.wait.until(
            lambda d: (
                    EC.text_to_be_present_in_element(self.SORT_TRIGGER, 'Highest Price')(d)
                    or EC.text_to_be_present_in_element(self.SORT_TRIGGER, 'убыванию цены')(d)
            )
        )
        return self

    def get_first_n_items(self, n: int):
        self.wait_loaded(n)

        rows = self.driver.find_elements(*self.RESULT_ROWS)[:n]
        items: list[tuple[str, int]] = []

        for row in rows:
            title = row.find_element(*self.TITLE_IN_ROW).text.strip()

            price_block = row.find_element(*self.PRICE_BLOCK_IN_ROW)
            price_final = int(price_block.get_attribute('data-price-final'))

            items.append((title, price_final))

        return items

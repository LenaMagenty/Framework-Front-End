from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//*[@id='global_action_menu']//a[contains(@href,'login')]")
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder,'Поиск') or contains(@placeholder,'Search')]")
    SEARCH_BUTTON = (By.XPATH, "//form[contains(@role,'search')]//button[@type='submit']")
    UNIQUE_ELEMENT = LOGIN_BUTTON

    def search(self, game_name: str):
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.send_keys(game_name)

        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()

        return SearchResultsPage()

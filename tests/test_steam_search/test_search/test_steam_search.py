import pytest
from pages.home_page import HomePage
from config.config_reader import ConfigReader


@pytest.mark.parametrize('game_name,n', [
    ('The Witcher', 10),
    ('Fallout', 20),
])
def test_search_sort_highest_price_and_get_n(driver, game_name, n):
    config = ConfigReader()
    driver.get(config.get('url'))
    home = HomePage()
    home.wait_opened()

    results = home.search(game_name)
    results.wait_opened()

    results.sort_by_highest_price()
    items = results.get_first_n_items(n)

    prices = [price for _, price in items]

    assert all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)), (
        "Сортировка по убыванию цены работает неверно"
    )

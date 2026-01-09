import pytest
from pages.home_page import HomePage
from config.config_reader import ConfigReader


@pytest.mark.parametrize('game_name,n', [
    ('The Witcher', 10),
    ('Fallout', 20)
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

    prices = [element[1] for element in items]

    assert prices == sorted(prices, reverse=True), (
        "Сортировка по убыванию цены работает неверно"
    )


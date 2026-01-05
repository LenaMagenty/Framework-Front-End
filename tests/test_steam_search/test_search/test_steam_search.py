import pytest
from pages.home_page import HomePage


@pytest.mark.parametrize('game_name,n', [
    ('The Witcher', 10),
    ('Fallout', 20),
])
def test_search_sort_highest_price_and_get_n(driver, game_name, n):
    home = HomePage(driver).open().assert_opened()
    results = home.search(game_name)

    results.sort_by_highest_price()
    items = results.get_first_n_items(n)

    assert len(items) == n, f'Ожидали {n} игр, получили {len(items)}'

    prices = [price for _, price in items]

    assert all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)), (
            "Сортировка по убыванию цены работает неверно"
    )

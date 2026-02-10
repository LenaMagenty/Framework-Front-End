from pages.infinity_scroll_page import InfinityScrollPage
from config.config_reader import ConfigReader
import pytest

@pytest.mark.slow
def test_infinite_scroll(browser):
    target = 36
    config = ConfigReader()
    browser.get(config.get('infinity_scroll_url'))

    page = InfinityScrollPage(browser)
    page.wait_for_open()

    page.scroll_until_paragraphs_count(target)

    assert page.get_paragraphs_count() == target, (
        f'Ожидали {target} параграфов, но получено {page.get_paragraphs_count()}'
    )

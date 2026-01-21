from config.config_reader import ConfigReader
from pages.hovers_page import HoversPage
from pages.user_page import UserPage


def test_hovers(browser):
    config = ConfigReader()
    browser.get(config.get('hovers_url'))

    page = HoversPage(browser)
    page.wait_for_open()

    users_count = page.get_users_count()

    for index in range(1, users_count + 1):
        name_number = page.get_user_number_by_index(index)

        page.open_user_profile_by_index(index)

        user_page = UserPage(browser)
        user_page.wait_for_open()

        url_number = browser.current_url.rstrip('/').split('/')[-1]

        assert name_number == url_number, (
            f'User id mismatch: name="{name_number}", url="{url_number}"'
        )

        browser.back()
        page.wait_for_open()

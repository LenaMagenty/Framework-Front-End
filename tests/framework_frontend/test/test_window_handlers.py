from pages.window_handlers_page import WindowHandlersPage
from pages.new_window_page import NewWindowPage
from config.config_reader import ConfigReader


def test_window_handlers(browser):
    config = ConfigReader()
    browser.get(config.get('windows_handlers_url'))

    page = WindowHandlersPage(browser)
    page.wait_for_open()

    main_handle = browser.get_current_window_handle()
    opened_handles: list[str] = []

    old_handles = browser.get_all_window_handles()
    page.click_click_here_link()

    first_new_handle = browser.wait_new_window_handle(old_handles)
    opened_handles.append(first_new_handle)

    browser.switch_to_window(first_new_handle)

    new_window = NewWindowPage(browser)
    new_window.wait_for_open()
    assert browser.get_title() == 'New Window'

    browser.switch_to_window(main_handle)
    page.wait_for_open()

    old_handles = browser.get_all_window_handles()
    page.click_click_here_link()

    second_new_handle = browser.wait_new_window_handle(old_handles)
    opened_handles.append(second_new_handle)

    browser.switch_to_window(second_new_handle)
    new_window.wait_for_open()
    assert browser.get_title() == 'New Window'

    browser.switch_to_window(main_handle)
    page.wait_for_open()

    for handle in opened_handles:
        browser.switch_to_window(handle)
        browser.close_current_window()

    browser.switch_to_window(main_handle)
    page.wait_for_open()

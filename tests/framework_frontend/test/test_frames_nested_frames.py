from pages.frames_page import FramesPage
from pages.nested_frames_page import NestedFramesPage
from config.config_reader import ConfigReader
from logger.logger import Logger


def test_frames_nested_frames(browser):
    config = ConfigReader()
    browser.get(config.get('frames_url'))

    frames_page = FramesPage(browser)
    frames_page.wait_for_open()

    frames_page.ensure_alerts_frame_windows_group_opened()

    frames_page.open_nested_frames()

    nested_frames_page = NestedFramesPage(browser)
    nested_frames_page.wait_for_open()

    nested_frames_page.check_parent_text_visible()
    nested_frames_page.check_child_text_visible()

    frames_page.open_frames()
    frames_page.wait_for_open()

    top_text = frames_page.get_top_frame_text()
    bottom_text = frames_page.get_bottom_frame_text()

    Logger.info(f'top frame text = "{top_text}"')
    Logger.info(f'bottom frame text = "{bottom_text}"')

    assert top_text == bottom_text, (
        f'Текст в верхнем фрейме отличается от текста в нижнем фрейме. '
        f'top="{top_text}", bottom="{bottom_text}"'
    )

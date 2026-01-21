from pathlib import Path

from config.config_reader import ConfigReader
from pages.upload_image_page import UploadImagePage
from utils.pyautogui import PyAutoGUIUtilities


def test_upload_image_drag_and_drop(browser):
    config = ConfigReader()
    browser.get(config.get('upload_image_url'))

    page = UploadImagePage(browser)
    page.wait_for_open()

    file_name = 'New Image.jpeg'
    file_path = (Path(__file__).parent / file_name).resolve()

    point = browser.execute_script(
        """
        const el = arguments[0];

        const r = el.getBoundingClientRect();
        const chromeY = window.outerHeight - window.innerHeight;

        const x = Math.round(r.left + r.width / 2);
        const y = Math.round(chromeY + r.top + r.height / 2);

        return { x: x, y: y };
        """,
        page.drop_zone.wait_for_presence()
    )

    PyAutoGUIUtilities.drag_file_from_explorer_to_screen_point(
        file_path=str(file_path),
        target_x=point["x"],
        target_y=point["y"]
    )
    page.wait_file_in_dropzone()

    assert page.dropzone_file_name.is_exists(), (
        'Имя файла не появилось после его загрузки'
    )
    assert page.dropzone_success_mark.is_exists(), (
        'Подтверждающая галочка не появилась после загрузки файла'
    )

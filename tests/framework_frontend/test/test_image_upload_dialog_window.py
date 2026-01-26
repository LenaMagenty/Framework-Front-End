from pathlib import Path

from config.config_reader import ConfigReader
from pages.upload_image_page import UploadImagePage
from utils.pyautogui import PyAutoGUIUtilities


def test_upload_image_via_dialog_window(browser):
    config = ConfigReader()
    browser.get(config.get('upload_image_url'))

    page = UploadImagePage(browser)
    page.wait_for_open()

    file_path = Path('tests/framework_frontend/test/New Image.jpeg').resolve()

    page.open_file_dialog()
    print('PRINT:', str(file_path))
    print('REPR :', repr(str(file_path)))
    print('EXISTS:', file_path.exists())
    PyAutoGUIUtilities.upload_file(str(file_path))

    page.wait_file_in_dropzone()

    assert page.dropzone_file_name.is_exists(), (
        'Имя файла не появилось после его загрузки'
    )
    assert page.dropzone_success_mark.is_exists(), (
        'Подтверждающая галочка не появилась после загрузки файла'
    )

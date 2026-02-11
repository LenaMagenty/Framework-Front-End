import pytest

pytest.importorskip('pyautogui')

import sys

from config.config_reader import ConfigReader
from pages.upload_image_page import UploadImagePage

from pathlib import Path


@pytest.mark.skipif(
    sys.platform.startswith("linux"),
    reason="PyAutoGUI tests are not supported on Linux"
)
def test_image_upload(browser):
    file_name = 'New Image.jpeg'
    file_path = Path(__file__).parent / 'New Image.jpeg'

    config = ConfigReader()
    browser.get(config.get('upload_image_url'))

    page = UploadImagePage(browser)
    page.wait_for_open()

    page.upload_file(str(file_path))
    page.wait_uploaded()

    assert page.get_uploaded_file_name() == file_name, (
        f'Загружен файл "{file_name}", '
        f'но получено имя "{page.get_uploaded_file_name()}"'
    )

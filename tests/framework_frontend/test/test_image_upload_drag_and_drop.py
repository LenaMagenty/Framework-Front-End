import pytest
import sys

pytest.importorskip('pyautogui')

from pathlib import Path

from config.config_reader import ConfigReader
from pages.upload_image_page import UploadImagePage


@pytest.mark.skipif(
    sys.platform.startswith("linux"),
    reason="PyAutoGUI tests are not supported on Linux"
)
def test_upload_image_drag_and_drop(browser):
    config = ConfigReader()
    browser.get(config.get("upload_image_url"))

    page = UploadImagePage(browser)
    page.wait_for_open()

    file_path = Path(r'tests/framework_frontend/test/New Image.jpeg').resolve()

    page.drag_file_to_dropzone(file_path=str(file_path))
    page.wait_file_in_dropzone()

    assert page.is_file_in_dropzone(), (
        "Имя файла и/или подтверждающая галочка не появились после загрузки файла"
    )

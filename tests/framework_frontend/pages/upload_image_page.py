from utils.pyautogui import PyAutoGUIUtilities

from elements.web_element import WebElement
from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage


class UploadImagePage(BasePage):
    PAGE_NAME = "UploadImagePage"

    UPLOAD_BTN_LOC = "file-upload"
    SUBMIT_BTN_LOC = "file-submit"
    UPLOADED_FILE_LOC = "uploaded-files"
    UPLOADED_HEADER_LOC = "//h3[normalize-space()='File Uploaded!']"

    DROP_ZONE_LOC = "drag-drop-upload"
    DROPZONE_FILE_NAME_LOC = (
        "//*[@id='drag-drop-upload']"
        "//div[contains(@class,'dz-preview') "
        "and not(ancestor::div[@id='preview-template'])]"
        "//span[@data-dz-name]"
    )
    DROPZONE_SUCCESS_MARK_LOC = (
        "//*[@id='drag-drop-upload']"
        "//div[contains(@class,'dz-preview') "
        "and not(ancestor::div[@id='preview-template'])]"
        "//div[contains(@class,'dz-success-mark')]"
        "//span[normalize-space()='✔']"
    )

    UNIQUE_ELEMENT_LOC = UPLOAD_BTN_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.file_input = Input(
            browser=self.browser,
            locator=self.UPLOAD_BTN_LOC,
            description="File input"
        )
        self.upload_button = Button(
            browser=self.browser,
            locator=self.SUBMIT_BTN_LOC,
            description="Upload button"
        )
        self.uploaded_header = WebElement(
            browser=self.browser,
            locator=self.UPLOADED_HEADER_LOC,
            description="Uploaded header"
        )
        self.uploaded_file_name = WebElement(
            browser=self.browser,
            locator=self.UPLOADED_FILE_LOC,
            description="Uploaded file name"
        )

        self.drop_zone = Button(
            browser=self.browser,
            locator=self.DROP_ZONE_LOC,
            description="Drop zone"
        )
        self.dropzone_file_name = WebElement(
            browser=self.browser,
            locator=self.DROPZONE_FILE_NAME_LOC,
            description="Dropzone file name"
        )
        self.dropzone_success_mark = WebElement(
            browser=self.browser,
            locator=self.DROPZONE_SUCCESS_MARK_LOC,
            description="Dropzone success mark"
        )

        self.unique_element = self.file_input

    def upload_file(self, file_path: str) -> None:
        self.file_input.send_keys(file_path)
        self.upload_button.click()

    def open_file_dialog(self) -> None:
        self.drop_zone.click()

    def wait_uploaded(self) -> None:
        self.uploaded_header.wait_for_presence()

    def wait_file_in_dropzone(self) -> None:
        self.dropzone_file_name.wait_for_presence()
        self.dropzone_success_mark.wait_for_presence()

    def is_file_in_dropzone(self) -> bool:
        return self.dropzone_file_name.is_exists() and self.dropzone_success_mark.is_exists()

    def get_dropzone_file_name(self) -> str:
        return self.dropzone_file_name.get_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.get_text()

    def _get_dropzone_center_screen_point(self) -> dict:
        dropzone_element = self.drop_zone.wait_for_presence()

        return self.browser.execute_script(
            """
            const el = arguments[0];

            const r = el.getBoundingClientRect();
            const chromeY = window.outerHeight - window.innerHeight;

            const x = Math.round(r.left + r.width / 2);
            const y = Math.round(chromeY + r.top + r.height / 2);

            return { x: x, y: y };
            """,
            dropzone_element
        )

    def drag_file_to_dropzone(self, file_path: str) -> None:
        point = self._get_dropzone_center_screen_point()

        PyAutoGUIUtilities.drag_file_from_explorer_to_screen_point(
            file_path=file_path,
            target_x=point["x"],
            target_y=point["y"]
        )

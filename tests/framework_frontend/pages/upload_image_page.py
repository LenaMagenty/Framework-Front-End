from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.web_element import WebElement
from elements.button import Button
from elements.input import Input


class UploadImagePage(BasePage):
    PAGE_NAME = 'UploadImagePage'

    UPLOAD_BTN_LOC = (By.ID, 'file-upload')
    SUBMIT_BTN_LOC = (By.ID, 'file-submit')
    UPLOADED_FILE_LOC = (By.ID, 'uploaded-files')
    UPLOADED_HEADER_LOC = (By.XPATH, "//h3[normalize-space()='File Uploaded!']")
    DROP_ZONE_LOC = (By.ID, 'drag-drop-upload')
    DROPZONE_FILE_NAME_LOC = (
        By.XPATH,
        "//div[@id='drag-drop-upload']"
        "//div[contains(@class,'dz-preview') and not(ancestor::div[@id='preview-template'])]"
        "//span[@data-dz-name]"
    )
    DROPZONE_SUCCESS_MARK_LOC = (
        By.XPATH,
        "//div[@id='drag-drop-upload']"
        "//div[contains(@class,'dz-preview') and not(ancestor::div[@id='preview-template'])]"
        "//div[contains(@class,'dz-success-mark')]"
        "//span[normalize-space()='✔']"
    )

    UNIQUE_ELEMENT_LOC = UPLOAD_BTN_LOC

    def __init__(self, browser):
        super().__init__(browser)

        self.file_input = Input(
            browser=self.browser,
            locator=self.UPLOAD_BTN_LOC,
            description='File input'
        )

        self.upload_button = Button(
            browser=self.browser,
            locator=self.SUBMIT_BTN_LOC,
            description='Upload button'
        )

        self.uploaded_header = WebElement(
            browser=self.browser,
            locator=self.UPLOADED_HEADER_LOC,
            description='Uploaded header'
        )

        self.uploaded_file_name = WebElement(
            browser=self.browser,
            locator=self.UPLOADED_FILE_LOC,
            description='Uploaded file name'
        )

        self.drop_zone = Button(
            browser=self.browser,
            locator=self.DROP_ZONE_LOC,
            description='Drop zone'
        )

        self.dropzone_file_name = WebElement(
            browser=self.browser,
            locator=self.DROPZONE_FILE_NAME_LOC,
            description='Dropzone file name'
        )

        self.dropzone_success_mark = WebElement(
            browser=self.browser,
            locator=self.DROPZONE_SUCCESS_MARK_LOC,
            description='Dropzone success mark'
        )

    def upload_file(self, file_path: str) -> None:
        self.file_input.send_keys(file_path)
        self.upload_button.click()

    def wait_uploaded(self) -> None:
        self.uploaded_header.wait_for_presence()

    def open_file_dialog(self) -> None:
        self.drop_zone.click()

    def wait_file_in_dropzone(self) -> None:
        self.dropzone_file_name.wait_for_presence()
        self.dropzone_success_mark.wait_for_presence()

    def get_dropzone_file_name(self) -> str:
        return self.dropzone_file_name.get_text()

from pages.base_page import BasePage
from elements.web_element import WebElement
from logger.logger import Logger


class FramesPage(BasePage):
    PAGE_NAME = 'FramesPage'

    UNIQUE_ELEMENT_LOC = "//*[@id='framesWrapper']//h1[normalize-space()='Frames']"

    ALERTS_FRAME_WINDOWS_GROUP_LOC = (
        "//div[contains(@class,'element-group')]"
        "[.//div[contains(@class,'header-text')][normalize-space()='Alerts, Frame & Windows']]"
    )

    MENU_ITEMS_LOC = (
        "//div[contains(@class,'element-group')]"
        "[.//div[contains(@class,'header-text')][normalize-space()='Alerts, Frame & Windows']]"
        "//ul[contains(@class,'menu-list')]"
    )

    NESTED_FRAMES_ITEM_LOC = "//span[normalize-space()='Nested Frames']"
    FRAMES_ITEM_LOC = "//span[normalize-space()='Frames']"

    TOP_FRAME_LOC = 'frame1'
    BOTTOM_FRAME_LOC = 'frame2'
    FRAME_TEXT_LOC = 'sampleHeading'

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = WebElement(
            browser=self.browser,
            locator=self.UNIQUE_ELEMENT_LOC,
            description='Frames header'
        )

        self.alerts_group = WebElement(
            browser=self.browser,
            locator=self.ALERTS_FRAME_WINDOWS_GROUP_LOC,
            description='Alerts, Frame & Windows group'
        )
        self.menu_items = WebElement(
            browser=self.browser,
            locator=self.MENU_ITEMS_LOC,
            description='Alerts, Frame & Windows menu items'
        )

        self.nested_frames_item = WebElement(
            browser=self.browser,
            locator=self.NESTED_FRAMES_ITEM_LOC,
            description='Nested Frames menu item'
        )
        self.frames_item = WebElement(
            browser=self.browser,
            locator=self.FRAMES_ITEM_LOC,
            description='Frames menu item'
        )

        self.top_frame = WebElement(
            browser=self.browser,
            locator=self.TOP_FRAME_LOC,
            description='Top frame'
        )
        self.bottom_frame = WebElement(
            browser=self.browser,
            locator=self.BOTTOM_FRAME_LOC,
            description='Bottom frame'
        )
        self.frame_text = WebElement(
            browser=self.browser,
            locator=self.FRAME_TEXT_LOC,
            description='Frame text'
        )

    def ensure_alerts_frame_windows_group_opened(self) -> None:
        Logger.info(f'{self}: ensure Alerts, Frame & Windows group opened')

        if self.menu_items.is_visible():
            Logger.info(f'{self}: menu already opened')
            return

        self.alerts_group.click()
        self.menu_items.wait_for_visible()

    def open_nested_frames(self) -> None:
        Logger.info(f'{self}: open Nested Frames from menu')
        self.nested_frames_item.click()

    def open_frames(self) -> None:
        Logger.info(f'{self}: open Frames from menu')
        self.frames_item.click()

    def _get_text_from_frame(self, frame: WebElement) -> str:
        self.browser.switch_to_frame(frame)
        text = self.frame_text.get_text().strip()
        self.browser.switch_to_default_content()
        return text

    def get_top_frame_text(self) -> str:
        return self._get_text_from_frame(self.top_frame)

    def get_bottom_frame_text(self) -> str:
        return self._get_text_from_frame(self.bottom_frame)

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from elements.base_element import BaseElement
from logger.logger import Logger


class FramesPage(BasePage):
    PAGE_NAME = 'FramesPage'

    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@id='framesWrapper']//h1[normalize-space()='Frames']"
    )

    ALERTS_FRAME_WINDOWS_GROUP = (
        By.XPATH,
        "//div[contains(@class,'element-group')]"
        "[.//div[contains(@class,'header-text')][normalize-space()='Alerts, Frame & Windows']]"
    )

    MENU_ITEMS = (
        By.XPATH,
        "//div[contains(@class,'element-group')]"
        "[.//div[contains(@class,'header-text')][normalize-space()='Alerts, Frame & Windows']]"
        "//ul[contains(@class,'menu-list')]"
    )

    NESTED_FRAMES_ITEM = (By.XPATH, "//span[normalize-space()='Nested Frames']")
    FRAMES_ITEM = (By.XPATH, "//span[normalize-space()='Frames']")

    TOP_FRAME = (By.ID, 'frame1')
    BOTTOM_FRAME = (By.ID, 'frame2')
    FRAME_TEXT = (By.ID, 'sampleHeading')

    def __init__(self, browser):
        super().__init__(browser)

        self.alerts_group = BaseElement(
            self.browser, self.ALERTS_FRAME_WINDOWS_GROUP, 'Alerts, Frame & Windows group'
        )
        self.menu_items = BaseElement(
            self.browser, self.MENU_ITEMS, 'Alerts, Frame & Windows menu items'
        )
        self.nested_frames_item = BaseElement(
            self.browser, self.NESTED_FRAMES_ITEM, 'Nested Frames menu item'
        )
        self.frames_item = BaseElement(
            self.browser, self.FRAMES_ITEM, 'Frames menu item'
        )

        self.top_frame = BaseElement(self.browser, self.TOP_FRAME, 'Top frame')
        self.bottom_frame = BaseElement(self.browser, self.BOTTOM_FRAME, 'Bottom frame')
        self.frame_text = BaseElement(self.browser, self.FRAME_TEXT, 'Frame text')

    def ensure_alerts_frame_windows_group_opened(self) -> None:
        Logger.info(f'{self}: ensure Alerts, Frame & Windows group opened')

        if self.menu_items.is_visible():
            Logger.info(f'{self}: menu already opened')
            return

        self.alerts_group.wait_for_clickable().click()
        self.menu_items.wait_for_visible()

    def open_nested_frames(self) -> None:
        Logger.info(f'{self}: open Nested Frames from menu')
        self.nested_frames_item.wait_for_clickable().click()

    def open_frames(self) -> None:
        Logger.info(f'{self}: open Frames from menu')
        self.frames_item.wait_for_clickable().click()

    def _get_text_from_frame(self, frame: BaseElement) -> str:
        self.browser.switch_to_frame(frame)
        text = self.frame_text.wait_for_presence().text.strip()
        self.browser.switch_to_default_content()
        return text

    def get_top_frame_text(self) -> str:
        return self._get_text_from_frame(self.top_frame)

    def get_bottom_frame_text(self) -> str:
        return self._get_text_from_frame(self.bottom_frame)

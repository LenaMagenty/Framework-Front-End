import logging
import time
import os

import pyautogui

from logger.logger import Logger


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(3)  # timeout after opening File Dialog

        logging.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.typewrite(file_path)
        logging.debug("Press enter")
        pyautogui.hotkey("enter")

        time.sleep(3)  # timeout before closing File Dialog

    @staticmethod
    def drag_file_from_explorer_to_screen_point(
            file_path: str,
            target_x: int,
            target_y: int
    ) -> None:
        folder, file_name = os.path.split(file_path)

        Logger.info('Open Explorer')
        os.startfile(folder)
        time.sleep(2)

        Logger.info('Select file')
        pyautogui.typewrite(file_name)
        time.sleep(2)

        Logger.info('Drag file to dropzone')
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.moveTo(target_x, target_y, duration=3)
        pyautogui.mouseUp()

        time.sleep(1)

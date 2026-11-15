"""Base page with shared UI interaction helpers."""

from typing import List, Tuple

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver as AppiumDriver
from selenium.common.exceptions import TimeoutException

from utils.logger import get_logger
from utils.wait_utils import WaitUtils

Locator = Tuple[str, str]


class BasePage:
    """All page objects inherit from this class."""

    def __init__(self, driver: AppiumDriver):
        self.driver = driver
        self.wait_utils = WaitUtils(driver)
        self.logger = get_logger(self.__class__.__name__)

    # --- low-level helpers ---
    def find_element(self, locator: Locator):
        self.wait_utils.wait_for_element_visible(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Locator) -> List:
        self.wait_utils.wait_for_element_present(locator)
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:
        self.logger.info("Clicking element: %s", locator)
        self.wait_utils.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).click()

    def send_keys(self, locator: Locator, text: str) -> None:
        self.logger.info("Typing '%s' into element: %s", text, locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find_element(locator).text

    def is_element_displayed(self, locator: Locator) -> bool:
        try:
            self.wait_utils.wait_for_element_visible(locator)
            return self.driver.find_element(*locator).is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator: Locator) -> bool:
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    # --- mobile gestures ---
    def scroll_to_text(self, text: str) -> None:
        """Scroll until an element with the given text is visible (UiScrollable)."""
        scrollable = (
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().textContains("{text}"))'
        )
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable)

    def hide_keyboard(self) -> None:
        try:
            self.driver.hide_keyboard()
        except Exception:  # keyboard may not be open
            pass

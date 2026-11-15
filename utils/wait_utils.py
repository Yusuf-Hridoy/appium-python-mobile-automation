"""Explicit wait helpers built on WebDriverWait."""

from typing import Tuple

from appium.webdriver.webdriver import WebDriver as AppiumDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.settings import Settings

Locator = Tuple[str, str]


class WaitUtils:
    """Reusable wait strategies for Appium elements."""

    def __init__(self, driver: AppiumDriver, timeout: int = None):
        self.driver = driver
        self.timeout = timeout or Settings.EXPLICIT_WAIT
        self.wait = WebDriverWait(driver, self.timeout)

    def wait_for_element_visible(self, locator: Locator) -> None:
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator: Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_present(self, locator: Locator) -> None:
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_invisible(self, locator: Locator) -> None:
        self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_text_present(self, locator: Locator, text: str) -> None:
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

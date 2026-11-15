"""Appium driver initialization and lifecycle management."""

from appium import webdriver
from appium.webdriver.webdriver import WebDriver as AppiumDriver

from config.capabilities import android_capabilities
from config.settings import Settings


class DriverFactory:
    """Creates and tears down Appium driver instances."""

    @staticmethod
    def create_driver() -> AppiumDriver:
        """Start a new Appium session against the configured device/emulator."""
        driver = webdriver.Remote(
            command_executor=Settings.APPIUM_SERVER_URL,
            options=android_capabilities(),
        )
        driver.implicitly_wait(Settings.IMPLICIT_WAIT)
        return driver

    @staticmethod
    def quit_driver(driver: AppiumDriver) -> None:
        """Safely terminate the Appium session."""
        if driver is not None:
            driver.quit()

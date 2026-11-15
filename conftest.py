"""Pytest fixtures: Appium driver lifecycle and page object injection."""

import pytest

from config.settings import Settings
from drivers.driver_factory import DriverFactory
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger(__name__)


@pytest.fixture()
def driver():
    """Create a fresh Appium session per test and always quit afterwards."""
    logger.info("=== Starting Appium session ===")
    appium_driver = DriverFactory.create_driver()
    yield appium_driver
    DriverFactory.quit_driver(appium_driver)
    logger.info("=== Appium session ended ===")


# --- Page object fixtures ---
@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture()
def menu_page(driver):
    return MenuPage(driver)


@pytest.fixture()
def logged_in_home_page(driver, login_page):
    """Precondition fixture: logs in with valid credentials and returns HomePage."""
    login_page.login(Settings.VALID_USERNAME, Settings.VALID_PASSWORD)
    home = HomePage(driver)
    assert home.is_home_page_displayed(), "Login failed - home page not displayed"
    return home


# --- Failure hook: screenshot on test failure ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and Settings.SCREENSHOT_ON_FAILURE:
        driver = item.funcargs.get("driver")
        if driver is not None:
            take_screenshot(driver, item.name)

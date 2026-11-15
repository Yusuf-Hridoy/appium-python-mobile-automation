"""Side menu (settings drawer) locators and actions (SwagLabs)."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage, Locator


class MenuPage(BasePage):
    # --- Locators ---
    MENU_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Menu")
    ALL_ITEMS: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-ALL ITEMS")
    LOGOUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGOUT")
    ABOUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-ABOUT")
    CLOSE_MENU: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Close")
    MENU_DRAWER: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Menu item scroll view")

    def open_menu(self) -> None:
        self.click(self.MENU_BUTTON)

    def is_menu_open(self) -> bool:
        return self.is_element_displayed(self.MENU_DRAWER)

    def close_menu(self) -> None:
        self.click(self.CLOSE_MENU)

    def logout(self) -> None:
        self.open_menu()
        self.click(self.LOGOUT)

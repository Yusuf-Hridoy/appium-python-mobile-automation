"""Checkout (information, overview, complete) locators and actions (SwagLabs)."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage, Locator


class CheckoutPage(BasePage):
    # --- Locators: checkout information ---
    FIRST_NAME_INPUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    LAST_NAME_INPUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    POSTAL_CODE_INPUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    CONTINUE_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
    ERROR_MESSAGE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Error message")

    # --- Locators: checkout overview / complete ---
    OVERVIEW_TITLE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: OVERVIEW")
    FINISH_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")
    COMPLETE_TITLE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT: COMPLETE!")
    BACK_HOME_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-BACK HOME")

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)
        self.hide_keyboard()
        self.click(self.CONTINUE_BUTTON)

    def is_error_message_displayed(self) -> bool:
        """True when the checkout form shows a validation error."""
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def finish_order(self) -> None:
        """Tap FINISH, scrolling it into view first - it sits below the fold."""
        if not self.is_element_present(self.FINISH_BUTTON):
            self.scroll_to_text("FINISH")
        self.click(self.FINISH_BUTTON)

    def is_checkout_complete_displayed(self) -> bool:
        return self.is_element_displayed(self.COMPLETE_TITLE)

    def go_back_home(self) -> None:
        self.click(self.BACK_HOME_BUTTON)

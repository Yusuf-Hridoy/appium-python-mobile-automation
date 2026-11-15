"""Login page locators and actions (SwagLabs)."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage, Locator


class LoginPage(BasePage):
    # --- Locators ---
    USERNAME_INPUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_INPUT: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    ERROR_MESSAGE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Error message")
    # The accessibility-id node is a React Native container View with no text of its
    # own; the visible message sits in a nested TextView, so read the text from there.
    ERROR_MESSAGE_TEXT: Locator = (
        AppiumBy.XPATH,
        '//*[@content-desc="test-Error message"]//android.widget.TextView',
    )

    def login(self, username: str, password: str) -> None:
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.hide_keyboard()
        self.click(self.LOGIN_BUTTON)

    def is_login_page_displayed(self) -> bool:
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return the visible login error text (read from the nested TextView)."""
        return self.get_text(self.ERROR_MESSAGE_TEXT)

    def is_error_message_displayed(self) -> bool:
        return self.is_element_displayed(self.ERROR_MESSAGE)

"""Cart page locators and actions (SwagLabs)."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage, Locator


class CartPage(BasePage):
    # --- Locators ---
    # The app has no "test-Your Cart" id; the cart container is "test-Cart Content".
    YOUR_CART_TITLE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Cart Content")
    # On the cart screen items expose "test-Description", whose first TextView is the
    # product name (the second is the long description). "test-Item title" is home-only.
    CART_ITEM_TITLES: Locator = (
        AppiumBy.XPATH,
        '//*[@content-desc="test-Description"]/android.widget.TextView[1]',
    )
    CHECKOUT_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
    CONTINUE_SHOPPING_BUTTON: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE SHOPPING")
    REMOVE_BUTTONS: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")

    def is_cart_page_displayed(self) -> bool:
        return self.is_element_displayed(self.YOUR_CART_TITLE)

    def get_cart_item_titles(self) -> list:
        return [el.text for el in self.find_elements(self.CART_ITEM_TITLES)]

    def proceed_to_checkout(self) -> None:
        """Tap CHECKOUT, scrolling it into view first when the cart is long."""
        if not self.is_element_present(self.CHECKOUT_BUTTON):
            self.scroll_to_text("CHECKOUT")
        self.click(self.CHECKOUT_BUTTON)

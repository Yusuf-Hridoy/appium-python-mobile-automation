"""Home / Products page locators and actions (SwagLabs)."""

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage, Locator


class HomePage(BasePage):
    # --- Locators ---
    PRODUCTS_TITLE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    PRODUCT_TITLES: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Item title")
    ADD_TO_CART_BUTTONS: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    REMOVE_BUTTONS: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-REMOVE")
    CART_BADGE: Locator = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")
    # The app exposes no "test-Cart badge" id; the count is a bare TextView nested
    # inside test-Cart, and it is simply absent when the cart is empty.
    CART_BADGE_COUNT: Locator = (
        AppiumBy.XPATH,
        '//*[@content-desc="test-Cart"]//android.widget.TextView',
    )

    def is_home_page_displayed(self) -> bool:
        return self.is_element_displayed(self.PRODUCTS_TITLE)

    def get_product_titles(self) -> list:
        return [el.text for el in self.find_elements(self.PRODUCT_TITLES)]

    def add_product_to_cart_by_index(self, index: int) -> None:
        """Tap the ADD TO CART button at `index` among those currently rendered.

        Only on-screen items exist in the hierarchy, and a product's button turns
        into REMOVE once added - so this list shrinks and re-indexes as you add.
        To add several products use :meth:`add_first_available_product_to_cart`.
        """
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index >= len(buttons):
            raise IndexError(
                f"ADD TO CART index {index} out of range: only {len(buttons)} button(s) "
                f"rendered. Off-screen products are not addressable by index."
            )
        buttons[index].click()

    def add_first_available_product_to_cart(self) -> None:
        """Tap the first ADD TO CART button on screen.

        Calling this twice adds two different products: the first one's button
        becomes REMOVE, so the next available button belongs to another item.
        """
        self.add_product_to_cart_by_index(0)

    def get_cart_badge_count(self) -> int:
        """Number on the cart badge, or 0 when the cart is empty.

        The cart icon itself must be present - if it is not, the locator or the
        current screen is wrong, and that should surface rather than read as 0.
        """
        self.find_element(self.CART_BADGE)
        counts = self.driver.find_elements(*self.CART_BADGE_COUNT)
        return int(counts[0].text) if counts else 0

    def open_cart(self) -> None:
        self.click(self.CART_BADGE)

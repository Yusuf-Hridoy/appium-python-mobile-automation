"""Shopping cart feature test scenarios."""

import pytest


@pytest.mark.cart
class TestCart:
    def test_products_are_displayed_on_home_page(self, logged_in_home_page):
        titles = logged_in_home_page.get_product_titles()
        assert len(titles) > 0, "At least one product should be listed"
        assert any("Sauce Labs" in title for title in titles)

    def test_add_single_product_to_cart(self, logged_in_home_page):
        logged_in_home_page.add_product_to_cart_by_index(0)
        assert logged_in_home_page.get_cart_badge_count() == 1

    def test_add_multiple_products_to_cart(self, logged_in_home_page):
        logged_in_home_page.add_first_available_product_to_cart()
        logged_in_home_page.add_first_available_product_to_cart()
        assert logged_in_home_page.get_cart_badge_count() == 2

    def test_cart_page_shows_added_product(self, logged_in_home_page, cart_page):
        titles_before = logged_in_home_page.get_product_titles()
        logged_in_home_page.add_product_to_cart_by_index(0)
        logged_in_home_page.open_cart()
        assert cart_page.is_cart_page_displayed(), "Cart page should be displayed"
        cart_titles = cart_page.get_cart_item_titles()
        assert len(cart_titles) == 1
        assert cart_titles[0] == titles_before[0]

    def test_continue_shopping_from_cart(self, logged_in_home_page, cart_page):
        logged_in_home_page.add_product_to_cart_by_index(0)
        logged_in_home_page.open_cart()
        cart_page.click(cart_page.CONTINUE_SHOPPING_BUTTON)
        assert logged_in_home_page.is_home_page_displayed(), "Should return to products page"

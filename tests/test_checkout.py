"""Checkout feature test scenarios."""

import pytest


@pytest.mark.checkout
class TestCheckout:
    @pytest.mark.parametrize(
        "first_name,last_name,postal_code",
        [("John", "Doe", "10001")],
    )
    def test_complete_checkout_flow(
        self, logged_in_home_page, cart_page, checkout_page, first_name, last_name, postal_code
    ):
        logged_in_home_page.add_product_to_cart_by_index(0)
        logged_in_home_page.open_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_checkout_information(first_name, last_name, postal_code)
        assert checkout_page.is_element_displayed(checkout_page.OVERVIEW_TITLE)

        checkout_page.finish_order()
        assert checkout_page.is_checkout_complete_displayed(), "Order completion message should be shown"

        checkout_page.go_back_home()
        assert logged_in_home_page.is_home_page_displayed(), "Should return to home page"

    def test_checkout_without_information_shows_error(
        self, logged_in_home_page, cart_page, checkout_page
    ):
        logged_in_home_page.add_product_to_cart_by_index(0)
        logged_in_home_page.open_cart()
        cart_page.proceed_to_checkout()

        checkout_page.click(checkout_page.CONTINUE_BUTTON)
        assert checkout_page.is_error_message_displayed(), "Error should be shown for empty fields"

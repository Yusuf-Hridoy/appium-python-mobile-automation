"""Login feature test scenarios."""

import pytest

from config.settings import Settings


@pytest.mark.login
class TestLogin:
    def test_login_with_valid_credentials(self, login_page, home_page):
        login_page.login(Settings.VALID_USERNAME, Settings.VALID_PASSWORD)
        assert home_page.is_home_page_displayed(), "Home page should be displayed after login"

    def test_login_with_invalid_credentials(self, login_page):
        login_page.login("invalid_user", "wrong_password")
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "Username and password do not match" in login_page.get_error_message()

    def test_login_with_locked_out_user(self, login_page):
        login_page.login(Settings.LOCKED_USERNAME, Settings.VALID_PASSWORD)
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert "locked out" in login_page.get_error_message().lower()

    def test_login_without_credentials(self, login_page):
        login_page.login("", "")
        assert login_page.is_error_message_displayed(), "Error message should be displayed"

    def test_logout_returns_to_login_page(self, logged_in_home_page, menu_page, login_page):
        menu_page.logout()
        assert login_page.is_login_page_displayed(), "Login page should be displayed after logout"

# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project overview

Python + Appium 2.x (UiAutomator2) mobile automation framework targeting the **SwagLabs
(Sauce Labs) demo Android app** (`com.swaglabsmobileapp`). Test runner: **Pytest**.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install Appium-Python-Client pytest pytest-html python-dotenv selenium
```

Requirements to run tests (not installable via pip):

- Appium 2.x server running with the `uiautomator2` driver (`appium driver install uiautomator2`)
- Android emulator or real device visible in `adb devices`
- SwagLabs APK at `apps/Android.SauceLabs.Mobile.Sample.app.apk`
  (download: https://github.com/saucelabs/sample-app-mobile/releases)
- Environment config: copy `.env.example` to `.env` and adjust device values

Run tests with `pytest` (see README.md for filter/report options).

## Architecture rules

- **Page Object Model is mandatory.** All locators live in `pages/*_page.py` classes
  inheriting from `pages/base_page.py`. Never locate elements inside test files.
- Locator convention: class-level tuples `Locator = (AppiumBy.ACCESSIBILITY_ID, "test-...")`.
  The SwagLabs app exposes accessibility ids (`test-Username`, `test-LOGIN`, ...) — prefer
  them over XPath.
- `BasePage` provides `click`, `send_keys`, `get_text`, `find_element(s)`,
  `is_element_displayed/present`, and mobile gestures (`scroll_to_text`, `hide_keyboard`).
  Reuse these instead of raw driver calls.
- `conftest.py` owns driver lifecycle: the `driver` fixture creates and quits one Appium
  session **per test** (function scope — do not change to session scope; tests mutate
  app state). Page objects are injected via fixtures (`login_page`, `home_page`, ...).
- Driver creation goes through `drivers/driver_factory.py`; capabilities through
  `config/capabilities.py`; environment values through `config/settings.py` (reads `.env`).
  Never hardcode capabilities, credentials, or paths outside `config/` and `.env`.
- Waits: use `utils/wait_utils.py` / `BasePage` helpers (explicit waits). Do not sprinkle
  `time.sleep()` — if a wait is missing, add a helper in `WaitUtils`.
- Logging: use `utils/logger.py` `get_logger(__name__)` in pages/utils.
- Screenshots on failure are automatic via the `pytest_runtest_makereport` hook in
  `conftest.py` (saves to `reports/screenshots/`).

## Testing conventions

- Tests live in `tests/test_<feature>.py`, grouped in classes `Test<Feature>` with a
  matching pytest marker (`@pytest.mark.login`, `@pytest.mark.cart`, `@pytest.mark.checkout`).
  New features: add the marker to `pytest.ini`.
- Test names: `test_<behavior>`, e.g. `test_login_with_valid_credentials`.
- Assertions carry message strings explaining the expected outcome.
- Reuse the `logged_in_home_page` fixture as the precondition for any test that starts
  past the login screen.
- SwagLabs accounts come from `Settings` (`VALID_USERNAME`, `VALID_PASSWORD`,
  `LOCKED_USERNAME`) — never inline credentials in tests.

## Validation

- `pytest --collect-only -q` must succeed (12 tests at time of writing) after any change.
- Actually executing tests requires a running Appium server + device; if unavailable,
  validate with collection plus `python -c "import conftest"` style import checks.

## Style

- Python 3.10+, type hints on helpers, Google-style docstrings on modules/classes.
- Keep changes minimal and consistent with existing file layout.
- Windows environment: use PowerShell syntax in any shell instructions.

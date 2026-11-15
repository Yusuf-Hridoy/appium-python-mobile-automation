# Appium Python Framework — SwagLabs Android

A maintainable mobile automation framework built with **Python + Pytest + Appium 2.x (UiAutomator2)**,
targeting the **SwagLabs (Sauce Labs) demo Android app**.

## Project structure

```
appium-framework/
├── config/            # Settings, device capabilities, environment config
│   ├── settings.py        # env-driven configuration (reads .env)
│   └── capabilities.py    # UiAutomator2Options builder
├── pages/             # Page Objects: locators + UI actions
│   ├── base_page.py       # shared element/gesture helpers
│   ├── login_page.py      # login screen
│   ├── home_page.py       # products (home) screen
│   ├── cart_page.py       # cart screen
│   ├── checkout_page.py   # checkout information/overview/complete
│   └── menu_page.py       # side menu / settings drawer (logout, about)
├── tests/             # Test scenarios grouped by feature
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/             # Wait helpers, logging, screenshots
│   ├── wait_utils.py
│   ├── logger.py
│   └── screenshot.py
├── drivers/           # Appium driver initialization and lifecycle
│   └── driver_factory.py
├── reports/           # pytest-html reports + failure screenshots
├── logs/              # framework.log diagnostics
├── apps/              # put the SwagLabs APK here
├── conftest.py        # fixtures (driver, page objects) + failure screenshot hook
├── pytest.ini         # pytest config and markers
├── pyproject.toml     # dependencies
└── .env.example       # environment template (copy to .env)
```

## Prerequisites

1. **Python 3.10+**
2. **Node.js + Appium 2.x**: `npm install -g appium` then `appium driver install uiautomator2`
3. **Android SDK / platform-tools** with `adb` on PATH
4. An **Android emulator running** (or a real device with USB debugging enabled)
5. The **SwagLabs APK** downloaded from
   [saucelabs/sample-app-mobile releases](https://github.com/saucelabs/sample-app-mobile/releases)
   and placed in `apps/Android.SauceLabs.Mobile.Sample.app.apk`

## Setup

```bash
# 1. Create virtual environment and install dependencies
python -m venv .venv
.venv\Scripts\activate
pip install -e .          # or: pip install Appium-Python-Client pytest pytest-html python-dotenv selenium

# 2. Configure environment
copy .env.example .env
# edit .env -> set DEVICE_NAME / PLATFORM_VERSION / APP_PATH for your device

# 3. Start Appium server (separate terminal)
appium

# 4. Verify a device is connected
adb devices
```

## Running tests

```bash
pytest                                # run everything
pytest -m login                       # run only login feature
pytest tests/test_cart.py             # run a single file
pytest -k "valid_credentials"         # run by test name
pytest --html=reports/report.html     # run + generate HTML report
```

- Failed tests automatically save a screenshot to `reports/screenshots/`.
- Logs are written to `logs/framework.log`.
- HTML report opens the full execution detail: `reports/report.html`.

## SwagLabs test accounts

| Username          | Password       | Purpose                 |
|-------------------|----------------|-------------------------|
| standard_user     | secret_sauce   | Happy-path login        |
| locked_out_user   | secret_sauce   | Locked-out error flow   |

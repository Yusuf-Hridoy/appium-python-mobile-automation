"""Builds Appium desired capabilities for the SwagLabs Android app."""

from appium.options.android import UiAutomator2Options

from config.settings import Settings


def android_capabilities() -> UiAutomator2Options:
    """Return UiAutomator2Options configured for the SwagLabs demo app."""
    options = UiAutomator2Options()
    options.platform_name = Settings.PLATFORM_NAME
    options.automation_name = "UiAutomator2"
    options.device_name = Settings.DEVICE_NAME
    options.app_package = Settings.APP_PACKAGE
    options.app_activity = Settings.APP_ACTIVITY
    options.no_reset = Settings.NO_RESET
    options.full_reset = Settings.FULL_RESET
    options.new_command_timeout = 300
    options.auto_grant_permissions = True
    options.set_capability("appium:appWaitActivity", "*")

    if Settings.PLATFORM_VERSION:
        options.platform_version = Settings.PLATFORM_VERSION
    if Settings.UDID:
        options.udid = Settings.UDID
    # Only attach the apk when it actually exists (e.g. device already has the app).
    import os
    if os.path.exists(Settings.APP_PATH):
        options.app = Settings.APP_PATH

    return options

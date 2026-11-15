"""Centralized settings loaded from environment variables (.env file)."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def _get(key: str, default: str = "") -> str:
    return os.getenv(key, default)


class Settings:
    """Framework-wide configuration values."""

    # --- Appium server ---
    APPIUM_SERVER_URL: str = _get("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    # --- Device ---
    PLATFORM_NAME: str = _get("PLATFORM_NAME", "Android")
    PLATFORM_VERSION: str = _get("PLATFORM_VERSION", "")
    DEVICE_NAME: str = _get("DEVICE_NAME", "Android Emulator")
    UDID: str = _get("UDID", "")

    # --- Application under test (SwagLabs demo app) ---
    APP_PATH: str = _get("APP_PATH", str(PROJECT_ROOT / "apps" / "Android.SauceLabs.Mobile.Sample.app.apk"))
    APP_PACKAGE: str = _get("APP_PACKAGE", "com.swaglabsmobileapp")
    APP_ACTIVITY: str = _get("APP_ACTIVITY", "com.swaglabsmobileapp.MainActivity")
    NO_RESET: bool = _get("NO_RESET", "false").lower() == "true"
    FULL_RESET: bool = _get("FULL_RESET", "false").lower() == "true"

    # --- SwagLabs test accounts ---
    VALID_USERNAME: str = _get("VALID_USERNAME", "standard_user")
    VALID_PASSWORD: str = _get("VALID_PASSWORD", "secret_sauce")
    LOCKED_USERNAME: str = _get("LOCKED_USERNAME", "locked_out_user")

    # --- Framework ---
    IMPLICIT_WAIT: int = int(_get("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT: int = int(_get("EXPLICIT_WAIT", "20"))
    SCREENSHOT_ON_FAILURE: bool = _get("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

    # --- Paths ---
    REPORTS_DIR: Path = PROJECT_ROOT / "reports"
    LOGS_DIR: Path = PROJECT_ROOT / "logs"

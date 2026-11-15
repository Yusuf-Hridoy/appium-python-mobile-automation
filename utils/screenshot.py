"""Screenshot capture helpers."""

from datetime import datetime
from pathlib import Path

from appium.webdriver.webdriver import WebDriver as AppiumDriver

from config.settings import Settings
from utils.logger import get_logger

logger = get_logger(__name__)


def take_screenshot(driver: AppiumDriver, name: str) -> Path:
    """Save a timestamped PNG screenshot under reports/screenshots/."""
    screenshots_dir = Path(Settings.REPORTS_DIR) / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = screenshots_dir / f"{name}_{timestamp}.png"
    driver.save_screenshot(str(file_path))
    logger.info("Screenshot saved: %s", file_path)
    return file_path

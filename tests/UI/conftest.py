import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def playwright_browser():
    playwright = sync_playwright().start()
    # chromium firefox webkit
    browser = getattr(playwright, 'chromium').launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()

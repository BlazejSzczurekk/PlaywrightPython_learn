import pytest
from playwright.sync_api import sync_playwright

def test_name():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://google.com')
        print(page.title())
        assert "Google" in page.title()
        browser.close()
    
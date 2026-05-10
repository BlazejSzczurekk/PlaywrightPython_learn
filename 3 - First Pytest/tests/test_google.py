import re
from playwright.sync_api import expect

def test_google_search(page):
  
    page.goto("https://www.google.com/ncr")
    page.wait_for_timeout(2000)
    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
    except:
        print("no popup")
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.wait_for_timeout(1000)
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
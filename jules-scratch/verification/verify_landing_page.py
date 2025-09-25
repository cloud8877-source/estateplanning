from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    # Using an absolute file path to ensure it can be found
    page.goto(f"file:///app/index.html")
    page.set_viewport_size({"width": 1280, "height": 800})
    page.screenshot(path="jules-scratch/verification/verification.png", full_page=True)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)